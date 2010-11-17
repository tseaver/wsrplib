from zope.interface import implements

from wsrplib.interfaces import IMarkupType
from wsrplib.interfaces import IPortlet
from wsrplib.interfaces import IServiceDescriptionInfo
from wsrplib._service_description import ServiceDescriptionAPI
from wsrplib._markup import MarkupAPI
#from wsrplib import RegistrationAPI
#from wsrplib import PortletManagementAPI

class DummyMarkupType(object):
    implements(IMarkupType)
    mimeType = 'text/html'
    modes = ('view',)
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

class DummyServiceDescriptionInfo(object):
    implements(IServiceDescriptionInfo)
    requiresRegistration = False
    requiresInitCookie = 'none'
    locales = ['en-US']

if __name__=='__main__':
    from zope.component import provideUtility
    import soaplib
    from soaplib.server import wsgi
    from wsgiref.simple_server import make_server
    provideUtility(DummyServiceDescriptionInfo(), IServiceDescriptionInfo)
    provideUtility(DummyPortlet(), IPortlet, name='dummy')
    soap_application = soaplib.Application(
                            [ServiceDescriptionAPI,
                             MarkupAPI,
                             #RegistrationAPI,
                             #PortletManagementAPI,
                            ], None)
    wsgi_application = wsgi.Application(soap_application)
    server = make_server('localhost', 7789, wsgi_application)

    print "listening to http://0.0.0.0:7789"
    print "wsdl is at: http://127.0.0.1:7789/?wsdl"
    server.serve_forever()
