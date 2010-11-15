from suds.client import Client

if __name__ == '__main__':
    client = Client('http://localhost:7789/?wsdl')
    sd =  client.service.getServiceDescription(None, [])
    print 'Service Description'
    print '==================='
    print 'Requires registration:', sd.requiresRegistration
    print 'Requires init cookie:', sd.requiresInitCookie
    print 'Locales:', ', '.join(sd.locales[0])
    for portlet in sd.offeredPortlets[0]:
        print
        print 'Portlet'
        print '-------'
        print 'Handle:', portlet.portletHandle
        print 'Title:', portlet.title.value
