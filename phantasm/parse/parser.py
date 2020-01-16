from typing import IO
import phantasm.wasm as wasm


class Parser:
    def __init__(self, stream):
        self.stream: IO = stream

        self.version: int = 0

    def parse(self):
        self.stream.seek(0)
        raw_bytes = self.stream.read()

        modules = iter(wasm.decode_module(raw_bytes))
        header, header_data = next(modules)
        print(header.to_string(header_data))

        for section, section_data in modules:
            print(section.to_string(section_data))
