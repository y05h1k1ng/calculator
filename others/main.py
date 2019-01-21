from parse import Parser
def main():
    print('Hello!')

    while True:
        source = input('>>')

        if source == 'q':
            print('Goodbye!')
            break

        source = source.replace(' ', '')
        ast = Parser(source).parse()

        print(ast.getValue())


if __name__ == "__main__":
    main()