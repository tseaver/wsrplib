""" Generate / parse rewritable URLs, per WSRP v1 section 10.2.
"""
from urllib import urlencode

RENDER = 'render'
BLOCKING_ACTION = 'blockingAction'
RESOURCE = 'resource'

_URL_TYPES = (RENDER, BLOCKING_ACTION, RESOURCE)


def generateConsumerRewritableURL(urlType, 
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

    - Values do *not* need to be URL-encoded.

    - 'urlType' must be one of the allowed values: "render", "blockingAction",
      or "resource".

    - If 'urlType' is "resource", then 'resourceURL' is required;  otherwise,
      'resourceURL' is not allowed.
    """
    if urlType not in _URL_TYPES:
        raise ValueError('Unknown urlType: %s' % urlType)

    if urlType == RESOURCE:
        if resourceURL is None:
            raise ValueError(
                    'urlType "resource" requires explicit resourceURL.')
    else:
        if resourceURL is not None:
            raise ValueError(
                    'urlType "%s" incompatible with resourceURL.')

    nvlist = [('wsrp-urlType', urlType)]
    if navigationalState is not None:
        nvlist.append(('wsrp-navigationalState', navigationalState))

    if interactionState is not None:
        nvlist.append(('wsrp-interactionState', interactionState))

    if mode is not None:
        nvlist.append(('wsrp-mode', mode))

    if windowState is not None:
        nvlist.append(('wsrp-windowState', windowState))

    if fragmentID is not None:
        nvlist.append(('wsrp-fragmentID', fragmentID))

    if secureURL is not None:
        nvlist.append(('wsrp-secureURL', secureURL))

    if resourceURL is not None:
        nvlist.append(('wsrp-resourceURL', resourceURL))

    if resourceRequiresRewrite is not None:
        nvlist.append(('wsrp-resourceRequiresRewrite',
                       resourceRequiresRewrite))

    return 'wsrp_rewrite?%s/wsrp_rewrite' % urlencode(nvlist)
