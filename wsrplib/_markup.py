from soaplib.service import DefinitionBase
from soaplib.service import rpc

from wsrplib._datatypes import BlockingInteractionResponse
from wsrplib._datatypes import MarkupParams
from wsrplib._datatypes import MarkupResponse
from wsrplib._datatypes import PortletContext
from wsrplib._datatypes import RegistrationContext
from wsrplib._datatypes import RuntimeContext
from wsrplib._datatypes import UserContext
from wsrplib._datatypes import sessionIDs
from wsrplib._namespaces import WSRP_INTF_NAMESPACE

class MarkupAPI(DefinitionBase):
    __namespace__ = WSRP_INTF_NAMESPACE

    @rpc(RegistrationContext,
         PortletContext,
         RuntimeContext,
         UserContext,
         MarkupParams,
         _returns=MarkupResponse)
    def getMarkup(self,
        registration_context,
        portlet_context,
        runtime_context,
        user_context,
        markup_params,
        ):
        # See WSRP 1.0 spec. 6.2
        pass

    @rpc(RegistrationContext,
         PortletContext,
         RuntimeContext,
         UserContext,
         MarkupParams,
         _returns=BlockingInteractionResponse,
        )
    def performBlockingInteraction(self,
        registration_context,
        portlet_context,
        runtime_context,
        user_context,
        markup_params,
        interaction_params,
        ):
        # See WSRP 1.0 spec. 6.3
        pass

    @rpc(RegistrationContext,
        )
    def initCookie(self,
        registration_context,
        ):
        # See WSRP 1.0 spec. 6.4
        pass

    @rpc(RegistrationContext,
         sessionIDs,
        )
    def releaseSessions(self,
        registration_context,
        session_ids,
        ):
        # See WSRP 1.0 spec. 6.4
        pass
