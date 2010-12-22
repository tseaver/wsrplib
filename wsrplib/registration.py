from soaplib.service import DefinitionBase
from soaplib import DOC_STYLE
from soaplib.service import soap

from wsrplib.datatypes import RegistrationContext
from wsrplib.datatypes import RegistrationData
from wsrplib.datatypes import RegistrationState
from wsrplib.faults import InvalidRegistration
from wsrplib.faults import MissingParameters
from wsrplib.faults import OperationFailed
from wsrplib.namespaces import WSRP_TYPES_NAMESPACE

SERVICE_INTERFACE = 'WSRP_v1_Registration'
PORT_TYPE = '%s_PortType' % SERVICE_INTERFACE

class WSRP_v1_Registration(DefinitionBase):
    __namespace__ = WSRP_TYPES_NAMESPACE
    __service_interface__ = SERVICE_INTERFACE
    __port_types__ = (PORT_TYPE,)

    @classmethod
    def get_tns(cls):
        # Override to get our messages in the right namespace
        return cls.__namespace__

    @soap(RegistrationData,
          _faults=[MissingParameters,
                   OperationFailed,
                  ],
          _returns=RegistrationContext,
          _style=DOC_STYLE,
          _port_type=PORT_TYPE,
         )
    def register(self,
        registrationData,
        ):
        """ See WSRP 1.0 spec. 7.2
        """
        pass

    @soap(RegistrationContext,
          RegistrationData,
          _faults=[InvalidRegistration,
                   MissingParameters,
                   OperationFailed,
                  ],
          _returns=RegistrationState,
          _style=DOC_STYLE,
          _port_type=PORT_TYPE,
         )
    def modifyRegistration(self,
        registrationContext,
        registrationData,
        ):
        """ See WSRP 1.0 spec. 7.3
        """
        pass

    @soap(RegistrationContext,
          _faults=[InvalidRegistration,
                   OperationFailed,
                  ],
          _style=DOC_STYLE,
          _port_type=PORT_TYPE,
         )
    def deregister(self,
        registrationContext,
        ):
        """ See WSRP 1.0 spec. 7.4
        """
        pass
