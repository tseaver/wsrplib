from soaplib.core.service import DefinitionBase
from soaplib.core.service import soap
from soaplib.core.styles import DOC_STYLE

from wsrplib.datatypes import DestroyPortletsResponse
from wsrplib.datatypes import PortletContext
from wsrplib.datatypes import PortletDescriptionResponse
from wsrplib.datatypes import PortletPropertyDescriptionResponse
from wsrplib.datatypes import PropertyList
from wsrplib.datatypes import RegistrationContext
from wsrplib.datatypes import StringSeq
from wsrplib.datatypes import UserContext
from wsrplib.faults import AccessDenied
from wsrplib.faults import InconsistentParameters
from wsrplib.faults import InvalidHandle
from wsrplib.faults import InvalidRegistration
from wsrplib.faults import InvalidUserCategory
from wsrplib.faults import MissingParameters
from wsrplib.faults import OperationFailed
from wsrplib.namespaces import WSRP_TYPES_NAMESPACE

PORT_TYPE = 'WSRP_v1_PortletManagement_PortType'

class WSRP_v1_PortletManagement(DefinitionBase):
    __namespace__ = WSRP_TYPES_NAMESPACE
    __port_types__ = (PORT_TYPE,)

    @classmethod
    def get_tns(cls):
        # Override to get our messages in the right namespace
        return cls.__namespace__

    @soap(RegistrationContext,
          PortletContext,
          UserContext,
          StringSeq,
          _faults=[AccessDenied,
                   InconsistentParameters,
                   InvalidHandle,
                   InvalidRegistration,
                   InvalidUserCategory,
                   MissingParameters,
                   OperationFailed,
                  ],
          _returns=PortletDescriptionResponse,
          _style=DOC_STYLE,
          _port_type=PORT_TYPE,
         )
    def getPortletDescription(self,
        registrationContext,
        portletContext,
        userContext,
        desiredLocales,
        ):
        """ See WSRP 1.0 spec. 8.2
        """
        pass

    @soap(RegistrationContext,
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
          _style=DOC_STYLE,
          _port_type=PORT_TYPE,
         )
    def clonePortlet(self,
        registrationContext,
        portletContext,
        userContext,
        ):
        """ See WSRP 1.0 spec. 8.3
        """
        pass

    @soap(RegistrationContext,
          StringSeq,
          _faults=[InconsistentParameters,
                   InvalidRegistration,
                   MissingParameters,
                   OperationFailed,
                  ],
          _returns=DestroyPortletsResponse,
          _style=DOC_STYLE,
          _port_type=PORT_TYPE,
         )
    def destroyPortlets(self,
        registrationContext,
        portletHandles,
        ):
        """ See WSRP 1.0 spec. 8.4
        """
        pass

    @soap(RegistrationContext,
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
          _style=DOC_STYLE,
          _port_type=PORT_TYPE,
         )
    def setPortletProperties(self,
        registrationContext,
        portletContext,
        userContext,
        propertyList,
        ):
        """ See WSRP 1.0 spec. 8.5
        """
        pass

    @soap(RegistrationContext,
          PortletContext,
          UserContext,
          StringSeq,
          _faults=[AccessDenied,
                   InconsistentParameters,
                   InvalidHandle,
                   InvalidRegistration,
                   InvalidUserCategory,
                   MissingParameters,
                   OperationFailed,
                  ],
          _returns=PropertyList,
          _style=DOC_STYLE,
          _port_type=PORT_TYPE,
         )
    def getPortletProperties(self,
        registrationContext,
        portletContext,
        userContext,
        nameList,
        ):
        """ See WSRP 1.0 spec. 8.6
        """
        pass

    @soap(RegistrationContext,
          PortletContext,
          UserContext,
          StringSeq,
          _faults=[AccessDenied,
                   InconsistentParameters,
                   InvalidHandle,
                   InvalidRegistration,
                   InvalidUserCategory,
                   MissingParameters,
                   OperationFailed,
                  ],
          _returns=PortletPropertyDescriptionResponse,
          _style=DOC_STYLE,
          _port_type=PORT_TYPE,
         )
    def getPortletPropertyDescription(self,
        registrationContext,
        portletContext,
        userContext,
        desiredLocales,
        ):
        """ See WSRP 1.0 spec. 8.7
        """
        pass
