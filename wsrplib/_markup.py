from soaplib.service import DefinitionBase
from soaplib.service import document
from zope.component import queryUtility

from wsrplib.interfaces import IPortlet
from wsrplib._datatypes import BlockingInteractionResponse
from wsrplib._datatypes import InteractionParams
from wsrplib._datatypes import MarkupParams
from wsrplib._datatypes import MarkupResponse
from wsrplib._datatypes import PortletContext
from wsrplib._datatypes import RegistrationContext
from wsrplib._datatypes import RuntimeContext
from wsrplib._datatypes import StringSeq
from wsrplib._datatypes import UserContext
from wsrplib._faults import AccessDenied
from wsrplib._faults import InconsistentParameters
from wsrplib._faults import InvalidCookie
from wsrplib._faults import InvalidHandle
from wsrplib._faults import InvalidRegistration
from wsrplib._faults import InvalidSession
from wsrplib._faults import InvalidUserCategory
from wsrplib._faults import MissingParameters
from wsrplib._faults import OperationFailed
from wsrplib._faults import PortletStateChangeRequired
from wsrplib._faults import UnsupportedLocale
from wsrplib._faults import UnsupportedMimeType
from wsrplib._faults import UnsupportedMode
from wsrplib._faults import UnsupportedWindowState
from wsrplib._namespaces import WSRP_TYPES_NAMESPACE

class WSRP_v1_Markup(DefinitionBase):
    __namespace__ = WSRP_TYPES_NAMESPACE

    @classmethod
    def get_tns(cls):
        # Override to get our messages in the right namespace
        return cls.__namespace__

    @document(RegistrationContext,
              PortletContext,
              RuntimeContext,
              UserContext,
              MarkupParams,
              _faults=[AccessDenied,
                       InconsistentParameters,
                       InvalidCookie,
                       InvalidHandle,
                       InvalidRegistration,
                       InvalidSession,
                       InvalidUserCategory,
                       MissingParameters,
                       OperationFailed,
                       UnsupportedLocale,
                       UnsupportedMimeType,
                       UnsupportedMode,
                       UnsupportedWindowState,
                      ],
              _returns=MarkupResponse,
             )
    def getMarkup(self,
        registrationContext,
        portletContext,
        runtimeContext,
        userContext,
        markupParams,
        ):
        """ See WSRP 1.0 spec. 6.2
        """
        p_handle = portletContext.portletHandle
        portlet = queryUtility(IPortlet, name=p_handle)
        if portlet is None:
            return InvalidHandle('No such portlet: %s' % p_handle)
        m_response = MarkupResponse()
        try:
            m_response.markupContext = portlet.GET(registrationContext,
                                                   portletContext,
                                                   runtimeContext,
                                                   userContext,
                                                   markupParams,
                                                  )
            # XXX sessionContext in response?
        except Exception, e:
            return OperationFailed(str(e))
        else:
            return m_response

    @document(RegistrationContext,
              PortletContext,
              RuntimeContext,
              UserContext,
              MarkupParams,
              InteractionParams,
              _faults=[AccessDenied,
                       InconsistentParameters,
                       InvalidCookie,
                       InvalidHandle,
                       InvalidRegistration,
                       InvalidSession,
                       InvalidUserCategory,
                       MissingParameters,
                       OperationFailed,
                       PortletStateChangeRequired,
                       UnsupportedLocale,
                       UnsupportedMimeType,
                       UnsupportedMode,
                       UnsupportedWindowState,
                      ],
              _returns=BlockingInteractionResponse,
             )
    def performBlockingInteraction(self,
        registrationContext,
        portletContext,
        runtimeContext,
        userContext,
        markupParams,
        interactionParams,
        ):
        """ See WSRP 1.0 spec. 6.3
        """
        return OperationFailed()

    @document(RegistrationContext,
              _faults=[AccessDenied,
                       InvalidRegistration,
                       OperationFailed,
                      ],
             )
    def initCookie(self,
        registrationContext,
        ):
        """ See WSRP 1.0 spec. 6.4
        """
        return OperationFailed()

    @document(RegistrationContext,
              StringSeq,
              _faults=[AccessDenied,
                       InvalidRegistration,
                       MissingParameters,
                       OperationFailed,
                      ],
             )
    def releaseSessions(self,
        registrationContext,
        sessionIDs,
        ):
        # See WSRP 1.0 spec. 6.4
        return OperationFailed()
