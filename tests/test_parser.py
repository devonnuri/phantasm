from phantasm import Parser

if __name__ == '__main__':
    with open('add.wasm', 'rb') as f:
        parser = Parser(f)
        print(parser.parse())
