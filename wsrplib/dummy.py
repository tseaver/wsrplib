from zope.interface import implements

from wsrplib.datatypes import MarkupContext
from wsrplib.datatypes import MarkupResponse
from wsrplib.interfaces import IMarkupType
from wsrplib.interfaces import IPortlet
from wsrplib.interfaces import IServiceDescriptionInfo

class DummyMarkupType(object):
    implements(IMarkupType)
    mimeType = 'text/plain'
    modes = ('wsrp:view',)
    windowStates = ('wsrp:normal',)
    locales = ('en',)

class DummyPortlet(object):
    implements(IPortlet)
    markupTypes = (DummyMarkupType(),)
    groupID = 'Dummy Group'
    title = shortTitle = displayName = 'Dummy Portlet'
    description = 'Portlet registered to test portlet definition exchange.'
    keywords = ('dummy', 'testing')
    userCategories = userProfileItems = ()
    usesMethodGet = False
    defaultMarkupSecure = False
    onlySecure = False
    userContextStoredInSession = False
    templatesStoredInSession = False
    hasUserSpecificState = False
    doesUrlTemplateProcessing = False

    def GET(self, request_environ,
            registration_context, portlet_context, runtime_context,
            user_context, markup_params):
        """ See IPortlet.
        """
        response = MarkupResponse()
        payload = response.markupContext = MarkupContext()
        payload.useCachedMarkup = False
        payload.mimeType = 'text/plain'
        payload.markupString = 'Hello, world!'
        payload.locale = 'en'
        payload.requiresUrlRewriting = False
        payload.cacheControl = None
        payload.preferredTitle = 'Demo Portlet'
        return response

class DummyServiceDescriptionInfo(object):
    implements(IServiceDescriptionInfo)
    requiresRegistration = False
    requiresInitCookie = 'none'
    locales = ['en']

