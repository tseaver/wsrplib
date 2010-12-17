import unittest

class WSRP_v1_ServiceDescriptionTests(unittest.TestCase):

    def _getTargetClass(self):
        from wsrplib._service_description import WSRP_v1_ServiceDescription
        return WSRP_v1_ServiceDescription

    def test_get_tns(self):
        from wsrplib._namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.get_tns(), WSRP_TYPES_NAMESPACE)
