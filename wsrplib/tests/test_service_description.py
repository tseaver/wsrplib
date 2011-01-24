import unittest

class WSRP_v1_ServiceDescriptionTests(unittest.TestCase):

    def setUp(self):
        from zope.component.testing import setUp
        setUp()

    def tearDown(self):
        from zope.component.testing import tearDown
        tearDown()

    def _getTargetClass(self):
        from wsrplib.service_description import WSRP_v1_ServiceDescription
        return WSRP_v1_ServiceDescription

    def _makeOne(self):
        return self._getTargetClass()()

    def _getDescriptor(self, instance, name):
        method = getattr(instance, name)
        return method(clazz=self._getTargetClass(), _method_descriptor=1)

    def _registerServiceInfo(self, info):
        from zope.component import provideUtility
        from zope.interface import directlyProvides
        from wsrplib.interfaces import IServiceDescriptionInfo
        directlyProvides(info, IServiceDescriptionInfo)
        provideUtility(info, IServiceDescriptionInfo)

    def _registerPortlet(self, name, portlet):
        from zope.component import provideUtility
        from zope.interface import directlyProvides
        from wsrplib.interfaces import IPortlet
        directlyProvides(portlet, IPortlet)
        provideUtility(portlet, IPortlet, name)

    def test_get_tns(self):
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.get_tns(), WSRP_TYPES_NAMESPACE)

    def test_getServiceDescription_descriptor(self):
        from soaplib.core.service import MethodDescriptor
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

    def test_getServiceDescription_no_portlets(self):
        from wsrplib.datatypes import ServiceDescription
        instance = self._makeOne()
        reg_ctx = Dummy()
        locales = ['en-US', 'en']
        info = Dummy(requiresRegistration=False,
                     requiresInitCookie=False,
                     locales=['en'],
                    )
        self._registerServiceInfo(info)
        result = instance.getServiceDescription(reg_ctx, locales)
        self.failUnless(isinstance(result, ServiceDescription))
        self.assertEqual(result.requiresRegistration, False)
        self.assertEqual(result.requiresInitCookie, False)
        self.assertEqual(result.locales, ['en'])
        self.assertEqual(result.offeredPortlets, [])

    def test_getServiceDescription_w_portlets(self):
        from wsrplib.datatypes import ServiceDescription
        instance = self._makeOne()
        reg_ctx = Dummy()
        locales = ['en-US', 'en']
        info = Dummy(requiresRegistration=False,
                     requiresInitCookie=False,
                     locales=['en'],
                    )
        self._registerServiceInfo(info)
        m_type = Dummy(mimeType='text/plain',
                       modes=['wsrp:view'],
                       windowStates=['wsrp:normal'],
                       locales=['en'],
                      )
        p1 = Dummy(groupID='group',
                   title='Portlet 1',
                   shortTitle='P1',
                   displayName='P1 (display)',
                   description='P1 (description)',
                   keywords=['p1', 'kw1'],
                   markupTypes=[m_type],
                   userCategories=[],
                   userProfileItems=[],
                   usesMethodGet=False,
                   defaultMarkupSecure=False,
                   onlySecure=False,
                   userContextStoredInSession=False,
                   templatesStoredInSession=False,
                   hasUserSpecificState=False,
                   doesUrlTemplateProcessing=False,
                  )
        self._registerPortlet('p1', p1)
        p2 = Dummy(groupID='group',
                   title='Portlet 2',
                   shortTitle='P2',
                   displayName='P2 (display)',
                   description='P2 (description)',
                   keywords=['p2', 'kw1'],
                   markupTypes=[m_type],
                   userCategories=[],
                   userProfileItems=[],
                   usesMethodGet=False,
                   defaultMarkupSecure=False,
                   onlySecure=False,
                   userContextStoredInSession=False,
                   templatesStoredInSession=False,
                   hasUserSpecificState=False,
                   doesUrlTemplateProcessing=True,
                  )
        self._registerPortlet('p2', p2)
        result = instance.getServiceDescription(reg_ctx, locales)
        self.failUnless(isinstance(result, ServiceDescription))
        self.assertEqual(result.requiresRegistration, False)
        self.assertEqual(result.requiresInitCookie, False)
        self.assertEqual(result.locales, ['en'])
        portlets = sorted(result.offeredPortlets,
                          key=lambda x: x.portletHandle)
        self.assertEqual(len(portlets), 2)
        for index, portlet in enumerate(portlets):
            self.assertEqual(portlet.title.xmlLang, 'en')
            self.assertEqual(portlet.title.resourceName, 'title')
            self.assertEqual(portlet.title.value, 'Portlet %d' % (index + 1))


class Dummy(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)
