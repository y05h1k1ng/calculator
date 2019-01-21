from parse import Parser
def main():
    print('Hello!')

    while True:
        source = input('>>')
        source = source.replace(' ', '')
        source = source.strip()

        if source == 'q':
            print('Goodbye!')
            break
        elif len(source) == 0:
            continue
        
        ast = Parser(source).parse()

        print(ast.getValue())


if __name__ == "__main__":
    main()