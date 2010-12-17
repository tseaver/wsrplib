from soaplib.model.exception import Fault

from wsrplib.namespaces import WSRP_TYPES_NAMESPACE

class _WSRPFault(Fault):
    __namespace__ = WSRP_TYPES_NAMESPACE

    @classmethod
    def get_type_name(cls):
        return cls.__name__

class AccessDenied(_WSRPFault):
    pass

class InvalidUserCategory(_WSRPFault):
    pass

class InconsistentParameters(_WSRPFault):
    pass

class InvalidRegistration(_WSRPFault):
    pass

class MissingParameters(_WSRPFault):
    pass

class OperationFailed(_WSRPFault):
    pass

class InvalidHandle(_WSRPFault):
    pass

class PortletStateChangeRequired(_WSRPFault):
    pass

class InvalidCookie(_WSRPFault):
    pass

class InvalidSession(_WSRPFault):
    pass

class UnsupportedMode(_WSRPFault):
    pass

class UnsupportedWindowState(_WSRPFault):
    pass

class UnsupportedLocale(_WSRPFault):
    pass

class UnsupportedMimeType(_WSRPFault):
    pass
