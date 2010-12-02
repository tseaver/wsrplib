import sys
from suds.client import Client

def _maybeEmpty(attr):
    if attr is None:
        return ()
    return attr[0]

def main():
    url = 'http://localhost:7789/?wsdl'
    if len(sys.argv) > 1:
        url = sys.argv[1]
    client = Client(url, cache=None)
    sd =  client.service.getServiceDescription(None, [])

    print '###################'
    print 'Service Description'
    print '###################'
    print 'Requires registration:', sd.requiresRegistration
    print 'Requires init cookie:', sd.requiresInitCookie
    print 'Locales:', ', '.join(_maybeEmpty(sd.locales))

    for portlet in _maybeEmpty(sd.offeredPortlets):
        print
        print ' Portlet'
        print ' ======='
        print ' Handle:', portlet.portletHandle
        print ' Group ID:', portlet.groupID
        print ' Title:', portlet.title.value
        print ' Short title:', portlet.shortTitle.value
        print ' Display name:', portlet.displayName.value
        print ' Dscription:', portlet.description.value
        print ' Keywords:', ', '.join([
                                x.value for x in _maybeEmpty(portlet.keywords)])
        print ' User categories:', ', '.join(
                                _maybeEmpty(portlet.userCategories))
        print ' User profile items:', ', '.join(
                                _maybeEmpty(portlet.userProfileItems))
        print ' Uses GET method?', portlet.usesMethodGet
        print ' Default markup secure?', portlet.defaultMarkupSecure
        print ' All markup secure?', portlet.onlySecure
        print ' User ctx in session?', portlet.userContextStoredInSession
        print ' Templates in session?', portlet.templatesStoredInSession
        print ' User-specific state?', portlet.hasUserSpecificState
        print ' URL Template processing?', portlet.doesUrlTemplateProcessing

        for markupType in _maybeEmpty(portlet.markupTypes):
            print
            print '  Markup Type'
            print '  -----------'
            print '  MIME type:', markupType.mimeType
            print '  Modes:', ', '.join(_maybeEmpty(markupType.modes))
            print '  Window States:', ', '.join(
                                    _maybeEmpty(markupType.windowStates))
            print '  Locales:', ', '.join(_maybeEmpty(markupType.locales))

        p_context = {'portletHandle': portlet.portletHandle}
        response = client.service.getMarkup(None, p_context, None, None, None)
        m_context = response.markupContext

        print
        print '  getMarkup'
        print '  ---------'
        print '  Use Cached?', m_context.useCachedMarkup
        print '  MIME Type:', m_context.mimeType
        print '  Markup:'
        for line in response.markupContext.markupString.splitlines():
            print '     ', line
        print '  Locale:', m_context.locale
        print '  Requires URL Rewriting?', m_context.requiresUrlRewriting
        print '  Cache control:', m_context.cacheControl
        print '  Preferred Title:', m_context.preferredTitle

if __name__ == '__main__':
    main()
