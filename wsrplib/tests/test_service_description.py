import unittest

class WSRP_v1_ServiceDescriptionTests(unittest.TestCase):

    def _getTargetClass(self):
        from wsrplib.service_description import WSRP_v1_ServiceDescription
        return WSRP_v1_ServiceDescription

    def _makeOne(self):
        return self._getTargetClass()()

    def _getDescriptor(self, instance, name):
        method = getattr(instance, name)
        return method(clazz=self._getTargetClass(), _method_descriptor=1)

    def test_get_tns(self):
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.get_tns(), WSRP_TYPES_NAMESPACE)

    def test_getServiceDescription_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import ServiceDescription
        from wsrplib.datatypes import StringSeq
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'getServiceDescription')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'getServiceDescription')
        self.assertEqual(descriptor.public_name, 'getServiceDescription')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'getServiceDescription')
        self.assertEqual(in_message.__namespace__, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 2)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is StringSeq)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'getServiceDescriptionResponse')
        self.assertEqual(out_message.__namespace__, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info, ServiceDescription._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 2)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')
