from AST import OpAST, NumberAST, NameAST, CallAST, DefAST, VARS

class Parser():
    def __init__(self, source):
        self.source = source
        self.p = 0

    def parse(self):
        n = self.define()
        if n:
            return n
        self.p = 0
        return self.expr()

    def expr(self):
        return self.add()

    def define(self):
        n = self.name()
        if self.isnext('='):
            self.next()
            n2 = self.expr()

            return DefAST(n.getValue(), n2)
        
        return None

    def add(self):
        n1 = self.sub()
        if self.isnext('+'):
            self.next()
            n2 = self.add()

            return OpAST('+', [n1, n2])
        
        return n1
    
    def sub(self):
        n1 = self.mul()
        if self.isnext('-'):
            self.next()
            n2 = self.sub()

            return OpAST('-', [n1, n2])
        
        return n1
    def mul(self):
        n1 = self.div()
        if self.isnext('*'):
            self.next()
            n2 = self.mul()

            return OpAST('*', [n1, n2])
        
        return n1
    
    def div(self):
        n1 = self.ddiv()
        if self.isnext('/'):
            self.next()
            n2 = self.div()

            return OpAST('/', [n1, n2])
        
        return n1
    
    def ddiv(self):
        n1 = self.call()
        if self.isnext('%'):
            self.next()
            n2 = self.ddiv()

            return OpAST('%', [n1, n2])
        
        return n1
    
    def call(self):
        n = self.name()
        if not n:
            return self.factor()
        
        if self.isnext('('):
            self.next()
            arg = self.expr()
            if not self.isnext(')'):
                raise Exception('Error')
            self.next()
            
            return CallAST(n, arg)
        
        return n

    def factor(self):
        n = self.name()
        if n:
            return n

        n = self.number()
        if n:
            return n

        return None

    def name(self):
        c = self.get()
        s = ""
        while not self.isend():
            c = self.get()
            if not c.isalpha():
                break
            s += c
            self.next()
        
        if not s:
            return None
        
        return NameAST(s)
    
    def number(self):
        c = self.get()
        if c == '0':
            return NumberAST(0)
        
        s = ""
        while not self.isend():
            c = self.get()
            if  not ord('0') <= ord(c) <= ord('9'):
                break
            s += c
            self.next()

        if not s:
            return None
        
        return NumberAST( int(s) )
        
    def isend(self):
         return self.p >= len(self.source)

    def get(self):
        return self.source[self.p]

    def isnext(self, s):
        return self.source[self.p:self.p + len(s)] == s

    def next(self):
        self.p += 1

if __name__ == "__main__":
    ast = Parser("x=sin(3)").parse()
    ast2 = Parser("4*x").parse()

    print(ast)
    print(ast.getValue())
    print(VARS)
    print(ast2)
    print(ast2.getValue())
