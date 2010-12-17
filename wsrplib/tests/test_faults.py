import unittest


class _ByName(unittest.TestCase):
    @classmethod
    def _getTargetClass(cls):
        name = cls.__name__
        assert name.endswith('Tests')
        name = name[:-len('Tests')]
        module = __import__('wsrplib.faults', fromlist=[name])
        return getattr(module, name)


class _API(object):
    # Test that the (declarative) datatype classes can be imported.
    def test_API_importable(self):
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.__namespace__, WSRP_TYPES_NAMESPACE)


class AccessDeniedTests(_ByName, _API):
    pass


class InvalidUserCategoryTests(_ByName, _API):
    pass


class InconsistentParametersTests(_ByName, _API):
    pass


class InvalidRegistrationTests(_ByName, _API):
    pass


class MissingParametersTests(_ByName, _API):
    pass


class OperationFailedTests(_ByName, _API):
    pass


class InvalidHandleTests(_ByName, _API):
    pass


class PortletStateChangeRequiredTests(_ByName, _API):
    pass


class InvalidCookieTests(_ByName, _API):
    pass


class InvalidSessionTests(_ByName, _API):
    pass


class UnsupportedModeTests(_ByName, _API):
    pass


class UnsupportedWindowStateTests(_ByName, _API):
    pass


class UnsupportedLocaleTests(_ByName, _API):
    pass


class UnsupportedMimeTypeTests(_ByName, _API):
    pass
