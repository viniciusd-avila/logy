from rply import LexerGenerator

lg = LexerGenerator()


lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')
lg.add('AND', r'\^')
lg.add('OR', r'v')
lg.add('XOR', r'x')
lg.add('NOT', r'¬')
lg.add('IMPLY', r'->')
lg.add('XNOR', r'<->')
lg.add('VARIABLE', r'[A-Z]')
lg.add('BOOLEAN', r'(t|f)')
lg.ignore(r'\s+')

lexer = lg.build()