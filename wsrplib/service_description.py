from soaplib.service import DefinitionBase
from soaplib.service import document
from zope.component import getUtilitiesFor
from zope.component import getUtility

from wsrplib.interfaces import IPortlet
from wsrplib.interfaces import IServiceDescriptionInfo
from wsrplib.datatypes import LocalizedString
from wsrplib.datatypes import MarkupType
from wsrplib.datatypes import ModelDescription
from wsrplib.datatypes import ModelTypes
from wsrplib.datatypes import PortletDescription
from wsrplib.datatypes import RegistrationContext
from wsrplib.datatypes import ServiceDescription
from wsrplib.datatypes import StringSeq
from wsrplib.faults import InvalidRegistration
from wsrplib.faults import OperationFailed
from wsrplib.namespaces import WSRP_TYPES_NAMESPACE


def _localized(name, value):
    ls = LocalizedString()
    ls.xmlLang = 'en'
    ls.value = value
    ls.resourceName = name
    return ls

class WSRP_v1_ServiceDescription(DefinitionBase):
    __namespace__ = WSRP_TYPES_NAMESPACE

    @classmethod
    def get_tns(cls):
        # Override to get our messages in the right namespace
        return cls.__namespace__

    @document(RegistrationContext,
              StringSeq,
              _faults=[InvalidRegistration,
                       OperationFailed,
                      ],
              _returns=ServiceDescription,
             )
    def getServiceDescription(self,
        registrationContext,
        desiredLocales,
        ):
        """ See WSRP 1.0 spec. 5.2
        """
        result = ServiceDescription()
        info = getUtility(IServiceDescriptionInfo)
        result.requiresRegistration = info.requiresRegistration
        result.userCategoryDescriptions = []            # XXX
        result.customUserProfileItemDescriptions = []   # XXX
        result.customWindowStateDescriptions = []       # XXX
        result.customModeDescriptions = []              # XXX
        result.requiresInitCookie = info.requiresInitCookie
        regProps = ModelDescription()
        regProps.propertyDescriptions = []
        modelTypes = ModelTypes()
        modelTypes.any = []
        regProps.modelTypes = modelTypes
        result.registrationPropertyDescription = regProps
        result.locales = list(info.locales)
        result.resourceList = []                        # XXX
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
