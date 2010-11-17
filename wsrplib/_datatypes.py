# WSRP datatypes

from soaplib.model.binary import Attachment
from soaplib.model.enum import Enum
from soaplib.model.primitive import Any  # AnyAsDict?
from soaplib.model.primitive import AnyUri
from soaplib.model.primitive import Boolean
from soaplib.model.primitive import Date
from soaplib.model.primitive import Integer
from soaplib.model.primitive import SimpleType
from soaplib.model.primitive import String
from soaplib.model.primitive import Mandatory
from soaplib.model.clazz import Array
from soaplib.model.clazz import ClassSerializer

from wsrplib._namespaces import WSDL_NAMESPACE
from wsrplib._namespaces import WSRP_TYPES_NAMESPACE


class QName(AnyUri):
    __namespace__ = WSDL_NAMESPACE



class _WSRPSerializer(ClassSerializer):
    __namespace__ = WSRP_TYPES_NAMESPACE

class _WSRPString(String):
    __namespace__ = WSRP_TYPES_NAMESPACE
    __base_type__ = String


class Extension(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.1
    any = Any


class Handle(_WSRPString):
    # See WSRP 1.0 spec. 5.1.2
    __type_name__ = 'Handle'
    class Attributes(String.Attributes):
        min_len = 1
        max_len = 255


class Key(_WSRPString):
    # See WSRP 1.0 spec. 5.1.3
    __type_name__ = 'Key'
    class Attributes(String.Attributes):
        min_len = 1
        max_len = 255


class ID(_WSRPString):
    # See WSRP 1.0 spec. 5.1.4
    __type_name__ = 'ID'
    class Attributes(String.Attributes):
        min_len = 1
        max_len = 4096


##############################################################################
# ServiceDescription API
##############################################################################


class LocalizedString(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.5
    xmlLang = Mandatory.String
    value = Mandatory.String
    resourceName = String


class ResourceValue(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.6
    xmlLang = Mandatory.String
    value = Mandatory.String
    extensions = Array(Extension)


class Resource(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.7
    resourceName = Mandatory.String
    values = Array(ResourceValue)
    extensions = Array(Extension)


class ResourceList(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.8
    resources = Array(Resource)
    extensions = Array(Extension)


class ItemDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.9
    itemName = Mandatory.String
    description = LocalizedString
    extensions = Array(Extension)

class MarkupType(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.10
    mimeType = Mandatory.String
    modes = Array(String)
    windowStates = Array(String)
    locales = Array(String)
    extensions = Array(Extension)

class PortletDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.11
    portletHandle = Handle
    markupTypes = Array(MarkupType)
    groupID = ID
    description = LocalizedString
    shortTitle = LocalizedString
    title = LocalizedString
    displayName = LocalizedString
    keywords = Array(LocalizedString)
    userCategories = Array(String)
    userProfileItems = Array(String)
    usesMethodGet = Boolean
    defaultMarkupSecure = Boolean
    onlySecure = Boolean
    userContextStoredInSession = Boolean
    templatesStoredInSession = Boolean
    hasUserSpecificState = Boolean
    doesUrlTemplateProcessing = Boolean
    extensions = Array(Extension)


class Property(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.12
    name = Mandatory.String
    xmlLang = String
    value = Array(Any)


class ResetProperty(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.13
    name = Mandatory.String


class PropertyList(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.14
    properties = Array(Property)
    resetProperties = Array(ResetProperty)
    extensions = Array(Extension)


class PropertyDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.15
    name = Mandatory.String
    type = QName
    label = LocalizedString
    hint = LocalizedString
    extensions = Array(Extension)


class ModelTypes(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.16
    any = Array(Any)


class ModelDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.17
    propertyDescriptions = Array(PropertyDescription)
    modelTypes = ModelTypes
    extensions = Array(Extension)


# See WSRP 1.0 spec. 5.1.18
CookieProtocol = Enum('none', 'perUser', 'perGroup', type_name='String')
CookieProtocol__namespace__ = WSRP_TYPES_NAMESPACE



class ServiceDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.19
    requiresRegistration = Boolean
    offeredPortlets = Array(PortletDescription)
    userCategoryDescriptions = Array(ItemDescription)
    customUserProfileItemDescriptions = Array(ItemDescription)
    customWindowStateDescriptions = Array(ItemDescription)
    customModeDescriptions = Array(ItemDescription)
    requiresInitCookie = CookieProtocol
    registrationPropertyDescription = ModelDescription
    locales = Array(String)
    resourceList = ResourceList
    extensions = Array(Extension)


class RegistrationState(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.20
    registrationState = Attachment
    extensions = Array(Extension)


class RegistrationContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.21
    registrationHandle = Handle
    registrationState = Attachment
    extensions = Array(Extension)


# See WSRP 1.0 spec. 5.1.22
desiredLocales = Array(String)
desiredLocales.__namespace__ = WSRP_TYPES_NAMESPACE



##############################################################################
# Markup API
##############################################################################


class SessionContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.1
    sessionID = ID
    expires = Integer
    extensions = Array(Extension)


class Templates(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.6
    defaultTemplate = String
    blockingActionTemplate = String
    renderTemplate = String
    resourceTemplate = String
    secureDefaultTemplate = String
    secureBlockingActionTemplate = String
    secureRenderTemplate = String
    secureResourceTemplate = String
    extensions = Array(Extension)


class RuntimeContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.2
    userAuthentication = Mandatory.String
    portletInstanceKey = Key
    namespacePrefix = String
    templates = Templates # WTF?
    sessionID = ID
    extensions = Array(Extension)


class PortletContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.3
    portletHandle = Handle
    portletState = Attachment
    extensions = Array(Extension)


# standard user scopes, 6.1.4


class CacheControl(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.6
    expires = Mandatory.Integer
    userScope = Mandatory.String
    validateTag = String
    extensions = Array(Extension)


# Templates, 6.1.6, defined out of order because used by RuntimeContext


class ClientData(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.7
    userAgent = String
    extensions = Array(Extension)


class NamedString(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.8
    name = Mandatory.String
    value = Mandatory.String


class MarkupParams(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.9
    secureClientCommunication = Boolean         # XXX required
    locales = Array(String)
    mimeTypes = Array(String)
    mode = Mandatory.String
    windowState = Mandatory.String
    clientData = ClientData
    navigationalState = String
    markupCharacterSets = Array(String)
    validateTag = String
    validNewModes = Array(String)
    validNewWIndowStates = Array(String)
    extensions = Array(Extension)


class MarkupContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.10
    useCachedMarkup = Boolean
    mimeType = String
    markupString = String
    markupBinary = Attachment
    locale = String
    requiresUrlRewriting = Boolean
    cacheControl = CacheControl
    preferredTitle = String
    extensions = Array(Extension)


class MarkupResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.11
    markupContext = MarkupContext
    sessionContext = SessionContext
    extensions = Array(Extension)


class UpdateResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.12
    sessionContext = SessionContext
    portletContext = PortletContext
    markupContext = MarkupContext
    navigationalState = Mandatory.String
    newWindowState = String
    newMode = String


class BlockingInteractionResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.13
    updateResponse = UpdateResponse
    redirectURL = String
    extensions = Array(Extension)


# See WSRP 1.0 spec. 6.1.14
StateChange = Enum('readWrite', 'cloneBeforeWrite', 'readOnly',
                   type_name='String')
StateChange.__namespace__ = WSRP_TYPES_NAMESPACE


class UploadContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.15
    mimeType = Mandatory.String
    uploadData = Attachment
    mimeAttributes = Array(NamedString)
    extensions = Array(Extension)


class InteractionParams(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.16
    stateChange = StateChange                   # XXX required
    interactionState = String
    formParameters = Array(NamedString)
    uploadContexts = Array(UploadContext)
    extensions = Array(Extension)


class PersonName(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.1
    prefix = String
    given = String
    family = String
    middle = String
    suffix = String
    nickname = String
    extensions = Array(Extension)


class EmployerInfo(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.2
    employer = String
    department = String
    jobTitle = String
    extensions = Array(Extension)


class TelephoneNum(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.3
    intcode = String
    loccode = String
    number = String
    ext = String
    comment = String
    extensions = Array(Extension)


class Telecom(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.4
    telephone = TelephoneNum
    fax = TelephoneNum
    mobile = TelephoneNum
    pager = TelephoneNum
    extensions = Array(Extension)


class Online(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.5
    email = String
    uri = String
    extensions = Array(Extension)


class Postal(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.6
    name = String
    steet = String
    city = String
    stateprov = String
    country = String
    organization = String
    extensions = Array(Extension)


class Contact(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.7
    postal = Postal
    telecom = Telecom
    online = Online
    extensions = Array(Extension)


class UserProfile(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17
    name = PersonName
    bdate = Date
    gender = String
    employerInfo = EmployerInfo
    homeInfo = Contact
    businessInfo = Contact
    extensions = Array(Extension)


class UserContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.18
    userContextKey = Key
    userCategories = Array(String)
    profile = UserProfile
    extensions = Array(Extension)


# Not named in API
sessionIDs = Array(ID)
__namespace__ = WSRP_TYPES_NAMESPACE


##############################################################################
# Registration API
##############################################################################


class RegistrationData(_WSRPSerializer):
    # See WSRP 1.0 spec. 7.1.1
    consumerName = Mandatory.String
    consumerAgent = Mandatory.String
    methodGetSupported = Boolean            # XXX required
    consumerModes = Array(String)
    consumerWindowStates = Array(String)
    consumerUserScopes = Array(String)
    customUserProfileData = Array(String)
    registrationProperties = Array(Property)
    extensions = Array(Extension)


##############################################################################
# PortletManagement API
##############################################################################


class DestroyFailed(_WSRPSerializer):
    # See WSRP 1.0 spec. 8.1.1
    portletHandle = Handle                  # XXX required
    reason = String                         # XXX required


class DestroyPortletsResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 8.1.2
    destroyFailed = Array(DestroyFailed)
    extensions = Array(Extension)


class PortletDescriptionResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 8.1.3
    portletDescription = PortletDescription
    resourceList = ResourceList
    extensions = Array(Extension)


class PortletPropertyDescriptionResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 8.1.4
    modelDescription = ModelDescription
    resourceList = ResourceList
    extensions = Array(Extension)


# Not named in API
handleList = Array(ID)
handleList.__namespace__ = WSRP_TYPES_NAMESPACE


# Not named in API
nameList = Array(String)
nameList.__namespace__ = WSRP_TYPES_NAMESPACE
