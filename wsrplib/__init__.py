# package

from soaplib.service import DefinitionBase
from soaplib.service import rpc

# Utility type
from wsrplib._datatypes import QName

from wsrplib._datatypes import Extension
from wsrplib._datatypes import Handle
from wsrplib._datatypes import Key
from wsrplib._datatypes import ID
from wsrplib._datatypes import LocalizedString
from wsrplib._datatypes import ResourceValue
from wsrplib._datatypes import Resource
from wsrplib._datatypes import ResourceList
from wsrplib._datatypes import ItemDescription
from wsrplib._datatypes import MarkupType
from wsrplib._datatypes import PortletDescription
from wsrplib._datatypes import Property
from wsrplib._datatypes import ResetProperty
from wsrplib._datatypes import PropertyList
from wsrplib._datatypes import PropertyDescription
from wsrplib._datatypes import ModelTypes
from wsrplib._datatypes import ModelDescription
from wsrplib._datatypes import CookieProtocol
from wsrplib._datatypes import ServiceDescription
from wsrplib._datatypes import RegistrationState
from wsrplib._datatypes import RegistrationContext
from wsrplib._datatypes import desiredLocales
from wsrplib._datatypes import SessionContext
from wsrplib._datatypes import Templates
from wsrplib._datatypes import RuntimeContext
from wsrplib._datatypes import PortletContext
from wsrplib._datatypes import CacheControl
from wsrplib._datatypes import ClientData
from wsrplib._datatypes import NamedString
from wsrplib._datatypes import MarkupParams
from wsrplib._datatypes import MarkupContext
from wsrplib._datatypes import MarkupResponse
from wsrplib._datatypes import UpdateResponse
from wsrplib._datatypes import BlockingInteractionResponse
from wsrplib._datatypes import StateChange
from wsrplib._datatypes import UploadContext
from wsrplib._datatypes import InteractionParams
from wsrplib._datatypes import PersonName
from wsrplib._datatypes import EmployerInfo
from wsrplib._datatypes import TelephoneNum
from wsrplib._datatypes import Telecom
from wsrplib._datatypes import Online
from wsrplib._datatypes import Postal
from wsrplib._datatypes import Contact
from wsrplib._datatypes import UserProfile
from wsrplib._datatypes import UserContext
from wsrplib._datatypes import sessionIDs
from wsrplib._datatypes import RegistrationData


class ServiceDescriptionAPI(DefinitionBase):

    @rpc(RegistrationContext,
         desiredLocales,
         _returns=ServiceDescription)
    def getServiceDescription(self,
        registration_context,
        desired_locales,
        ):
        # See WSRP 1.0 spec. 5.2
        pass


class MarkupAPI(DefinitionBase):

    @rpc(RegistrationContext,
         PortletContext,
         RuntimeContext,
         UserContext,
         MarkupParams,
         _returns=ServiceDescription)
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
         _returns=ServiceDescription,
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


class RegistrationAPI(DefinitionBase):

    @rpc(RegistrationData,
         _returns=RegistrationContext,
        )
    def register(self,
        registration_data,
        ):
        pass

    @rpc(RegistrationContext,
         RegistrationData,
         _returns=RegistrationState,
        )
    def modifyRegistration(self,
        registration_context,
        registration_data,
        ):
        pass

    @rpc(RegistrationContext,
        )
    def deregister(self,
        registration_context,
        ):
        pass
