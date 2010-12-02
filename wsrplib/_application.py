from lxml.etree import Comment
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
_WSRP_SERVICE_SOAP_BINDING_TEMPLATE = 'bind:WSRP_v1_%s_Binding_SOAP'

_NS_MAP = {
    None: ns_wsdl,
    'soap': ns_soap,
    'wsdl': ns_wsdl,
    'bind': WSRP_BIND_NAMESPACE,
    'intf': WSRP_INTF_NAMESPACE,
    'types': WSRP_TYPES_NAMESPACE,
    'wsrp': WSRP_WSDL_NAMESPACE,
}

class Application(_Application):

    def __init__(self, services, tns, name=None,
                 _with_partnerlink=False,
                 _wsdl_generation=None,
                ):
        super(Application, self).__init__(services, tns, name,
                                          _with_partnerlink,
                                         )
        self._wsdl_generation = _wsdl_generation
        for prefix, namespace in _NS_MAP.items():
            if prefix is not None:
                self.set_namespace_prefix(namespace, prefix)

        # Rebuild after updating namespaces.
        self.call_routes = {}
        self.build_schema()

    def __build_wsdl(self, url):
        """ Override to import standard WSDL rather than introspect.
        """
        if self._wsdl_generation == 'dynamic':
            return self._build_dynamic_wsdl(url)

        if self._wsdl_generation == 'static':
            return self._build_static_wsdl(url)

        return super(Application, self).__build_wsdl(url)

    def _build_dynamic_wsdl(self, url):
        #return super(Application, self).__build_wsdl(url)
        # Ripping off soaplib._base.Application.__build_wsdl
        services = {}
        for s_klass in self.services:
            name = s_klass.__name__.split('.')[-1]
            inst = self.get_service(s_klass, None)
            services[name] = inst

        url = url.replace('.wsdl', '')
        service_name = self.get_name()
        root = Element("{%s}definitions" % ns_wsdl, nsmap=_NS_MAP)
        root.set('targetNamespace', WSRP_WSDL_NAMESPACE)

        root.append(Comment('Begin WSRP 1.0 types'))
        types = SubElement(root, "{%s}types" % ns_wsdl)
        self.build_schema(types)
        root.append(Comment('End WSRP 1.0 types'))

        root.append(Comment('Begin WSRP 1.0 messages'))
        messages = set()
        # XXX faults?
        for name, inst in services.items():
            inst.add_messages_for_methods(self, root, messages)
        root.append(Comment('End WSRP 1.0 messages'))

        port_types = {}
        root.append(Comment('Begin WSRP 1.0 port types'))
        for name, inst in services.items():
            port_type = SubElement(root, '{%s}portType' % ns_wsdl)
            pt_name = port_types[name] = '%s_PortType' % name
            port_type.set('name', pt_name)
            inst.add_port_type(self, root, name, types, url, port_type)
        root.append(Comment('End WSRP 1.0 port types'))

        root.append(Comment('Begin WSRP 1.0 bindings'))
        for name, inst in services.items():
            binding = SubElement(root, '{%s}binding' % ns_wsdl)
            binding.set('name', name)
            binding.set('type', '%s:%s'% (inst.__namespace__,
                                          port_types[name]))

            soap_binding = SubElement(binding, '{%s}binding' % ns_soap)
            soap_binding.set('style', 'document')

            if self.transport is None:
                raise Exception("You must set the 'transport' property")
            soap_binding.set('transport', self.transport)

            inst.add_bindings_for_methods(self, root, name, types, url,
                                          binding, None)

        root.append(Comment('End WSRP 1.0 bindings'))

        root.append(Comment('Begin WSRP 1.0 services'))
        for name, inst in services.items():
            service = SubElement(root, '{%s}service' % ns_wsdl)
            service.set('name', '%s_Service' % name)
            self._add_service(root, name, types, url, service)
        root.append(Comment('End WSRP 1.0 services'))

        self.__wsdl = tostring(root, xml_declaration=True, encoding="UTF-8")

        return self.__wsdl

    def _add_service(self, root, service_name, types, url, service):
        # Ripping off soaplib._base.Application.__add_service

        wsdl_port = SubElement(service, '{%s}port' % ns_wsdl)
        wsdl_port.set('name', service_name)
        wsdl_port.set('binding', 'bind:%s' % service_name)

        addr = SubElement(wsdl_port, '{%s}address' % ns_soap)
        addr.set('location', url)

    def _build_static_wsdl(self, url):
        root = Element('{%s}definitions' % ns_wsdl, nsmap=_NS_MAP)
        root.set('targetNamespace', WSRP_WSDL_NAMESPACE)

        import_ = SubElement(root, 'import')
        import_.set('namespace', WSRP_BIND_NAMESPACE)
        import_.set('location', _WSRP_BIND_URL)

        service = SubElement(root, '{%s}service' % ns_wsdl)
        service.set('name', self.name)

        for name in ('ServiceDescription', 'Markup'):
            port = SubElement(service, '{%s}port' % ns_wsdl)
            port.set('name', _WSRP_SERVICE_NAME_TEMPLATE % name)
            port.set('binding', _WSRP_SERVICE_SOAP_BINDING_TEMPLATE % name)

            soap = SubElement(port, '{%s}address' % ns_soap)
            soap.set('location', url)

        self.__wsdl = tostring(root, xml_declaration=True, encoding="UTF-8")

        return self.__wsdl
