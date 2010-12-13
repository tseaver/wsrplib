# package API exports

from wsrplib._namespaces import WSRP_TYPES_NAMESPACE
from wsrplib._namespaces import WSRP_INTF_NAMESPACE

#from wsrplib._datatypes import Extension
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
from wsrplib._datatypes import RegistrationData
from wsrplib._datatypes import DestroyFailed
from wsrplib._datatypes import DestroyPortletsResponse
from wsrplib._datatypes import PortletDescriptionResponse
from wsrplib._datatypes import PortletPropertyDescriptionResponse

from wsrplib._faults import AccessDenied
from wsrplib._faults import InvalidUserCategory
from wsrplib._faults import InconsistentParameters
from wsrplib._faults import InvalidRegistration
from wsrplib._faults import MissingParameters
from wsrplib._faults import OperationFailed
from wsrplib._faults import InvalidHandle
from wsrplib._faults import PortletStateChangeRequired
from wsrplib._faults import InvalidCookie
from wsrplib._faults import InvalidSession
from wsrplib._faults import UnsupportedMode
from wsrplib._faults import UnsupportedWindowState
from wsrplib._faults import UnsupportedLocale
from wsrplib._faults import UnsupportedMimeType

from wsrplib._service_description import WSRP_v1_ServiceDescription
from wsrplib._markup import WSRP_v1_Markup
from wsrplib._registration import WSRP_v1_Registration
from wsrplib._portlet_management import WSRP_v1_PortletManagement



