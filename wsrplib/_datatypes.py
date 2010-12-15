# WSRP datatypes

from soaplib.model import SimpleType
from soaplib.model.binary import Attachment
from soaplib.model.enum import Enum
from soaplib.model.primitive import Any  # AnyAsDict?
from soaplib.model.primitive import Boolean
from soaplib.model.primitive import Date
from soaplib.model.primitive import Integer
from soaplib.model.primitive import String
from soaplib.model.clazz import ClassSerializer
from soaplib.model.clazz import XMLAttribute
from soaplib.model.clazz import XMLAttributeRef

from wsrplib._namespaces import WSRP_TYPES_NAMESPACE

def _makeSeq(cls):
    return cls.customize(min_occurs=0, max_occurs="unbounded", nillable=False)

def _makeNotNillable(cls):
    return cls.customize(min_occurs=0, nillable=False)

StringSeq = _makeSeq(String)
StringSeqNotEmpty = String.customize(min_occurs=1, max_occurs="unbounded",
                                     nillable=False)
AnySeq = _makeSeq(Any)


class _WSRPSerializer(ClassSerializer):
    __namespace__ = WSRP_TYPES_NAMESPACE


class _WSRPString(String):
    __namespace__ = WSRP_TYPES_NAMESPACE
    __base_type__ = String


class _WSRPMandatoryString(String):
    __namespace__ = WSRP_TYPES_NAMESPACE
    __base_type__ = String
    __type_name__ = 'MandatoryString'
    class Attributes(SimpleType.Attributes):
        min_len = 1
        min_occurs = 1
        max_len = "unbounded"
        pattern = None
        nillable = False


#class Extension(_WSRPSerializer):
#    # See WSRP 1.0 spec. 5.1.1
#    any = AnySeq
#
#ExtensionSeq = _makeSeq(Extension)


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
    xmlLang = XMLAttributeRef('xml:lang', use='required')
    value = _WSRPMandatoryString
    resourceName = XMLAttribute('xs:string')

LocalizedStringSeq = _makeSeq(LocalizedString)


