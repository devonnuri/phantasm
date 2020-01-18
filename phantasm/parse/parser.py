from typing import IO
import phantasm.wasm as wasm
from phantasm.wasm.wasmtypes import SectionType


class Parser:
    def __init__(self, stream):
        self.stream: IO = stream

        self.version: int = 0

    def parse(self):
        self.stream.seek(0)
        raw_bytes = self.stream.read()

        modules = iter(wasm.decode_module(raw_bytes))
        header = next(modules)

        for section, section_data in modules:
            if section_data.id == SectionType.CODE:
                print(section.to_string(section_data))
                for a in wasm.decode_bytecode(section_data.payload.bodies[1].code.tobytes()):
                    print(a)
