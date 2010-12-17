from soaplib.service import DefinitionBase
from soaplib.service import document
from zope.component import queryUtility

from wsrplib.interfaces import IPortlet
from wsrplib.datatypes import BlockingInteractionResponse
from wsrplib.datatypes import InteractionParams
from wsrplib.datatypes import MarkupParams
from wsrplib.datatypes import MarkupResponse
from wsrplib.datatypes import PortletContext
from wsrplib.datatypes import RegistrationContext
from wsrplib.datatypes import RuntimeContext
from wsrplib.datatypes import StringSeq
from wsrplib.datatypes import UserContext
from wsrplib.faults import AccessDenied
from wsrplib.faults import InconsistentParameters
from wsrplib.faults import InvalidCookie
from wsrplib.faults import InvalidHandle
from wsrplib.faults import InvalidRegistration
from wsrplib.faults import InvalidSession
from wsrplib.faults import InvalidUserCategory
from wsrplib.faults import MissingParameters
from wsrplib.faults import OperationFailed
from wsrplib.faults import PortletStateChangeRequired
from wsrplib.faults import UnsupportedLocale
from wsrplib.faults import UnsupportedMimeType
from wsrplib.faults import UnsupportedMode
from wsrplib.faults import UnsupportedWindowState
from wsrplib.namespaces import WSRP_TYPES_NAMESPACE

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
        """ See WSRP 1.0 spec. 6.4
        """
        return OperationFailed()
