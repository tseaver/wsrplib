import unittest

class WSRP_v1_RegistrationTests(unittest.TestCase):

    def _getTargetClass(self):
        from wsrplib.registration import WSRP_v1_Registration
        return WSRP_v1_Registration

    def _makeOne(self):
        return self._getTargetClass()()

    def _getDescriptor(self, instance, name):
        method = getattr(instance, name)
        return method(clazz=self._getTargetClass(), _method_descriptor=1)

    def test_get_tns(self):
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.get_tns(), WSRP_TYPES_NAMESPACE)

    def test_register_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import RegistrationData
        from wsrplib.faults import MissingParameters
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'register')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'register')
        self.assertEqual(descriptor.public_name, 'register')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'register')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 1)
        self.failUnless(in_message._type_info[0] is RegistrationData)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'registerResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info,
                         RegistrationContext._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 2)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_modifyRegistration_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import RegistrationData
        from wsrplib.datatypes import RegistrationState
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import MissingParameters
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'modifyRegistration')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'modifyRegistration')
        self.assertEqual(descriptor.public_name, 'modifyRegistration')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'modifyRegistration')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 2)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is RegistrationData)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'modifyRegistrationResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info,
                         RegistrationState._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 3)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_deregister_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'deregister')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'deregister')
        self.assertEqual(descriptor.public_name, 'deregister')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'deregister')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 1)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'deregisterResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(out_message._type_info), 0)
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
