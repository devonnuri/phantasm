from typing import IO

from phantasm.parse.construct import Struct, Const, FixedUInt
from phantasm.parse.wasmstructs import U32, Vec, ValType
from phantasm.utils.exceptions import wasm_assert


class Parser:
    def __init__(self, stream):
        self.stream: IO = stream

        self.version: int = 0

    def parse(self):
        self.stream.seek(0)

        struct = Struct('modules',
                        Const('magic', b'\x00asm'),
                        FixedUInt('version', 4),
                        Struct(
                            'typesec',
                            Const('N', b'\x01'),
                            U32('size'),
                            Vec('functypes',
                                Struct('functype',
                                       Const(None, b'\x60'),
                                       Vec('t1', ValType),
                                       Vec('t2', ValType)))
                        ))

        result = struct.check(self.stream)

        wasm_assert(result['magic'], 'Incorrect magic number')

        return result
