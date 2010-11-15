from soaplib.service import DefinitionBase
from soaplib.service import rpc

from wsrplib._datatypes import RegistrationContext
from wsrplib._datatypes import ServiceDescription
from wsrplib._datatypes import desiredLocales
from wsrplib._namespaces import WSRP_INTF_NAMESPACE


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
        return result
