from phantasm.parse.construct import *
from io import BytesIO

if __name__ == '__main__':
    stream = BytesIO(b'helloworld')

    struct = Struct('test_struct',
                    Const('magic', b'hell'),
                    Optional(Const('magic2', b'ooo')),
                    Optional(Const('a', b'ooo')),
                    Optional(Const('b', b'ooo')),
                    Optional(Const('c', b'ooo')),
                    Optional(Const('d', b'ooo')),
                    Optional(Const('e', b'ooo')),
                    Const('magic3', b'owo'))
    print(struct.check(stream))
