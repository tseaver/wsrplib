# package API exports

from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
from wsrplib.namespaces import WSRP_INTF_NAMESPACE

#from wsrplib.datatypes import Extension
from wsrplib.datatypes import Handle
from wsrplib.datatypes import Key
from wsrplib.datatypes import ID
from wsrplib.datatypes import LocalizedString
from wsrplib.datatypes import ResourceValue
from wsrplib.datatypes import Resource
from wsrplib.datatypes import ResourceList
from wsrplib.datatypes import ItemDescription
from wsrplib.datatypes import MarkupType
from wsrplib.datatypes import PortletDescription
from wsrplib.datatypes import Property
from wsrplib.datatypes import ResetProperty
from wsrplib.datatypes import PropertyList
from wsrplib.datatypes import PropertyDescription
from wsrplib.datatypes import ModelTypes
from wsrplib.datatypes import ModelDescription
from wsrplib.datatypes import CookieProtocol
from wsrplib.datatypes import ServiceDescription
from wsrplib.datatypes import RegistrationState
from wsrplib.datatypes import RegistrationContext
from wsrplib.datatypes import SessionContext
from wsrplib.datatypes import Templates
from wsrplib.datatypes import RuntimeContext
from wsrplib.datatypes import PortletContext
from wsrplib.datatypes import CacheControl
from wsrplib.datatypes import ClientData
from wsrplib.datatypes import NamedString
from wsrplib.datatypes import MarkupParams
from wsrplib.datatypes import MarkupContext
from wsrplib.datatypes import MarkupResponse
from wsrplib.datatypes import UpdateResponse
from wsrplib.datatypes import BlockingInteractionResponse
from wsrplib.datatypes import StateChange
from wsrplib.datatypes import UploadContext
from wsrplib.datatypes import InteractionParams
from wsrplib.datatypes import PersonName
from wsrplib.datatypes import EmployerInfo
from wsrplib.datatypes import TelephoneNum
from wsrplib.datatypes import Telecom
from wsrplib.datatypes import Online
from wsrplib.datatypes import Postal
from wsrplib.datatypes import Contact
from wsrplib.datatypes import UserProfile
from wsrplib.datatypes import UserContext
from wsrplib.datatypes import RegistrationData
from wsrplib.datatypes import DestroyFailed
from wsrplib.datatypes import DestroyPortletsResponse
from wsrplib.datatypes import PortletDescriptionResponse
from wsrplib.datatypes import PortletPropertyDescriptionResponse

from wsrplib.faults import AccessDenied
from wsrplib.faults import InvalidUserCategory
from wsrplib.faults import InconsistentParameters
from wsrplib.faults import InvalidRegistration
from wsrplib.faults import MissingParameters
from wsrplib.faults import OperationFailed
from wsrplib.faults import InvalidHandle
from wsrplib.faults import PortletStateChangeRequired
from wsrplib.faults import InvalidCookie
from wsrplib.faults import InvalidSession
from wsrplib.faults import UnsupportedMode
from wsrplib.faults import UnsupportedWindowState
from wsrplib.faults import UnsupportedLocale
from wsrplib.faults import UnsupportedMimeType

from wsrplib.service_description import WSRP_v1_ServiceDescription
from wsrplib.markup import WSRP_v1_Markup
from wsrplib.registration import WSRP_v1_Registration
from wsrplib.portlet_management import WSRP_v1_PortletManagement



