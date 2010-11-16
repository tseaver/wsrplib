from soaplib.service import DefinitionBase
from soaplib.service import rpc
from zope.component import getUtilitiesFor

from wsrplib.interfaces import IPortlet
from wsrplib._datatypes import LocalizedString
from wsrplib._datatypes import PortletDescription
from wsrplib._datatypes import RegistrationContext
from wsrplib._datatypes import ServiceDescription
from wsrplib._datatypes import desiredLocales
from wsrplib._namespaces import WSRP_INTF_NAMESPACE


def _localized(name, value):
    ls = LocalizedString()
    ls.xmlLang = 'en'
    ls.value = value
    ls.resourceName = name
    return ls

class ServiceDescriptionAPI(DefinitionBase):
    __namespace__ = WSRP_INTF_NAMESPACE

    @rpc(RegistrationContext,
         desiredLocales,
         _returns=ServiceDescription)
    def getServiceDescription(self,
        registration_context,
        desired_locales,
        ):
        # See WSRP 1.0 spec. 5.2
        result = ServiceDescription()
        result.requiresRegistration = False
        result.requiresInitCookie = 'none'
        result.locales = ['en-US']
        portlets = []
        for name, portlet in getUtilitiesFor(IPortlet):
            pd = PortletDescription()
            pd.portletHandle = name
            pd.groupID = portlet.groupID
            pd.title = _localized('title', portlet.title)
            pd.shortTitle = _localized('shortTitle', portlet.shortTitle)
            pd.displayName = _localized('displayName', portlet.displayName)
            pd.description = _localized('description', portlet.description)
            pd.keywords = [_localized('keyword', x) for x in portlet.keywords]
            pd.markupTypes = [] # XXX
            pd.userCategories = list(portlet.userCategories)
            pd.userProfileItems = list(portlet.userProfileItems)
            pd.usesMethodGet = portlet.usesMethodGet
            pd.defaultMarkupSecure = portlet.defaultMarkupSecure
            pd.onlySecure = portlet.onlySecure
            pd.userContextStoredInSession = portlet.userContextStoredInSession
            pd.templatesStoredInSession = portlet.templatesStoredInSession
            pd.hasUserSpecificState = portlet.hasUserSpecificState
            pd.doesUrlTemplateProcessing = portlet.doesUrlTemplateProcessing
            portlets.append(pd)
        result.offeredPortlets = portlets
        return result
