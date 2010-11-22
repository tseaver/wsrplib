import os

from zope.interface import implements
from paste.urlmap import URLMap
from paste.urlparser import StaticURLParser

from wsrplib.interfaces import IMarkupType
from wsrplib.interfaces import IPortlet
from wsrplib.interfaces import IServiceDescriptionInfo
from wsrplib._datatypes import MarkupContext
from wsrplib._markup import MarkupAPI
from wsrplib._service_description import ServiceDescriptionAPI
#from wsrplib import RegistrationAPI
#from wsrplib import PortletManagementAPI

class DummyMarkupType(object):
    implements(IMarkupType)
    mimeType = 'text/plain'
    modes = ()
    windowStates = ()
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
    def GET(self, registration_context, portlet_context, runtime_context,
            user_context, markup_params):
        """ See IPortlet.
        """
        response = MarkupContext()
        response.useCachedMarkup = False
        response.mimeType = 'text/plain'
        response.markupString = 'Hello, world!'
        response.locale = 'en'
        response.requiresUrlRewriting = False
        response.cacheControl = None
        response.preferredTitle = 'Demo Portlet'
        return response

class DummyServiceDescriptionInfo(object):
    implements(IServiceDescriptionInfo)
    requiresRegistration = False
    requiresInitCookie = 'none'
    locales = ['en-US']

if __name__=='__main__':
    import logging
    from wsgiref.simple_server import make_server
    from zope.component import provideUtility
    from soaplib.server import wsgi
    from wsrplib._application import Application
    from wsrplib._namespaces import WSRP_TYPES_NAMESPACE
    logging.basicConfig(level=logging.DEBUG)
    provideUtility(DummyServiceDescriptionInfo(), IServiceDescriptionInfo)
    provideUtility(DummyPortlet(), IPortlet, name='dummy')
    soap_application = Application(
                            [ServiceDescriptionAPI,
                             MarkupAPI,
                             #RegistrationAPI,
                             #PortletManagementAPI,
                            ],
                            tns=WSRP_TYPES_NAMESPACE,
                            name='WSRP_v1_Service',
                           )
    wsgi_application = wsgi.Application(soap_application)
    urlmap = URLMap()
    here = os.path.split(__file__)[0]
    urlmap['/static/'] = StaticURLParser(os.path.join(here, 'static'))
    urlmap['/'] = wsgi_application
    server = make_server('localhost', 7789, urlmap)

    print "listening to http://0.0.0.0:7789"
    print "wsdl is at: http://127.0.0.1:7789/?wsdl"
    server.serve_forever()
