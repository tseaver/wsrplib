API Reference
=============

Interfaces
----------

.. automodule:: wsrplib.interfaces

  .. autointerface:: IPortlet
     :members:

  .. autointerface:: IMarkupType
     :members:

  .. autointerface:: IServiceDescriptionInfo
     :members:

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
     :members:

.. automodule:: wsrplib.markup

  .. autoclass:: WSRP_v1_Markup
     :members:

.. automodule:: wsrplib.registration

  .. autoclass:: WSRP_v1_Registration
     :members:

.. automodule:: wsrplib.portlet_management

  .. autoclass:: WSRP_v1_PortletManagement
     :members:

