from soaplib.service import DefinitionBase
from soaplib.service import rpc

from wsrplib._datatypes import DestroyPortletsResponse
from wsrplib._datatypes import PortletContext
from wsrplib._datatypes import PortletDescriptionResponse
from wsrplib._datatypes import PortletPropertyDescriptionResponse
from wsrplib._datatypes import PropertyList
from wsrplib._datatypes import RegistrationContext
from wsrplib._datatypes import UserContext
from wsrplib._datatypes import desiredLocales
from wsrplib._datatypes import handleList
from wsrplib._datatypes import nameList
from wsrplib._faults import AccessDenied
from wsrplib._faults import InconsistentParameters
from wsrplib._faults import InvalidHandle
from wsrplib._faults import InvalidRegistration
from wsrplib._faults import InvalidUserCategory
from wsrplib._faults import MissingParameters
from wsrplib._faults import OperationFailed
from wsrplib._namespaces import WSRP_INTF_NAMESPACE


class WSRP_v1_PortletManagement(DefinitionBase):
    __namespace__ = WSRP_INTF_NAMESPACE

    @rpc(RegistrationContext,
         PortletContext,
         UserContext,
         desiredLocales,
         _faults=[AccessDenied,
                  InconsistentParameters,
                  InvalidHandle,
                  InvalidRegistration,
                  InvalidUserCategory,
                  MissingParameters,
                  OperationFailed,
                 ],
         _returns=PortletDescriptionResponse,
        )
    def getPortletDescription(self,
        registration_context,
        portlet_context,
        user_context,
        desired_locales,
        ):
        # See WSRP 1.0 spec. 8.2
        pass

    @rpc(RegistrationContext,
         PortletContext,
         UserContext,
         _faults=[AccessDenied,
                  InconsistentParameters,
                  InvalidHandle,
                  InvalidRegistration,
                  InvalidUserCategory,
                  MissingParameters,
                  OperationFailed,
                 ],
         _returns=PortletContext,
        )
    def clonePortlet(self,
        registration_context,
        portlet_context,
        user_context,
        ):
        # See WSRP 1.0 spec. 8.3
        pass

    @rpc(RegistrationContext,
         handleList,
         _faults=[InconsistentParameters,
                  InvalidRegistration,
                  MissingParameters,
                  OperationFailed,
                 ],
         _returns=DestroyPortletsResponse,
        )
    def destroyPortlets(self,
        registration_context,
        portlet_handles,
        ):
        # See WSRP 1.0 spec. 8.4
        pass

    @rpc(RegistrationContext,
         PortletContext,
         UserContext,
         PropertyList,
         _faults=[AccessDenied,
                  InconsistentParameters,
                  InvalidHandle,
                  InvalidRegistration,
                  InvalidUserCategory,
                  MissingParameters,
                  OperationFailed,
                 ],
         _returns=PortletContext,
        )
    def setPortletProperties(self,
        registration_context,
        portlet_context,
        user_context,
        property_list,
        ):
        # See WSRP 1.0 spec. 8.5
        pass

    @rpc(RegistrationContext,
         PortletContext,
         UserContext,
         nameList,
         _faults=[AccessDenied,
                  InconsistentParameters,
                  InvalidHandle,
                  InvalidRegistration,
                  InvalidUserCategory,
                  MissingParameters,
                  OperationFailed,
                 ],
         _returns=PropertyList,
        )
    def getPortletProperties(self,
        registration_context,
        portlet_context,
        user_context,
        name_list,
        ):
        # See WSRP 1.0 spec. 8.6
        pass

    @rpc(RegistrationContext,
         PortletContext,
         UserContext,
         desiredLocales,
         _faults=[AccessDenied,
                  InconsistentParameters,
                  InvalidHandle,
                  InvalidRegistration,
                  InvalidUserCategory,
                  MissingParameters,
                  OperationFailed,
                 ],
         _returns=PortletPropertyDescriptionResponse,
        )
    def getPortletPropertyDsecription(self,
        registration_context,
        portlet_context,
        user_context,
        desired_locales,
        ):
        # See WSRP 1.0 spec. 8.7
        pass