class ResourceValue(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.6
    xmlLang = XMLAttributeRef('xml:lang', use='required')
    value = _WSRPMandatoryString
    #extensions = ExtensionSeq

ResourceValueSeq = _makeSeq(ResourceValue)


class Resource(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.7
    resourceName = XMLAttribute('xs:string', use='required')
    values = ResourceValueSeq
    #extensions = ExtensionSeq

ResourceSeq = _makeSeq(Resource)


class ResourceList(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.8
    resources = ResourceSeq
    #extensions = ExtensionSeq

ResourceListNotNillable = _makeNotNillable(ResourceList)

class ItemDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.9
    itemName = XMLAttribute('xs:string', use='required')
    description = LocalizedString
    #extensions = ExtensionSeq

ItemDescriptionSeq = _makeSeq(ItemDescription)


class MarkupType(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.10
    mimeType = _WSRPMandatoryString
    modes = StringSeqNotEmpty
    windowStates = StringSeqNotEmpty
    locales = StringSeq
    #extensions = ExtensionSeq

MarkupTypeSeq = _makeSeq(MarkupType)


class PortletDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.11
    portletHandle = Handle
    markupTypes = MarkupTypeSeq
    groupID = ID
    description = LocalizedString
    shortTitle = LocalizedString
    title = LocalizedString
    displayName = LocalizedString
    keywords = LocalizedStringSeq
    userCategories = StringSeq
    userProfileItems = StringSeq
    usesMethodGet = Boolean
    defaultMarkupSecure = Boolean
    onlySecure = Boolean
    userContextStoredInSession = Boolean
    templatesStoredInSession = Boolean
    hasUserSpecificState = Boolean
    doesUrlTemplateProcessing = Boolean
    #extensions = ExtensionSeq

PortletDescriptionSeq = _makeSeq(PortletDescription)


class Property(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.12
    name = XMLAttribute('xs:string', use='required')
    xmlLang = XMLAttributeRef('xml:lang', use='required')
    stringValue = StringSeq
    value = AnySeq

PropertySeq = _makeSeq(Property)


class ResetProperty(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.13
    name = XMLAttribute('xs:string', use='required')

ResetPropertySeq = _makeSeq(ResetProperty)


class PropertyList(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.14
    properties = PropertySeq
    resetProperties = ResetPropertySeq
    #extensions = ExtensionSeq


class PropertyDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.15
    name = XMLAttribute('xs:string', use='required')
    type = XMLAttribute('xs:QName', use='required')
    label = LocalizedString
    hint = LocalizedString
    #extensions = ExtensionSeq

PropertyDescriptionSeq = _makeSeq(PropertyDescription)


class ModelTypes(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.16
    any = AnySeq


class ModelDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.17
    propertyDescriptions = PropertyDescriptionSeq
    modelTypes = ModelTypes
    #extensions = ExtensionSeq

ModelDescriptionNotNillable = _makeNotNillable(ModelDescription)

# See WSRP 1.0 spec. 5.1.18
CookieProtocol = Enum('none', 'perUser', 'perGroup', type_name='CookieProtocol')
CookieProtocol__namespace__ = WSRP_TYPES_NAMESPACE



class ServiceDescription(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.19
    requiresRegistration = Boolean
    offeredPortlets = PortletDescriptionSeq
    userCategoryDescriptions = ItemDescriptionSeq
    customUserProfileItemDescriptions = ItemDescriptionSeq
    customWindowStateDescriptions = ItemDescriptionSeq
    customModeDescriptions = ItemDescriptionSeq
    requiresInitCookie = CookieProtocol
    registrationPropertyDescription = ModelDescriptionNotNillable
    locales = StringSeq
    resourceList = ResourceListNotNillable
    #extensions = ExtensionSeq


class RegistrationState(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.20
    registrationState = Attachment
    #extensions = ExtensionSeq


class RegistrationContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 5.1.21
    registrationHandle = Handle
    registrationState = Attachment
    #extensions = ExtensionSeq



##############################################################################
# Markup API
##############################################################################


class SessionContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.1
    sessionID = ID
    expires = Integer
    #extensions = ExtensionSeq


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
    #extensions = ExtensionSeq


class RuntimeContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.2
    userAuthentication = _WSRPMandatoryString
    portletInstanceKey = Key
    namespacePrefix = String
    templates = Templates # WTF?
    sessionID = ID
    #extensions = ExtensionSeq


class PortletContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.3
    portletHandle = Handle
    portletState = Attachment
    #extensions = ExtensionSeq


# standard user scopes, 6.1.4


class CacheControl(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.6
    expires = _WSRPMandatoryString
    userScope = _WSRPMandatoryString
    validateTag = String
    #extensions = ExtensionSeq


# Templates, 6.1.6, defined out of order because used by RuntimeContext


class ClientData(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.7
    userAgent = String
    #extensions = ExtensionSeq


class NamedString(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.8
    name = XMLAttribute('xs:string', use='required')
    value = _WSRPMandatoryString

NamedStringSeq = _makeSeq(NamedString)


class MarkupParams(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.9
    secureClientCommunication = Boolean         # XXX required
    locales = StringSeq
    mimeTypes = StringSeqNotEmpty
    mode = _WSRPMandatoryString
    windowState = _WSRPMandatoryString
    clientData = ClientData
    navigationalState = String
    markupCharacterSets = StringSeq
    validateTag = String
    validNewModes = StringSeq
    validNewWIndowStates = StringSeq
    #extensions = ExtensionSeq


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
    #extensions = ExtensionSeq


class MarkupResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.11
    markupContext = MarkupContext
    sessionContext = SessionContext
    #extensions = ExtensionSeq


class UpdateResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.12
    sessionContext = SessionContext
    portletContext = PortletContext
    markupContext = MarkupContext
    navigationalState = _WSRPMandatoryString
    newWindowState = String
    newMode = String


class BlockingInteractionResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.13
    updateResponse = UpdateResponse
    redirectURL = String
    #extensions = ExtensionSeq


# See WSRP 1.0 spec. 6.1.14
StateChange = Enum('readWrite', 'cloneBeforeWrite', 'readOnly',
                   type_name='StateChange')
StateChange.__namespace__ = WSRP_TYPES_NAMESPACE


class UploadContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.15
    mimeType = _WSRPMandatoryString
    uploadData = Attachment
    mimeAttributes = NamedStringSeq
    #extensions = ExtensionSeq

UploadContextSeq = _makeSeq(UploadContext)


class InteractionParams(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.16
    stateChange = StateChange                   # XXX required
    interactionState = String
    formParameters = NamedStringSeq
    uploadContexts = UploadContextSeq
    #extensions = ExtensionSeq


class PersonName(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.1
    prefix = String
    given = String
    family = String
    middle = String
    suffix = String
    nickname = String
    #extensions = ExtensionSeq


class EmployerInfo(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.2
    employer = String
    department = String
    jobTitle = String
    #extensions = ExtensionSeq


class TelephoneNum(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.3
    intcode = String
    loccode = String
    number = String
    ext = String
    comment = String
    #extensions = ExtensionSeq


class Telecom(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.4
    telephone = TelephoneNum
    fax = TelephoneNum
    mobile = TelephoneNum
    pager = TelephoneNum
    #extensions = ExtensionSeq


class Online(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.5
    email = String
    uri = String
    #extensions = ExtensionSeq


class Postal(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.6
    name = String
    steet = String
    city = String
    stateprov = String
    country = String
    organization = String
    #extensions = ExtensionSeq


class Contact(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17.7
    postal = Postal
    telecom = Telecom
    online = Online
    #extensions = ExtensionSeq


class UserProfile(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.17
    name = PersonName
    bdate = Date
    gender = String
    employerInfo = EmployerInfo
    homeInfo = Contact
    businessInfo = Contact
    #extensions = ExtensionSeq


class UserContext(_WSRPSerializer):
    # See WSRP 1.0 spec. 6.1.18
    userContextKey = Key
    userCategories = StringSeq
    profile = UserProfile
    #extensions = ExtensionSeq



##############################################################################
# Registration API
##############################################################################


class RegistrationData(_WSRPSerializer):
    # See WSRP 1.0 spec. 7.1.1
    consumerName = _WSRPMandatoryString
    consumerAgent = _WSRPMandatoryString
    methodGetSupported = Boolean            # XXX required
    consumerModes = StringSeq
    consumerWindowStates = StringSeq
    consumerUserScopes = StringSeq
    customUserProfileData = StringSeq
    registrationProperties = StringSeq
    #extensions = ExtensionSeq


##############################################################################
# PortletManagement API
##############################################################################


class DestroyFailed(_WSRPSerializer):
    # See WSRP 1.0 spec. 8.1.1
    portletHandle = Handle                  # XXX required
    reason = String                         # XXX required

DestroyFailedSeq = _makeSeq(DestroyFailed)


class DestroyPortletsResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 8.1.2
    destroyFailed = DestroyFailedSeq
    #extensions = ExtensionSeq


class PortletDescriptionResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 8.1.3
    portletDescription = PortletDescription
    resourceList = ResourceList
    #extensions = ExtensionSeq


class PortletPropertyDescriptionResponse(_WSRPSerializer):
    # See WSRP 1.0 spec. 8.1.4
    modelDescription = ModelDescription
    resourceList = ResourceList
    #extensions = ExtensionSeq
