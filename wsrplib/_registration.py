from soaplib.service import DefinitionBase
from soaplib.service import rpc

from wsrplib._datatypes import RegistrationContext
from wsrplib._datatypes import RegistrationData
from wsrplib._datatypes import RegistrationState
from wsrplib._namespaces import WSRP_INTF_NAMESPACE


class RegistrationAPI(DefinitionBase):
    __namespace__ = WSRP_INTF_NAMESPACE

    @rpc(RegistrationData,
         _returns=RegistrationContext,
        )
    def register(self,
        registration_data,
        ):
        # See WSRP 1.0 spec. 7.2
        pass

    @rpc(RegistrationContext,
         RegistrationData,
         _returns=RegistrationState,
        )
    def modifyRegistration(self,
        registration_context,
        registration_data,
        ):
        # See WSRP 1.0 spec. 7.3
        pass

    @rpc(RegistrationContext,
        )
    def deregister(self,
        registration_context,
        ):
        # See WSRP 1.0 spec. 7.4
        pass
