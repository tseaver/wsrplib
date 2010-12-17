import unittest

class WSRP_v1_RegistrationTests(unittest.TestCase):

    def _getTargetClass(self):
        from wsrplib._registration import WSRP_v1_Registration
        return WSRP_v1_Registration

    def test_get_tns(self):
        from wsrplib._namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.get_tns(), WSRP_TYPES_NAMESPACE)


