from lxml.etree import Comment
from lxml.etree import Element
from lxml.etree import SubElement
from lxml.etree import tostring
from soaplib import Application as _Application
from soaplib import ns_wsdl
from soaplib import ns_soap
from soaplib.core.wsdl import WSDL

from wsrplib.namespaces import WSRP_BIND_NAMESPACE
from wsrplib.namespaces import WSRP_INTF_NAMESPACE
from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
from wsrplib.namespaces import WSRP_WSDL_NAMESPACE

#_WSRP_BASE_URL = 'http://www.oasis-open.org/committees/wsrp/specifications'
#_WSRP_BIND_URL = '%s/version1/wsrp_v1_bindings.wsdl' % _WSRP_BASE_URL
_WSRP_BIND_URL = '/static/wsrp_v1_bindings.wsdl'
_WSRP_SERVICE_NAME_TEMPLATE = 'WSRP_v1_%s'
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

class WSRP_WSDL(WSDL):

    def _get_binding_name(self, port_type_name):
        if port_type_name.endswith('_PortType'):
            return '%s_Binding_SOAP' % port_type_name[:-len('_PortType')]

    def _get_port_name(self, port_type_name):
        if port_type_name.endswith('_PortType'):
            return port_type_name[:-len('_PortType')]

class Application(_Application):

    __name = 'WSRP_v1_Service_Service'

    def __init__(self, services, tns, name=None,
                 _with_partnerlink=False,
                 _wsdl_generation=None,
                 _endpoint_url=None,
                ):
        super(Application, self).__init__(services, tns, name,
                                          _with_partnerlink,
                                         )
        self._wsdl_generation = _wsdl_generation
        self._endpoint_url = _endpoint_url
        for prefix, namespace in _NS_MAP.items():
            if prefix is not None:
                self.set_namespace_prefix(namespace, prefix)

        # Rebuild after updating namespaces.
        self.call_routes = {}
        self.build_schema()

    def _WSDL_factory(self):
        return WSRP_WSDL

    def get_wsdl(self, url):
        """ Override to import standard WSDL rather than introspect.
        """
        if self._endpoint_url is not None:
            url = self._endpoint_url

        if self._wsdl_generation == 'dynamic':
            return self._build_dynamic_wsdl(url)

        if self._wsdl_generation == 'static':
            return self._build_static_wsdl(url)

        return super(Application, self).get_wsdl(url)

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
        root = Element("{%s}definitions" % ns_wsdl, nsmap=self.nsmap)
        root.set('targetNamespace', WSRP_WSDL_NAMESPACE)

        root.append(Comment('Begin WSRP 1.0 types'))
        types = SubElement(root, "{%s}types" % ns_wsdl)
        self.build_schema(types)
        root.append(Comment('End WSRP 1.0 types'))

        root.append(Comment('Begin WSRP 1.0 messages'))
        seen = set()
        # XXX faults?
        for name, inst in services.items():
            inst.add_messages_for_methods(self, root, seen)
        root.append(Comment('End WSRP 1.0 messages'))

        port_types = {}
        root.append(Comment('Begin WSRP 1.0 port types'))
        for name, inst in services.items():
            port_type = SubElement(root, '{%s}portType' % ns_wsdl)
            pt_name = port_types[name] = '%s_PortType' % name
            port_type.set('name', pt_name)
            # Ripped off from soaplib.service.DescriptionBase.add_port_type
            for method in inst.public_methods:
                operation = SubElement(port_type,'{%s}operation'% ns_wsdl)
                operation.set('name', method.name)

                if method.doc is not None:
                    documentation = SubElement(operation,
                                               '{%s}documentation' % ns_wsdl)
                    documentation.text = method.doc

                # XXX:  WSRP's WSDL does not have this attribute!
                #operation.set('parameterOrder',
                #              method.in_message.get_type_name())

                # Our messages are defined in *our* namespace, not the
                # namespace of the service ('types:'), and hence don't need
                # qualification.
                op_input = SubElement(operation, '{%s}input' % ns_wsdl)
                op_input.set('name', method.in_message.get_type_name())
                #op_input.set('message',
                #             method.in_message.get_type_name_ns(app))
                op_input.set('message', method.in_message.get_type_name())

                op_output = SubElement(operation, '{%s}output' %  ns_wsdl)
                op_output.set('name', method.out_message.get_type_name())
                #op_output.set('message',
                #              method.out_message.get_type_name_ns(app))
                op_output.set('message', method.out_message.get_type_name())

                for f in method.faults:
                    fault = SubElement(operation, '{%s}fault' %  ns_wsdl)
                    fault.set('name', f.get_type_name())
                    fault.set('message', f.get_type_name())

        root.append(Comment('End WSRP 1.0 port types'))

        root.append(Comment('Begin WSRP 1.0 bindings'))
        for name, inst in services.items():
            binding = SubElement(root, '{%s}binding' % ns_wsdl)
            binding.set('name', '%s_Binding_SOAP' % name)
            binding.set('type', port_types[name])

            soap_binding = SubElement(binding, '{%s}binding' % ns_soap)
            soap_binding.set('style', 'document')

            if self.transport is None:
                raise Exception("You must set the 'transport' property")
            soap_binding.set('transport', self.transport)

            inst.add_bindings_for_methods(self, root, name, types, url,
                                          binding, None)

        root.append(Comment('End WSRP 1.0 bindings'))

        root.append(Comment('Begin WSRP 1.0 services'))
        service = SubElement(root, '{%s}service' % ns_wsdl)
        service.set('name', '%s_Service' % self.name)
        for name, inst in services.items():
            wsdl_port = SubElement(service, '{%s}port' % ns_wsdl)
            wsdl_port.set('name', name)
            wsdl_port.set('binding', '%s_Binding_SOAP' % name)

            addr = SubElement(wsdl_port, '{%s}address' % ns_soap)
            addr.set('location', url)

        root.append(Comment('End WSRP 1.0 services'))

        self.__wsdl = tostring(root, xml_declaration=True, encoding="UTF-8")

        return self.__wsdl

    def _build_static_wsdl(self, url):
        root = Element('{%s}definitions' % ns_wsdl, nsmap=_NS_MAP)
        root.set('targetNamespace', WSRP_WSDL_NAMESPACE)

        import_ = SubElement(root, 'import')
        import_.set('namespace', WSRP_BIND_NAMESPACE)
        import_.set('location', _WSRP_BIND_URL)
        service = SubElement(root, '{%s}service' % ns_wsdl)
        service.set('name', self.name)

        for name in ('ServiceDescription',
                     'Markup',
                     'PortletManagement',
                     'Registration',
                    ):

            port = SubElement(service, '{%s}port' % ns_wsdl)
            port.set('name', _WSRP_SERVICE_NAME_TEMPLATE % name)
            port.set('binding', _WSRP_SERVICE_SOAP_BINDING_TEMPLATE % name)

            soap = SubElement(port, '{%s}address' % ns_soap)
            soap.set('location', url)

        self.__wsdl = tostring(root, xml_declaration=True, encoding="UTF-8")

        return self.__wsdl
