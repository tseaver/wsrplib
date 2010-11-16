from suds.client import Client

def _maybeEmpty(attr):
    if attr is None:
        return ()
    return attr[0]

if __name__ == '__main__':
    client = Client('http://localhost:7789/?wsdl')
    client.set_options(cache=None)
    sd =  client.service.getServiceDescription(None, [])
    print 'Service Description'
    print '==================='
    print 'Requires registration:', sd.requiresRegistration
    print 'Requires init cookie:', sd.requiresInitCookie
    print 'Locales:', ', '.join(_maybeEmpty(sd.locales))
    for portlet in sd.offeredPortlets[0]:
        print
        print 'Portlet'
        print '-------'
        print 'Handle:', portlet.portletHandle
        print 'Group ID:', portlet.groupID
        print 'Title:', portlet.title.value
        print 'Short title:', portlet.shortTitle.value
        print 'Display name:', portlet.displayName.value
        print 'Dscription:', portlet.description.value
        print 'Keywords:', ', '.join([
                                x.value for x in _maybeEmpty(portlet.keywords)])
        print 'User categories:', ', '.join(_maybeEmpty(portlet.userCategories))
        print 'User profile items:', ', '.join(
                                _maybeEmpty(portlet.userProfileItems))
        print 'Uses GET method?', portlet.usesMethodGet
        print 'Default markup secure?', portlet.defaultMarkupSecure
        print 'All markup secure?', portlet.onlySecure
        print 'User ctx in session?', portlet.userContextStoredInSession
        print 'Templates in session?', portlet.templatesStoredInSession
        print 'User-specific state?', portlet.hasUserSpecificState
        print 'URL Template processing?', portlet.doesUrlTemplateProcessing
