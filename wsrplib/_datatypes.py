# WSRP datatypes

from soaplib.serializers.binary import Attachment
from soaplib.serializers.enum import Enum
from soaplib.serializers.primitive import Any  # AnyAsDict?
from soaplib.serializers.primitive import AnyUri
from soaplib.serializers.primitive import Boolean
from soaplib.serializers.primitive import Date
from soaplib.serializers.primitive import Integer
from soaplib.serializers.primitive import String
from soaplib.serializers.primitive import Mandatory
from soaplib.serializers.clazz import Array
from soaplib.serializers.clazz import ClassSerializer


class QName(AnyUri):
    pass


class Extension(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.1
    any = Any


Handle = String(255)        # See WSRP 1.0 spec. 5.1.2


Key = String(255)           # See WSRP 1.0 spec. 5.1.3


ID = String(4096)           # See WSRP 1.0 spec. 5.1.4


##############################################################################
# ServiceDescription API
##############################################################################


class LocalizedString(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.5
    xmlLang = Mandatory.String
    value = Mandatory.String
    resourceName = String


class ResourceValue(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.6
    xmlLang = Mandatory.String
    value = Mandatory.String
    extensions = Array(Extension)


class Resource(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.7
    resourceName = Mandatory.String
    values = Array(ResourceValue)
    extensions = Array(Extension)


class ResourceList(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.8
    resources = Array(Resource)
    extensions = Array(Extension)


class ItemDescription(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.9
    itemName = Mandatory.String
    description = LocalizedString
    extensions = Array(Extension)

class MarkupType(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.10
    mimeType = Mandatory.String
    modes = Array(String)
    windowStates = Array(String)
    locales = Array(String)
    extensions = Array(Extension)

class PortletDescription(ClassSerializer):
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


class Property(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.12
    name = Mandatory.String
    xmlLang = String
    value = Array(Any)


class ResetProperty(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.13
    name = Mandatory.String


class PropertyList(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.14
    properties = Array(Property)
    resetProperties = Array(ResetProperty)
    extensions = Array(Extension)


class PropertyDescription(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.15
    name = Mandatory.String
    type = QName
    label = LocalizedString
    hint = LocalizedString
    extensions = Array(Extension)


class ModelTypes(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.16
    any = Array(Any)


class ModelDescription(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.17
    propertyDescriptions = Array(PropertyDescription)
    modelTypes = ModelTypes
    extensions = Array(Extension)


CookieProtocol = Enum('none', 'perUser', 'perGroup',
                      type_name='String')   # See WSRP 1.0 spec. 5.1.18



class ServiceDescription(ClassSerializer):
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


class RegistrationState(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.20
    registrationState = Attachment
    extensions = Array(Extension)


class RegistrationContext(ClassSerializer):
    # See WSRP 1.0 spec. 5.1.21
    registrationHandle = Handle
    registrationState = Attachment
    extensions = Array(Extension)


desiredLocales = Array(String)        # See WSRP 1.0 spec. 5.1.22



##############################################################################
# Markup API
##############################################################################


class SessionContext(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.1
    sessionID = ID
    expires = Integer
    extensions = Array(Extension)


class Templates(ClassSerializer):
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


class RuntimeContext(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.2
    userAuthentication = Mandatory.String
    portletInstanceKey = Key
    namespacePrefix = String
    templates = Templates # WTF?
    sessionID = ID
    extensions = Array(Extension)


class PortletContext(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.3
    portletHandle = Handle
    portletState = Attachment
    extensions = Array(Extension)


# standard user scopes, 6.1.4


class CacheControl(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.6
    expires = Mandatory.Integer
    userScope = Mandatory.String
    validateTag = String
    extensions = Array(Extension)


# Templates, 6.1.6, defined out of order because used by RuntimeContext


class ClientData(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.7
    userAgent = String
    extensions = Array(Extension)


class NamedString(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.8
    name = Mandatory.String
    value = Mandatory.String


class MarkupParams(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.9
    secureClientCommunication = Boolean # XXX required
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


class MarkupContext(ClassSerializer):
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


class MarkupResponse(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.11
    markupContext = MarkupContext
    sessionContext = SessionContext
    extensions = Array(Extension)


class UpdateResponse(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.12
    sessionContext = SessionContext
    portletContext = PortletContext
    markupContext = MarkupContext
    navigationalState = Mandatory.String
    newWindowState = String
    newMode = String


class BlockingInteractionResponse(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.13
    updateResponse = UpdateResponse
    redirectURL = String
    extensions = Array(Extension)


StateChange = Enum('readWrite', 'cloneBeforeWrite', 'readOnly',
                      type_name='String')   # See WSRP 1.0 spec. 6.1.14


class UploadContext(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.15
    mimeType = Mandatory.String
    uploadData = Attachment
    mimeAttributes = Array(NamedString)
    extensions = Array(Extension)


class InteractionParams(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.16
    stateChange = StateChange # required
    interactionState = String
    formParameters = Array(NamedString)
    uploadContexts = Array(UploadContext)
    extensions = Array(Extension)


class PersonName(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.17.1
    prefix = String
    given = String
    family = String
    middle = String
    suffix = String
    nickname = String
    extensions = Array(Extension)


class EmployerInfo(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.17.2
    employer = String
    department = String
    jobTitle = String
    extensions = Array(Extension)


class TelephoneNum(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.17.3
    intcode = String
    loccode = String
    number = String
    ext = String
    comment = String
    extensions = Array(Extension)


class Telecom(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.17.4
    telephone = TelephoneNum
    fax = TelephoneNum
    mobile = TelephoneNum
    pager = TelephoneNum
    extensions = Array(Extension)


class Online(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.17.5
    email = String
    uri = String
    extensions = Array(Extension)


class Postal(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.17.6
    name = String
    steet = String
    city = String
    stateprov = String
    country = String
    organization = String
    extensions = Array(Extension)


class Contact(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.17.7
    postal = Postal
    telecom = Telecom
    online = Online
    extensions = Array(Extension)


class UserProfile(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.17
    name = PersonName
    bdate = Date
    gender = String
    employerInfo = EmployerInfo
    homeInfo = Contact
    businessInfo = Contact
    extensions = Array(Extension)


class UserContext(ClassSerializer):
    # See WSRP 1.0 spec. 6.1.18
    userContextKey = Key
    userCategories = Array(String)
    profile = UserProfile
    extensions = Array(Extension)

sessionIDs = Array(ID)

##############################################################################
# Registration API
##############################################################################


class RegistrationData(ClassSerializer):
    # See WSRP 1.0 spec. 7.1.1
    consumerName = Mandatory.String
    consumerAgent = Mandatory.String
    methodGetSupported = Boolean # required
    consumerModes = Array(String)
    consumerWindowStates = Array(String)
    consumerUserScopes = Array(String)
    customUserProfileData = Array(String)
    registrationProperties = Array(Property)
    extensions = Array(Extension)
