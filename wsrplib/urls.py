""" Generate / parse rewritable URLs, per WSRP v1 section 10.2.
"""
import re
from urllib import quote_plus


def _quote(x):
    return quote_plus(str(x))

RENDER = 'render'
BLOCKING_ACTION = 'blockingAction'
RESOURCE = 'resource'

_URL_TYPES = (RENDER, BLOCKING_ACTION, RESOURCE)


def rewritableURL(urlType, 
                  navigationalState=None,
                  interactionState=None,
                  mode=None,
                  windowState=None,
                  fragmentID=None,
                  secureURL=None,
                  resourceURL=None,
                  resourceRequiresRewrite=False,
                 ):
    """ Generate a consumer-rewritable URL.
    
    - These URLs conform to WSRP v1, section 10.2.1.  Please see that
      section for the semantics of the fields.

    - Values in 'kw' do *not* need to be URL-encoded.

    - 'urlType' must be one of the allowed values: "render", "blockingAction",
      or "resource".

    - If 'urlType' is "resource", then 'resourceURL' is required;  otherwise,
      'resourceURL' is not allowed.
    """
    _checkPreconditions(urlType, resourceURL=resourceURL)

    nvlist = [('wsrp-urlType', urlType)]
    if navigationalState is not None:
        nvlist.append(('wsrp-navigationalState', _quote(navigationalState)))

    if interactionState is not None:
        nvlist.append(('wsrp-interactionState', _quote(interactionState)))

    if mode is not None:
        nvlist.append(('wsrp-mode', _quote(mode)))

    if windowState is not None:
        nvlist.append(('wsrp-windowState', _quote(windowState)))

    if fragmentID is not None:
        nvlist.append(('wsrp-fragmentID', _quote(fragmentID)))

    if secureURL is not None:
        nvlist.append(('wsrp-secureURL', _quote(secureURL)))

    if urlType == RESOURCE:

        if resourceURL is not None:
            nvlist.append(('wsrp-resourceURL', _quote(resourceURL)))

        if resourceRequiresRewrite is not None:
            nvlist.append(('wsrp-resourceRequiresRewrite',
                          _quote(resourceRequiresRewrite)))

    qs = '&amp;'.join(['='.join(nv)for nv in nvlist])
    return 'wsrp_rewrite?%s/wsrp_rewrite' % qs


def rewrittenURL(urlType, secure, runtime_ctx, portlet_ctx, user_ctx, **kw):
    """ Generate an already-rewritten URL, using consumer-supplied templates.
    
    - These URLs conform to WSRP v1, section 10.2.2.  Please see that
      section for the semantics of the fields.

    - Values in 'kw' do *not* need to be URL-encoded.

    - 'urlType' must be one of the allowed values: "render", "blockingAction",
      or "resource".

    - Select 'templates' from the runtime context as follows:

      - If a template exists matching 'urlType', use it;  otherwise, fall
        back to the default.

      - 'secure' is a boolean, selecting whether to use the "normal" templates
        or the 'secure*' equivalents.

    - If 'urlType' is "resource", then 'resourceURL' is a required keyword
      argument;  otherwise, 'resourceURL' is not allowed.
    """
    _checkPreconditions(urlType, **kw)
    template = _selectTemplate(runtime_ctx, urlType, secure)
    if template is None:
        raise ValueError('Missing template for %s, %s' % (urlType, secure))
    converted = _convertTemplate(template)
    mapping = _getMapping(runtime_ctx, portlet_ctx, user_ctx, kw)
    return converted.format(**mapping)


def _checkPreconditions(urlType, **kw):
    if urlType not in _URL_TYPES:
        raise ValueError('Unknown urlType: %s' % urlType)

    resourceURL = kw.get('resourceURL')

    if urlType == RESOURCE:
        if resourceURL is None:
            raise ValueError(
                    'urlType "resource" requires explicit resourceURL.')
    else:
        if resourceURL is not None:
            raise ValueError(
                    'urlType "%s" incompatible with resourceURL.')

_SECURE_TEMPLATES = {
    RENDER: 'secureRenderTemplate',
    BLOCKING_ACTION: 'secureBlockingActionTemplate',
    RESOURCE: 'secureResourceTemplate',
}

_NON_SECURE_TEMPLATES = {
    RENDER: 'renderTemplate',
    BLOCKING_ACTION: 'blockingActionTemplate',
    RESOURCE: 'resourceTemplate',
}

def _selectTemplate(runtime_ctx, urlType, secure):
    templates = runtime_ctx.templates
    if secure:
        attrs = _SECURE_TEMPLATES[urlType], 'secureDefaultTemplate'
    else:
        attrs = _NON_SECURE_TEMPLATES[urlType], 'defaultTemplate'
    for attr in attrs:
        template = getattr(templates, attr, None)
        if template is not None:
            return template


_REPLACEMENT_TOKEN = re.compile(r'{wsrp-(?P<name>\w+)}')

def _munge(m):
    return '{%s}' % m.group('name')

def _convertTemplate(template):
    return _REPLACEMENT_TOKEN.sub(_munge, template)


def _getMapping(runtime_ctx, portlet_ctx, user_ctx, kw):
    mapping = dict([(k, _quote(v)) for k, v in kw.items()])
    mapping['portletHandle'] = _quote(portlet_ctx.portletHandle)
    mapping['userContextKey'] = _quote(user_ctx.userContextKey)
    mapping['portletInstanceKey'] = _quote(runtime_ctx.portletInstanceKey)
    mapping['sessionID'] = _quote(runtime_ctx.sessionID)
    if 'resourceURL' in mapping:
        mapping.setdefault('resourceRequiresRewrite', False)
    return mapping
