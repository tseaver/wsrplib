from zope.interface import Attribute
from zope.interface import Interface

class IServiceDescriptionInfo(Interface):
    requiresRegistration = Attribute(u"Does the service require registration?")
    requiresInitCookie = Attribute(u"Does the service require that "
                                    "'initCookie' be called?")
    locales = Attribute(u"List of locales supported by the service.")


class IMarkupType(Interface):
    """ Define how portlet can be queried for markup.
    """
    mimeType = Attribute(u'MIME type of portlet markup')
    modes = Attribute(u'List of supported mode names')
    windowStates = Attribute(u'List of supported window state names')
    locales = Attribute(u'List of supported locale names')


class IPortlet(Interface):
    """ Utility interface:  portlets are registered as named utilities.
    """
    groupID = Attribute(u'Portlet group identifier')
    title = Attribute(u'Portlet title')
    displayName = Attribute(u'Portlet title')
    shortTitle = Attribute(u'Shorter portlet title')
    description = Attribute(u'Portlet description')
    keywords = Attribute(u'Keywords for the portlet')
    markupTypes = Attribute(u'List of supported IMarkupTypes')
    userCategories = Attribute(u'List of supported user category names')
    userProfileItems = Attribute(u'List of expected user profile properties')
    usesMethodGet = Attribute(u'Does the portlet use GET method for forms?')
    defaultMarkupSecure = Attribute(u'Does the portlet require secure '
                                    u'communication for its default markup?')
    onlySecure = Attribute(u'Does the portlet require secure '
                           u'communication for all its markup?')
    userContextStoredInSession = Attribute(u'Does the portlet store profile '
                                           u'information in the session?')
    templatesStoredInSession = Attribute(u'Does the portlet store provided '
                                         u'templates in the session?')
    hasUserSpecificState = Attribute(u'Does the portlet store persistent, '
                                     u'user-specific state?')
    doesUrlTemplateProcessing = Attribute(u'Does the portlet do its own '
                                          u'URL processing of templates?')

    def GET(registration_context,
            portlet_context,
            runtime_context,
            user_context,
            markup_params,
           ):
        """ Return a MarkupResponse.
        """
