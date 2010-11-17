from soaplib.service import DefinitionBase
from soaplib.service import rpc
from zope.component import getUtilitiesFor
from zope.component import getUtility

from wsrplib.interfaces import IPortlet
from wsrplib.interfaces import IServiceDescriptionInfo
from wsrplib._datatypes import LocalizedString
from wsrplib._datatypes import MarkupType
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
        info = getUtility(IServiceDescriptionInfo)
        result.requiresRegistration = info.requiresRegistration
        result.requiresInitCookie = info.requiresInitCookie
        result.locales = list(info.locales)
        result.offeredPortlets = portlets = []
        for name, portlet in getUtilitiesFor(IPortlet):
            pd = PortletDescription()
            pd.portletHandle = name
            pd.groupID = portlet.groupID
            pd.title = _localized('title', portlet.title)
            pd.shortTitle = _localized('shortTitle', portlet.shortTitle)
            pd.displayName = _localized('displayName', portlet.displayName)
            pd.description = _localized('description', portlet.description)
            pd.keywords = [_localized('keyword', x) for x in portlet.keywords]
            m_types = pd.markupTypes = []
            for m_type in portlet.markupTypes:
                mt = MarkupType()
                mt.mimeType = m_type.mimeType
                mt.modes = list(m_type.modes)
                mt.windowStates = list(m_type.windowStates)
                mt.locales = list(m_type.locales)
                m_types.append(mt)
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
        return result
