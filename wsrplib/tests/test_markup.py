import unittest

class WSRP_v1_MarkupTests(unittest.TestCase):

    def _getTargetClass(self):
        from wsrplib.markup import WSRP_v1_Markup
        return WSRP_v1_Markup

    def _makeOne(self):
        return self._getTargetClass()()

    def _getDescriptor(self, instance, name):
        method = getattr(instance, name)
        return method(clazz=self._getTargetClass(), _method_descriptor=1)

    def test_get_tns(self):
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.get_tns(), WSRP_TYPES_NAMESPACE)

    def test_getMarkup_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import MarkupParams
        from wsrplib.datatypes import MarkupResponse
        from wsrplib.datatypes import PortletContext
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import RuntimeContext
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
        from wsrplib.faults import UnsupportedLocale
        from wsrplib.faults import UnsupportedMimeType
        from wsrplib.faults import UnsupportedMode
        from wsrplib.faults import UnsupportedWindowState
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'getMarkup')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'getMarkup')
        self.assertEqual(descriptor.public_name, 'getMarkup')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'getMarkup')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 5)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is PortletContext)
        self.failUnless(in_message._type_info[2] is RuntimeContext)
        self.failUnless(in_message._type_info[3] is UserContext)
        self.failUnless(in_message._type_info[4] is MarkupParams)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'getMarkupResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info, MarkupResponse._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 13)
        self.failUnless(AccessDenied in faults)
        self.failUnless(InconsistentParameters in faults)
        self.failUnless(InvalidCookie in faults)
        self.failUnless(InvalidHandle in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(InvalidSession in faults)
        self.failUnless(InvalidUserCategory in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.failUnless(UnsupportedLocale in faults)
        self.failUnless(UnsupportedMimeType in faults)
        self.failUnless(UnsupportedMode in faults)
        self.failUnless(UnsupportedWindowState in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_performBlockingInteraction_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import BlockingInteractionResponse
        from wsrplib.datatypes import InteractionParams
        from wsrplib.datatypes import MarkupParams
        from wsrplib.datatypes import PortletContext
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import RuntimeContext
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
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'performBlockingInteraction')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'performBlockingInteraction')
        self.assertEqual(descriptor.public_name, 'performBlockingInteraction')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'performBlockingInteraction')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 6)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is PortletContext)
        self.failUnless(in_message._type_info[2] is RuntimeContext)
        self.failUnless(in_message._type_info[3] is UserContext)
        self.failUnless(in_message._type_info[4] is MarkupParams)
        self.failUnless(in_message._type_info[5] is InteractionParams)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'performBlockingInteractionResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(out_message._type_info,
                         BlockingInteractionResponse._type_info)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 14)
        self.failUnless(AccessDenied in faults)
        self.failUnless(InconsistentParameters in faults)
        self.failUnless(InvalidCookie in faults)
        self.failUnless(InvalidHandle in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(InvalidSession in faults)
        self.failUnless(InvalidUserCategory in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.failUnless(PortletStateChangeRequired in faults)
        self.failUnless(UnsupportedLocale in faults)
        self.failUnless(UnsupportedMimeType in faults)
        self.failUnless(UnsupportedMode in faults)
        self.failUnless(UnsupportedWindowState in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_initCookie_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.faults import AccessDenied
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'initCookie')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'initCookie')
        self.assertEqual(descriptor.public_name, 'initCookie')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'initCookie')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 1)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'initCookieResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(out_message._type_info), 0)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 3)
        self.failUnless(AccessDenied in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')

    def test_releaseSessions_descriptor(self):
        from soaplib.service import MethodDescriptor
        from wsrplib.datatypes import RegistrationContext
        from wsrplib.datatypes import StringSeq
        from wsrplib.faults import AccessDenied
        from wsrplib.faults import InvalidRegistration
        from wsrplib.faults import MissingParameters
        from wsrplib.faults import OperationFailed
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        instance = self._makeOne()
        descriptor = self._getDescriptor(instance, 'releaseSessions')
        self.failUnless(isinstance(descriptor, MethodDescriptor))
        self.assertEqual(descriptor.name, 'releaseSessions')
        self.assertEqual(descriptor.public_name, 'releaseSessions')
        in_message = descriptor.in_message
        self.assertEqual(in_message.__type_name__, 'releaseSessions')
        self.assertEqual(in_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(in_message._type_info), 2)
        self.failUnless(in_message._type_info[0] is RegistrationContext)
        self.failUnless(in_message._type_info[1] is StringSeq)
        out_message = descriptor.out_message
        self.assertEqual(out_message.__type_name__,
                         'releaseSessionsResponse')
        self.assertEqual(out_message.namespace, WSRP_TYPES_NAMESPACE)
        self.assertEqual(len(out_message._type_info), 0)
        self.failUnless('WSRP' in descriptor.doc)
        self.failIf(descriptor.is_callback)
        self.failIf(descriptor.is_async)
        self.failIf(descriptor.mtom)
        self.assertEqual(descriptor.in_header, None)
        self.assertEqual(descriptor.out_header, None)
        faults = descriptor.faults
        self.assertEqual(len(faults), 4)
        self.failUnless(AccessDenied in faults)
        self.failUnless(InvalidRegistration in faults)
        self.failUnless(MissingParameters in faults)
        self.failUnless(OperationFailed in faults)
        self.assertEqual(descriptor.body_style, 'document')
