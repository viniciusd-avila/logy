import sys
import re
import itertools
from lexer import lexer
from parsing import parser

def evaluate(statement):
    return parser.parse(lexer.lex(statement)).eval()

def prove(theorem):
    variables = set(filter(None,map(lambda x: x if re.match('[A-Z]',x) else None,list(theorem))))
    values = ['t','f']
    product = (itertools.product(variables,values))
    combinations = filter(lambda x: len(set([p[0] for p in x])) == len(variables), itertools.combinations(product,len(variables)))
   
    res = 't'
    table = []
    for config in combinations:
        theorem_copy = theorem
        for declaration in config:
            var = declaration[0]
            value = declaration[1]
            theorem_copy = theorem_copy.replace(var,value)
        ans = evaluate(theorem_copy)
        table.append([config,theorem_copy,ans])
        if ans=='f':
            res = 'f'
    return table,res

# Example: 
# print(prove('(P (P Q ->) ^ Q ->)'))