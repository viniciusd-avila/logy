from rply import ParserGenerator
from ast import *

pg = ParserGenerator(
    # list of all token names, accepted by the parser.
    ['AND', 'OPEN_PARENS', 'CLOSE_PARENS',
     'OR', 'NOT', 'IMPLY', 'BOOLEAN','XOR','XNOR'
    ])


@pg.production('expression : BOOLEAN')
def expression_boolean(p):
    return Boolean(p[0])

@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]

@pg.production('expression : expression NOT')
def expression_unaop(p):
    operator = p[1]
    value = p[0]
    token_type = operator.gettokentype()
    if token_type == 'NOT':
        return Not(value)
    else:
        raise AssertionError(f'{p} is not a valid expression.')

@pg.production('expression : expression expression AND')
@pg.production('expression : expression expression OR')
@pg.production('expression : expression expression XOR')
@pg.production('expression : expression expression IMPLY')
@pg.production('expression : expression expression XNOR')
def expression_binop(p):
    operator = p[2]
    left = p[0]
    right = p[1]
    token_type = operator.gettokentype()

    if token_type == 'AND':
        return And(left, right)
    elif token_type == 'OR':
        return Or(left, right)
    elif token_type == 'XOR':
        return Xor(left, right)
    elif token_type == 'IMPLY':
        return Or(Not(left), right)
    elif token_type == 'XNOR':
        return Not(Xor(left, right))
    else:
        raise AssertionError(f'{p} is not a valid expression.')

parser = pg.build()