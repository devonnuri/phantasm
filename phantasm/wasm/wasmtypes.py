"""Defines types used for both modules and bytecode."""
from .types import UIntNField, UnsignedLeb128Field, SignedLeb128Field


def _make_shortcut(klass, *args, **kwargs):
    def proxy(**kwargs2):
        kwargs.update(kwargs2)
        return klass(*args, **kwargs)
    return proxy


UInt8Field = _make_shortcut(UIntNField, 8)
UInt16Field = _make_shortcut(UIntNField, 16)
UInt32Field = _make_shortcut(UIntNField, 32)
UInt64Field = _make_shortcut(UIntNField, 64)

VarUInt1Field = _make_shortcut(UnsignedLeb128Field)
VarUInt7Field = _make_shortcut(UnsignedLeb128Field)
VarUInt32Field = _make_shortcut(UnsignedLeb128Field)

VarInt7Field = _make_shortcut(SignedLeb128Field)
VarInt32Field = _make_shortcut(SignedLeb128Field)
VarInt64Field = _make_shortcut(SignedLeb128Field)

ElementTypeField = VarInt7Field
ValueTypeField = VarInt7Field
ExternalKindField = UInt8Field
BlockTypeField = VarInt7Field


class SectionType:
    UNKNOWN = 0
    TYPE = 1
    IMPORT = 2
    FUNCTION = 3
    TABLE = 4
    MEMORY = 5
    GLOBAL = 6
    EXPORT = 7
    START = 8
    ELEMENT = 9
    CODE = 10
    DATA = 11
    NAME = b'name'


class LangType:
    I32 = -0x01
    I64 = -0x02
    F32 = -0x03
    F64 = -0x04
    ANYFUNC = -0x10
    FUNC = -0x20
    EMPTY = -0x40


class ValueType:
    I32 = LangType.I32
    I64 = LangType.I64
    F32 = LangType.F32
    F64 = LangType.F64


class NameSubSectionType:
    FUNCTION = 1
    LOCAL = 2


class Mutability:
    IMMUTABLE = 0
    MUTABLE = 1
