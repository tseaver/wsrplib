"""
"""

from zope.publisher.browser import BrowserPage

from wsrplib.application import Application
from wsrplib.markup import WSRP_v1_Markup
from wsrplib.service_description import WSRP_v1_ServiceDescription
from wsrplib.registration import WSRP_v1_Registration
from wsrplib.portlet_management import WSRP_v1_PortletManagement
from wsrplib.namespaces import WSRP_TYPES_NAMESPACE

class PortletsProducer(BrowserPage, Application):
    """Container of portlets, made available via web services.
    """

    transport = 'http://schemas.xmlsoap.org/soap/http'

    def __init__(self, context, request):
        BrowserPage.__init__(self, context, request)

        Application.__init__(self,
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

    def __call__(self, *args, **kw):
        """  """
        if self.__is_wsdl_request():
            self.request.response.setHeader('Content-Type', 'text/xml')
            return self.get_wsdl(url=self.request.getURL())

        print "GOT UNHANDLED SOAP CALL!"

        #TBD: ~/Clients/ZeOmega/jiva3/lib/python/soaplib/zope2.py

        self.request.response.setHeader('Content-Type', 'text/plain')
        return '(I got nada)'




    def __is_wsdl_request(self):
        """Test whether the request is for the WSDL of the producer service.

           Assume path_info matches pattern:
               /stuff/stuff/stuff/serviceName.wsdl
           or
               /stuff/stuff/stuff/serviceName/?wsdl
        """
        return (
            self.request['REQUEST_METHOD'].lower() == 'get'
            and (
                self.request['QUERY_STRING'].endswith('wsdl')
                or self.request['PATH_INFO'].endswith('wsdl')
                )
            )
