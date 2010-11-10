from wsrplib import ServiceDescriptionAPI
from wsrplib import MarkupAPI
from wsrplib import RegistrationAPI
from wsrplib import PortletManagementAPI

APIS = [
    ServiceDescriptionAPI,
    MarkupAPI,
    RegistrationAPI,
    PortletManagementAPI,
]

if __name__=='__main__':
    from wsgiref.simple_server import make_server
    from soaplib.wsgi import Application
    app = Application([ServiceDescriptionAPI], 'tns')
    server = make_server('localhost', 7789, app)
    server.serve_forever()
