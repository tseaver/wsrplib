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
from wsrplib._namespaces import WSRP_INTF_NAMESPACE


class PortletManagementAPI(DefinitionBase):
    __namespace__ = WSRP_INTF_NAMESPACE

    @rpc(RegistrationContext,
         PortletContext,
         UserContext,
         desiredLocales,
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
