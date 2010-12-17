from soaplib.service import DefinitionBase
from soaplib.service import document

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


class WSRP_v1_PortletManagement(DefinitionBase):
    __namespace__ = WSRP_TYPES_NAMESPACE

    @classmethod
    def get_tns(cls):
        # Override to get our messages in the right namespace
        return cls.__namespace__

    @document(RegistrationContext,
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

    @document(RegistrationContext,
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
        registrationContext,
        portletContext,
        userContext,
        ):
        """ See WSRP 1.0 spec. 8.3
        """
        pass

    @document(RegistrationContext,
              StringSeq,
              _faults=[InconsistentParameters,
                       InvalidRegistration,
                       MissingParameters,
                       OperationFailed,
                      ],
              _returns=DestroyPortletsResponse,
              )
    def destroyPortlets(self,
        registrationContext,
        portletHandles,
        ):
        """ See WSRP 1.0 spec. 8.4
        """
        pass

    @document(RegistrationContext,
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
        registrationContext,
        portletContext,
        userContext,
        propertyList,
        ):
        """ See WSRP 1.0 spec. 8.5
        """
        pass

    @document(RegistrationContext,
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

    @document(RegistrationContext,
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