from lxml.etree import Element
from lxml.etree import SubElement
from lxml.etree import tostring
from soaplib import Application as _Application
from soaplib import ns_wsdl
from soaplib import ns_soap

from wsrplib._namespaces import WSRP_BIND_NAMESPACE
from wsrplib._namespaces import WSRP_INTF_NAMESPACE
from wsrplib._namespaces import WSRP_TYPES_NAMESPACE
from wsrplib._namespaces import WSRP_WSDL_NAMESPACE

#_WSRP_BASE_URL = 'http://www.oasis-open.org/committees/wsrp/specifications'
#_WSRP_BIND_URL = '%s/version1/wsrp_v1_bindings.wsdl' % _WSRP_BASE_URL
_WSRP_BIND_URL = '/static/wsrp_v1_bindings.wsdl'
_WSRP_SERVICE_NAME_TEMPLATE = 'WSRP_v1_%s_Service'
_WSRP_SERVICE_SOAP_BINDING_TEMPLATE = 'WSRP_v1_%s_Binding_SOAP'


_NS_MAP = {
    'soap': ns_soap,
    'wsdl': ns_wsdl,
    'bind': WSRP_BIND_NAMESPACE,
    'intf': WSRP_INTF_NAMESPACE,
    'types': WSRP_TYPES_NAMESPACE,
    'wsrp': WSRP_WSDL_NAMESPACE,
}

class Application(_Application):

    def __build_wsdl(self, url):
        """ Override to import standard WSDL rather than introspect.
        """
        root = Element('{%s}definitions' % ns_wsdl, nsmap=_NS_MAP)
        root.set('targetNamespace', WSRP_WSDL_NAMESPACE)

        import_ = SubElement(root, 'import')
        import_.set('namespace', WSRP_BIND_NAMESPACE)
        import_.set('location', _WSRP_BIND_URL)

        service = SubElement(root, '{%s}service' % ns_wsdl)
        service.set('name', self.name)

        for name in ('ServiceDescrption', 'Markup'):
            port = SubElement(service, '{%s}port' % ns_wsdl)
            port.set('name', _WSRP_SERVICE_NAME_TEMPLATE % name)
            port.set('binding', _WSRP_SERVICE_SOAP_BINDING_TEMPLATE % name)

            soap = SubElement(port, '{%s}addresss' % ns_soap)
            soap.set('location', url)

        self.__wsdl = tostring(root, xml_declaration=True, encoding="UTF-8")

        return self.__wsdl
