from typing import IO
import wasm


class Parser:
    def __init__(self, stream):
        self.stream: IO = stream

        self.version: int = 0

    def parse(self):
        self.stream.seek(0)
        raw_bytes = self.stream.read()

        modules = iter(wasm.decode_module(raw_bytes))
        header, header_data = next(modules)

        self.version = header.version
        print(header.version.to_string())

        for current_section in modules:
            print(current_section)
