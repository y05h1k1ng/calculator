import math

VARS = {}

class AST():
    def getValue(self):
        pass

class OpAST(AST):
    def __init__(self, op, args):
        self.op = op
        self.args = args
    
    def getValue(self):
        if self.op == '+':
            return self.args[0].getValue() + self.args[1].getValue()
        elif self.op == '-':
            return self.args[0].getValue() - self.args[1].getValue()
        elif self.op == '*':
            return self.args[0].getValue() * self.args[1].getValue()
        elif self.op == '/':
            return self.args[0].getValue() / self.args[1].getValue()
        elif self.op == '%':
            return self.args[0].getValue() % self.args[1].getValue()
        raise Exception('Error')

    def __str__(self):
        return "Op({}, [{}])".format(self.op, ", ".join(map(str, self.args)))

class DefAST(AST):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    
    def getValue(self):
        VARS[self.name] = self.expr.getValue()
    
    def __str__(self):
        return "Def({}, {})".format(self.name, self.expr)

class NumberAST(AST):
    def __init__(self, number):
        self.number = number
    
    def getValue(self):
        return self.number

    def __str__(self):
        return "Number({})".format(self.number)

class NameAST(AST):
    def __init__(self, name):
        self.name = name
    
    def getValue(self):
        return VARS.get(self.name, self.name)
    
    def __str__(self):
        return "Name({})".format(self.name)

class CallAST(AST):
    def __init__(self, call, arg):
        self.call = call
        self.arg = arg
    
    def getValue(self):
        fn = self.call.getValue()
        if fn == 'sin':
            return math.sin(self.arg.getValue())
        elif fn == 'cos':
            return math.cos(self.arg.getValue())
        elif fn == 'tan':
            return math.tan(self.arg.getValue())
        elif fn == 'sqrt':
            return math.sqrt(self.arg.getValue())
        elif fn == 'round':
            return round(self.arg.getValue())
        raise Exception('Error')
    
    def __str__(self):
        return "Call({}, {})".format(self.call, self.arg)

if __name__ == "__main__":
    ast = OpAST('', [NumberAST(3), OpAST( '+', [ NumberAST(1), NumberAST(2) ])])
    print(ast.getValue())