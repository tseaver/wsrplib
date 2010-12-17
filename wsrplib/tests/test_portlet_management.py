import unittest

class WSRP_v1_PortletManagementTests(unittest.TestCase):

    def _getTargetClass(self):
        from wsrplib.portlet_management import WSRP_v1_PortletManagement
        return WSRP_v1_PortletManagement

    def test_get_tns(self):
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.get_tns(), WSRP_TYPES_NAMESPACE)

    def _makeOne(self):
        return self._getTargetClass()()

    def _getDescriptor(self, instance, name):
        method = getattr(instance, name)
        return method(clazz=self._getTargetClass(), _method_descriptor=1)

    def test_getPortletDescription_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import PortletContext
        from wsrplib.datatypes import PortletDescriptionResponse
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import StringSeq
        from wsrplib.datatypes import UserContext
        from wsrplib.faults import AccessDenied
        from wsrplib.faults import InconsistentParameters
        from wsrplib.faults import InvalidHandle
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import InvalidUserCategory
        from wsrplib.faults import MissingParameters
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'getPortletDescription')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'getPortletDescription')
        self.assertEqual(descriptor.public_name, 'getPortletDescription')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'getPortletDescription')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 4)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is PortletContext)
        self.failUnless(in_message._type_info[2] is UserContext)
        self.failUnless(in_message._type_info[3] is StringSeq)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'getPortletDescriptionResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info,
                         PortletDescriptionResponse._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 7)
        self.failUnless(AccessDenied in faults)
        self.failUnless(InconsistentParameters in faults)
        self.failUnless(InvalidHandle in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(InvalidUserCategory in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_clonePortlet_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import PortletContext
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import UserContext
        from wsrplib.faults import AccessDenied
        from wsrplib.faults import InconsistentParameters
        from wsrplib.faults import InvalidHandle
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import InvalidUserCategory
        from wsrplib.faults import MissingParameters
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'clonePortlet')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'clonePortlet')
        self.assertEqual(descriptor.public_name, 'clonePortlet')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'clonePortlet')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 3)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is PortletContext)
        self.failUnless(in_message._type_info[2] is UserContext)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'clonePortletResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info,
                         PortletContext._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 7)
        self.failUnless(AccessDenied in faults)
        self.failUnless(InconsistentParameters in faults)
        self.failUnless(InvalidHandle in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(InvalidUserCategory in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_destroyPortlets_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import DestroyPortletsResponse
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import StringSeq
        from wsrplib.faults import InconsistentParameters
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import MissingParameters
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'destroyPortlets')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'destroyPortlets')
        self.assertEqual(descriptor.public_name, 'destroyPortlets')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'destroyPortlets')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 2)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is StringSeq)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'destroyPortletsResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info,
                         DestroyPortletsResponse._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 4)
        self.failUnless(InconsistentParameters in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_setPortletProperties_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import PortletContext
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import PropertyList
        from wsrplib.datatypes import UserContext
        from wsrplib.faults import AccessDenied
        from wsrplib.faults import InconsistentParameters
        from wsrplib.faults import InvalidHandle
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import InvalidUserCategory
        from wsrplib.faults import MissingParameters
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'setPortletProperties')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'setPortletProperties')
        self.assertEqual(descriptor.public_name, 'setPortletProperties')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'setPortletProperties')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 4)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is PortletContext)
        self.failUnless(in_message._type_info[2] is UserContext)
        self.failUnless(in_message._type_info[3] is PropertyList)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'setPortletPropertiesResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info,
                         PortletContext._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 7)
        self.failUnless(AccessDenied in faults)
        self.failUnless(InconsistentParameters in faults)
        self.failUnless(InvalidHandle in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(InvalidUserCategory in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_getPortletProperties_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import PortletContext
        from wsrplib.datatypes import PropertyList
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import StringSeq
        from wsrplib.datatypes import UserContext
        from wsrplib.faults import AccessDenied
        from wsrplib.faults import InconsistentParameters
        from wsrplib.faults import InvalidHandle
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import InvalidUserCategory
        from wsrplib.faults import MissingParameters
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'getPortletProperties')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'getPortletProperties')
        self.assertEqual(descriptor.public_name, 'getPortletProperties')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'getPortletProperties')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 4)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is PortletContext)
        self.failUnless(in_message._type_info[2] is UserContext)
        self.failUnless(in_message._type_info[3] is StringSeq)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'getPortletPropertiesResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info,
                         PropertyList._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 7)
        self.failUnless(AccessDenied in faults)
        self.failUnless(InconsistentParameters in faults)
        self.failUnless(InvalidHandle in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(InvalidUserCategory in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_getPortletPropertyDescription_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import PortletContext
        from wsrplib.datatypes import PortletPropertyDescriptionResponse
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import StringSeq
        from wsrplib.datatypes import UserContext
        from wsrplib.faults import AccessDenied
        from wsrplib.faults import InconsistentParameters
        from wsrplib.faults import InvalidHandle
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import InvalidUserCategory
        from wsrplib.faults import MissingParameters
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance,
                                         'getPortletPropertyDescription')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'getPortletPropertyDescription')
        self.assertEqual(descriptor.public_name,
                         'getPortletPropertyDescription')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__,
                         'getPortletPropertyDescription')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 4)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is PortletContext)
        self.failUnless(in_message._type_info[2] is UserContext)
        self.failUnless(in_message._type_info[3] is StringSeq)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'getPortletPropertyDescriptionResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info,
                         PortletPropertyDescriptionResponse._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 7)
        self.failUnless(AccessDenied in faults)
        self.failUnless(InconsistentParameters in faults)
        self.failUnless(InvalidHandle in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(InvalidUserCategory in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')
