import unittest


class _ByName(unittest.TestCase):
    @classmethod
    def _getTargetClass(cls, suffix=None):
        name = cls.__name__
        assert name.endswith('Tests')
        name = name[:-len('Tests')]
        if suffix is not None:
            name += suffix
        module = __import__('wsrplib.datatypes', fromlist=[name])
        return getattr(module, name)


class _API(object):
    # Test that the (declarative) datatype classes can be imported.
    def test_API_importable(self):
        from wsrplib.namespaces import WSRP_TYPES_NAMESPACE
        cls = self._getTargetClass()
        self.assertEqual(cls.__namespace__, WSRP_TYPES_NAMESPACE)


class _Seq(object):
    # Test that the sequence type for the base datatype can be imported.
    def test_API_importable_as_sequence(self):
        self._getTargetClass(suffix='Seq')


class _NotNillable(object):
    # Test that the "not-nil" type for the base datatype can be imported.
    def test_API_importable_as_sequence(self):
        self._getTargetClass(suffix='NotNillable')


class HandleTests(_ByName, _API):
    pass


class KeyTests(_ByName, _API):
    pass


class IDTests(_ByName, _API):
    pass


class LocalizedStringTests(_ByName, _API, _Seq):
    pass


class ResourceValueTests(_ByName, _API, _Seq):
    pass


class ResourceTests(_ByName, _API, _Seq):
    pass


class ResourceListTests(_ByName, _API, _NotNillable):
    pass


class ItemDescriptionTests(_ByName, _API, _Seq):
    pass


class MarkupTypeTests(_ByName, _API, _Seq):
    pass


class PortletDescriptionTests(_ByName, _API, _Seq):
    pass


class PropertyTests(_ByName, _API, _Seq):
    pass


class ResetPropertyTests(_ByName, _API, _Seq):
    pass


class PropertyListTests(_ByName, _API):
    pass


class PropertyDescriptionTests(_ByName, _API, _Seq):
    pass


class ModelTypesTests(_ByName, _API):
    pass


class ModelDescriptionTests(_ByName, _API, _NotNillable):
    pass


class CookieProtocolTests(_ByName, _API):
    pass


class ServiceDescriptionTests(_ByName, _API):
    pass


class RegistrationStateTests(_ByName, _API):
    pass


class RegistrationContextTests(_ByName, _API):
    pass


class SessionContextTests(_ByName, _API):
    pass


class TemplatesTests(_ByName, _API):
    pass


class RuntimeContextTests(_ByName, _API):
    pass


class PortletContextTests(_ByName, _API):
    pass


class CacheControlTests(_ByName, _API):
    pass


class ClientDataTests(_ByName, _API):
    pass


class NamedStringTests(_ByName, _API):
    pass


class MarkupParamsTests(_ByName, _API):
    pass


class MarkupContextTests(_ByName, _API):
    pass


class MarkupResponseTests(_ByName, _API):
    pass


class UpdateResponseTests(_ByName, _API):
    pass


class BlockingInteractionResponseTests(_ByName, _API):
    pass


class UploadContextTests(_ByName, _API):
    pass


class InteractionParamsTests(_ByName, _API):
    pass


class PersonNameTests(_ByName, _API):
    pass


class EmployerInfoTests(_ByName, _API):
    pass


class TelephoneNumTests(_ByName, _API):
    pass


class TelecomTests(_ByName, _API):
    pass


class OnlineTests(_ByName, _API):
    pass


class PostalTests(_ByName, _API):
    pass


class ContactTests(_ByName, _API):
    pass


class UserProfileTests(_ByName, _API):
    pass


class UserContextTests(_ByName, _API):
    pass


class RegistrationDataTests(_ByName, _API):
    pass


class DestroyFailedTests(_ByName, _API):
    pass


class DestroyPortletsResponseTests(_ByName, _API):
    pass


class PortletDescriptionResponseTests(_ByName, _API):
    pass


class PortletPropertyDescriptionResponseTests(_ByName, _API):
    pass

