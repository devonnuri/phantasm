from typing import Optional
from phantasm.parse.construct import ULEB128, LEB128, NativeStruct, Endian, Node, Array


class U8(ULEB128):
    def __init__(self, name: Optional[str]):
        super().__init__(name, 8)


class U16(ULEB128):
    def __init__(self, name: Optional[str]):
        super().__init__(name, 16)


class U32(ULEB128):
    def __init__(self, name: Optional[str]):
        super().__init__(name, 32)


class U64(ULEB128):
    def __init__(self, name: Optional[str]):
        super().__init__(name, 64)


class S8(LEB128):
    def __init__(self, name: Optional[str]):
        super().__init__(name, 8)


class S16(LEB128):
    def __init__(self, name: Optional[str]):
        super().__init__(name, 16)


class S32(LEB128):
    def __init__(self, name: Optional[str]):
        super().__init__(name, 32)


class S64(LEB128):
    def __init__(self, name: Optional[str]):
        super().__init__(name, 64)


class F16(NativeStruct):
    def __init__(self, name: Optional[str], count: int, endian: Endian = Endian.LITTLE):
        super().__init__(name, count, endian, 'e')


class F32(NativeStruct):
    def __init__(self, name: Optional[str], count: int, endian: Endian = Endian.LITTLE):
        super().__init__(name, count, endian, 'f')


class F64(NativeStruct):
    def __init__(self, name: Optional[str], count: int, endian: Endian = Endian.LITTLE):
        super().__init__(name, count, endian, 'd')


class ValType(Node):
    i32 = 0
    i64 = 1
    f32 = 2
    f64 = 3

    def __init__(self, name: Optional[str]):
        super().__init__(name)

    def _check(self, stream):
        b = stream.read(1)
        return {
            'i32': ValType.i32,
            'i64': ValType.i64,
            'f32': ValType.f32,
            'f64': ValType.f64
        }.get(b, None)


class Vec(Node):
    def __init__(self, name: Optional[str], B: Node):
        super().__init__(name)

        self.B = B

    def _check(self, stream):
        n = U32('n').check(stream)
        x = Array('n', self.B, n).check(stream)

        return x

