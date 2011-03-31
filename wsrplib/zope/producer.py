"""
"""

from zope.publisher.browser import BrowserPage

from wsrplib.application import Application
from wsrplib.markup import WSRP_v1_Markup
from wsrplib.service_description import WSRP_v1_ServiceDescription
from wsrplib.registration import WSRP_v1_Registration
from wsrplib.portlet_management import WSRP_v1_PortletManagement
from wsrplib.namespaces import WSRP_TYPES_NAMESPACE


from soaplib.zope.metaconfigure import SoaplibHandler


class PortletsProducer(BrowserPage, Application):
    """Container of portlets, made available via web services.
    """

    transport = 'http://schemas.xmlsoap.org/soap/http'

    def __init__(self, context, request):
        BrowserPage.__init__(self, context, request)

        self.soap_app = Application(
                             services=[
                                 WSRP_v1_ServiceDescription,
                                 WSRP_v1_Markup,
                                 WSRP_v1_Registration,
                                 WSRP_v1_PortletManagement,
                                 ],
                             tns=WSRP_TYPES_NAMESPACE,
                             name='WSRP_v1_Service',
                             _wsdl_generation=None,
                             _endpoint_url=self.request.getURL(),
                             )
        self.soaplib_handler = SoaplibHandler(
                                self.request,
                                self.soap_app
                                )

    def __call__(self, *args, **kw):
        """  """
        self.soaplib_handler.handle_request()
