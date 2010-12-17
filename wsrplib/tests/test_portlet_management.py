import unittest

class WSRP_v1_PortletManagementTests(unittest.TestCase):

    def _getTargetClass(self):
        from wsrplib._portlet_management import WSRP_v1_PortletManagement
        return WSRP_v1_PortletManagement

    def test_get_tns(self):
        from wsrplib._namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.get_tns(), WSRP_TYPES_NAMESPACE)

