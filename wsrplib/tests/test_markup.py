import unittest

class WSRP_v1_MarkupTests(unittest.TestCase):

    def _getTargetClass(self):
        from wsrplib._markup import WSRP_v1_Markup
        return WSRP_v1_Markup

    def test_get_tns(self):
        from wsrplib._namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.get_tns(), WSRP_TYPES_NAMESPACE)

