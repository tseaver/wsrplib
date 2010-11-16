from suds.client import Client

if __name__ == '__main__':
    client = Client('http://localhost:7789/?wsdl')
    client.set_options(cache=None)
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
        print 'Short title:', portlet.shortTitle.value
        print 'Display name:', portlet.displayName.value
        print 'Dscription:', portlet.description.value
        print 'Keywords:', ', '.join([x.value for x in portlet.keywords[0]])
