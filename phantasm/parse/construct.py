from typing import IO, Optional as _Optional
from enum import Enum
import struct
import math


class Endian(Enum):
    BIG = '>'
    LITTLE = '<'

    def __init__(self, order_character):
        self._order_character = order_character

    @property
    def order_character(self):
        return self._order_character


class Node:
    def __init__(self, name: _Optional[str]):
        self.name = name
        self.last_pos = None

    def check(self, stream: IO):
        self.last_pos = stream.tell()
        return self._check(stream)

    def _check(self, stream: IO):
        raise NotImplementedError('\'check\' method should be implemented')

    def rollback(self, stream: IO):
        stream.seek(stream.tell() - self.last_pos, 1)


class Struct(Node):
    def __init__(self, name: _Optional[str], *args: Node):
        super().__init__(name)

        self.children = args
        if name == 'functype':
            print(self.children)

    def _check(self, stream: IO):
        result = {}
        for child in self.children:
            child_result = child.check(stream)
            if child.name:
                result[child.name] = child_result
        return result


class Array(Node):
    def __init__(self, name: _Optional[str], node: Node, count: int):
        super().__init__(name)

        self.count = count
        self.node = node

    def _check(self, stream: IO):
        result = []
        for i in range(self.count):
            result.append(self.node.__class__(None).check(stream))
        return result


class Const(Node):
    def __init__(self, name: _Optional[str], value: bytes):
        super().__init__(name)

        self.value = value

    def _check(self, stream: IO):
        if stream.read(len(self.value)) == self.value:
            return self.value
        return None


class NativeStruct(Node):
    def __init__(self, name: _Optional[str], count: int, endian: Endian, format_character: str):
        super().__init__(name)

        self.count = count self.endian = endian
        self.format_character = format_character

    def _check(self, stream: IO):
        data = stream.read(self.count)
        try:
            value, = struct.unpack(self.endian.order_character + self.format_character, data)
        except struct.error:
            return None
        return value


class FixedUInt(NativeStruct):
    def __init__(self, name: _Optional[str], count: int, endian: Endian = Endian.LITTLE):
        super().__init__(name, count, endian, 'I')


class FixedInt(NativeStruct):
    def __init__(self, name: _Optional[str], count: int, endian: Endian = Endian.LITTLE):
        super().__init__(name, count, endian, 'i')


class ULEB128(Node):
    def __init__(self, name: _Optional[str], bits: int):
        super().__init__(name)

        self.length = math.ceil(bits / 7)

    def _check(self, stream: IO):
        value = 0
        for i in range(self.length):
            b = stream.read(1)[0]
            tmp = b & 0x7f
            value = tmp << (i * 7) | value
            if (b & 0x80) != 0x80:
                break
        return value


class LEB128(Node):
    def __init__(self, name: _Optional[str], bits: int):
        super().__init__(name)

        self.length = math.ceil(bits / 7)

    def _check(self, stream: IO):
        mask = [0xffffff80, 0xffffc000, 0xffe00000, 0xf0000000, 0]
        bitmask = [0x40, 0x40, 0x40, 0x40, 0x8]
        value = 0
        for i in range(self.length):
            b = stream.read(1)[0]
            tmp = b & 0x7f
            value = tmp << (i * 7) | value
            if (b & 0x80) != 0x80:
                if bitmask[i] & tmp:
                    value |= mask[i]
                break
        buffer = struct.pack("I", value)
        value, = struct.unpack("i", buffer)
        return value


class Optional(Node):
    def __init__(self, child: Node):
        super().__init__(child.name)

        self.child = child

    def _check(self, stream: IO):
        result = self.child.check(stream)
        if result is None:
            stream.seek(self.last_pos - stream.tell(), 1)
        return result

