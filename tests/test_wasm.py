from phantasm.parse.construct import *

if __name__ == '__main__':
    with open('add.wasm', 'rb') as f:
        struct = Struct('modules',
                        Const('magic', b'\x00asm'),
                        FixedUInt('version', 4),
                        Struct(
                            'typesec',
                            Const('N', b'\x01'),
                            ULEB128('size', 32),
                        ))
        print(struct.check(f))
