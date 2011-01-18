API Reference
=============

Interfaces
----------

.. automodule:: wsrplib.interfaces

  .. autointerface:: IPortlet
     :members:
     :member-order: alphabetical

  .. autointerface:: IMarkupType
     :members:
     :member-order: alphabetical

  .. autointerface:: IServiceDescriptionInfo
     :members:
     :member-order: alphabetical

WSRP Datatypes
--------------

.. automodule:: wsrplib.datatypes

  .. autoclass:: Handle

  .. autoclass:: Key

  .. autoclass:: ID

  .. autoclass:: LocalizedString

  .. autoclass:: ResourceValue

  .. autoclass:: Resource

  .. autoclass:: ResourceList

  .. autoclass:: ItemDescription

  .. autoclass:: MarkupType

  .. autoclass:: PortletDescription

  .. autoclass:: Property

  .. autoclass:: ResetProperty

  .. autoclass:: PropertyList

  .. autoclass:: PropertyDescription

  .. autoclass:: ModelTypes

  .. autoclass:: ModelDescription

  .. autoclass:: CookieProtocol

  .. autoclass:: ServiceDescription

  .. autoclass:: RegistrationState

  .. autoclass:: RegistrationContext

  .. autoclass:: SessionContext

  .. autoclass:: Templates

  .. autoclass:: RuntimeContext

  .. autoclass:: PortletContext

  .. autoclass:: CacheControl

  .. autoclass:: ClientData

  .. autoclass:: NamedString

  .. autoclass:: MarkupParams

  .. autoclass:: MarkupContext

  .. autoclass:: MarkupResponse

  .. autoclass:: UpdateResponse

  .. autoclass:: BlockingInteractionResponse

  .. autoclass:: StateChange

  .. autoclass:: UploadContext

  .. autoclass:: InteractionParams

  .. autoclass:: PersonName

  .. autoclass:: EmployerInfo

  .. autoclass:: TelephoneNum

  .. autoclass:: Telecom

  .. autoclass:: Online

  .. autoclass:: Postal

  .. autoclass:: Contact

  .. autoclass:: UserProfile

  .. autoclass:: UserContext

  .. autoclass:: RegistrationData

  .. autoclass:: DestroyFailed

  .. autoclass:: DestroyPortletsResponse

  .. autoclass:: PortletDescriptionResponse

  .. autoclass:: PortletPropertyDescriptionResponse



WSRP Faults
-----------

.. automodule:: wsrplib.faults

  .. autoclass:: AccessDenied

  .. autoclass:: InvalidUserCategory

  .. autoclass:: InconsistentParameters

  .. autoclass:: InvalidRegistration

  .. autoclass:: MissingParameters

  .. autoclass:: OperationFailed

  .. autoclass:: InvalidHandle

  .. autoclass:: PortletStateChangeRequired

  .. autoclass:: InvalidCookie

  .. autoclass:: InvalidSession

  .. autoclass:: UnsupportedMode

  .. autoclass:: UnsupportedWindowState

  .. autoclass:: UnsupportedLocale

  .. autoclass:: UnsupportedMimeType


WSRP Ports
----------

.. automodule:: wsrplib.service_description

  .. autoclass:: WSRP_v1_ServiceDescription
     
    .. automethod:: getServiceDescription(RegistrationContext, desiredLocales) -> ServiceDescription

.. automodule:: wsrplib.markup

  .. autoclass:: WSRP_v1_Markup

    .. automethod:: getMarkup(RegistrationContext, PortletContext, RuntimeContext, UserContext, MarkupParams) -> MarkupResponse

    .. automethod:: performBlockingInteraction(RegistrationContext, PortletContext, RuntimeContext, UserContext, MarkupParams, InteractionParams) -> BlockingInterationResponse

    .. automethod:: initCookie(RegistrationContext)

    .. automethod:: releaseSessions(RegistrationContext, sessionIDs)

.. automodule:: wsrplib.registration

  .. autoclass:: WSRP_v1_Registration

    .. automethod:: register(RegistrationData) -> RegistrationContext

    .. automethod:: modifyRegistration(RegistrationContext, RegistrationData) -> RegistrationState

    .. automethod:: deregister(RegistrationContext)

.. automodule:: wsrplib.portlet_management

  .. autoclass:: WSRP_v1_PortletManagement

    .. automethod:: getPortletDescription(RegistrationContext, PortletContext, UserContext, desiredLocales) -> PortletDescriptionResponse

    .. automethod:: clonePortlet(RegistrationContext, PortletContext, UserContext) -> PortletContext

    .. automethod:: destroyPortlets(RegistrationContext, portletHandles) -> DestroyPortletsResponse

    .. automethod:: getPortletProperties(RegistrationContext, PortletContext, UserContext, propertyNames) -> PropertyList

    .. automethod:: getPortletPropertyDescription(RegistrationContext, PortletContext, UserContext, desiredLocales) -> PortletPropertyDescriptionResponse
