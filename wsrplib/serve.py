from wsrplib import ServiceDescriptionAPI
#from wsrplib import MarkupAPI
#from wsrplib import RegistrationAPI
#from wsrplib import PortletManagementAPI



if __name__=='__main__':
    from wsgiref.simple_server import make_server
    import soaplib
    from soaplib.server import wsgi
    soap_application = soaplib.Application([ServiceDescriptionAPI], None)
    wsgi_application = wsgi.Application(soap_application)
    server = make_server('localhost', 7789, wsgi_application)

    print "listening to http://0.0.0.0:7789"
    print "wsdl is at: http://127.0.0.1:7789/?wsdl"
    server.serve_forever()
