from wsrplib import ServiceDescriptionAPI
from wsrplib import MarkupAPI
from wsrplib import RegistrationAPI
from wsrplib import PortletManagementAPI

#__namespace__ = 'http://schemas.xmlsoap.org/wsdl/'

class Producer(ServiceDescriptionAPI,
               MarkupAPI,
               RegistrationAPI,
               PortletManagementAPI,
              ):
    pass

if __name__=='__main__':
    from wsgiref.simple_server import make_server
    from soaplib.wsgi import Application
    app = Application([Producer], None)
    server = make_server('localhost', 7789, app)
    server.serve_forever()
