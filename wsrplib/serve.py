"""\
Run a test WSRP portlet server.

Usage:  %s [OPTIONS]

Options
-------

--help, -h, -?          Print this usage message and exit with RC = 2.

--quiet, -q             Suppress inessential output.

--verbose, -v           Print more output.

--static-wsdl, -s       Render static WSDL.

--dynamic-wsdl, -d      Render dynamic WSDL.
"""
import os
import sys

from paste.urlmap import URLMap
from paste.urlparser import StaticURLParser

from wsrplib.dummy import DummyPortlet
from wsrplib.dummy import DummyServiceDescriptionInfo
from wsrplib.interfaces import IPortlet
from wsrplib.interfaces import IServiceDescriptionInfo
from wsrplib.markup import WSRP_v1_Markup
from wsrplib.service_description import WSRP_v1_ServiceDescription
from wsrplib.registration import WSRP_v1_Registration
from wsrplib.portlet_management import WSRP_v1_PortletManagement

def usage(message='', rc=1):
    print >>sys.stderr, __doc__ % sys.argv[0]
    if message:
        print >>sys.stderr
        print >>sys.stderr, message
    sys.exit(rc)

def main():
    import getopt
    import logging
    from wsgiref.simple_server import make_server

    from zope.component import provideUtility
    from soaplib.core.server import wsgi
    from wsrplib.application import Application
    from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
    wsdl_generation = None
    verbosity = 1
    endpoint_url = None

    logging.basicConfig(level=logging.DEBUG)

    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:],
                                       '?hqvsdu:',
                                       ['help',
                                        'quiet',
                                        'verbose',
                                        'static-wsdl',
                                        'dynamic-wsdl',
                                        'endpoint-url',
                                       ],
                                      )
    except getopt.GetoptError:
        usage(1)

    for k, v in opts:
        if k in ('--help', '-h', '-?'):
            usage(rc=2)
        if k in ('--quiet', '-q'):
            verbosity = 0
        if k in ('--verbose', '-v'):
            verbosity += 1
        if k in ('--static-wsdl', '-s'):
            wsdl_generation = 'static'
        if k in ('--dynamic-wsdl', '-d'):
            wsdl_generation = 'dynamic'
        if k in ('--endpoint-url', '-u'):
            endpoint_url = v

    provideUtility(DummyServiceDescriptionInfo(), IServiceDescriptionInfo)
    provideUtility(DummyPortlet(), IPortlet, name='dummy')
    soap_application = Application(
                            [WSRP_v1_ServiceDescription,
                             WSRP_v1_Markup,
                             WSRP_v1_Registration,
                             WSRP_v1_PortletManagement,
                            ],
                            tns=WSRP_TYPES_NAMESPACE,
                            name='WSRP_v1_Service',
                            _wsdl_generation=wsdl_generation,
                            _endpoint_url=endpoint_url,
                           )
    wsgi_application = wsgi.Application(soap_application)
    urlmap = URLMap()
    here = os.path.split(__file__)[0]
    urlmap['/static/'] = StaticURLParser(os.path.join(here, 'static'))
    urlmap['/'] = wsgi_application
    server = make_server('localhost', 7789, urlmap)

    print "listening to http://0.0.0.0:7789"
    print "wsdl is at: http://127.0.0.1:7789/?wsdl"
    server.serve_forever()

if __name__=='__main__':
    main()
