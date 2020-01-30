from rply.token import BaseBox

class Boolean(BaseBox):
    def __init__(self,value):
        self.value = value
    
    def eval(self):
        return self.value.getstr()

class UnaryOp(BaseBox):
    def __init__(self,value):
        self.value = value

class BinaryOp(BaseBox):
    def __init__(self,left,right):
        self.left = left
        self.right = right

class Not(UnaryOp):
    def eval(self):
        if self.value.eval() == 't':
            return 'f'
        elif self.value.eval() == 'f':
            return 't'

class And(BinaryOp):
    def eval(self):
        if (self.left.eval() == 't' and self.right.eval() == 't'):
            return 't'
        else:
            return 'f'

class Or(BinaryOp):
    def eval(self):
        if (self.left.eval() == 'f' and self.right.eval() == 'f'):
            return 'f'
        else:
            return 't'

class Xor(BinaryOp):
    def eval(self):
        if (self.left.eval() == 't' and self.right.eval() == 't'):
            return 'f'
        elif (self.left.eval() == 'f' and self.right.eval() == 'f'):
            return 'f'
        else:
            return 't'