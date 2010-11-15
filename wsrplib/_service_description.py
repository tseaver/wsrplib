from soaplib.service import DefinitionBase
from soaplib.service import rpc

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
        # Dummy implementation for testing.
        pd = PortletDescription()
        pd.portletHandle = '0001'
        pd.title = _localized('title', 'Some Portlet')
        result = ServiceDescription()
        result.requiresRegistration = False
        result.requiresInitCookie = 'none'
        result.locales = ['en-US']
        result.offeredPortlets = [pd]
        return result
