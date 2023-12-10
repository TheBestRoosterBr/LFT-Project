# -------------------------
# lingexpslex.py
#----------------------
import ply.lex as lex

tokens = ('SOMA', 'NUMERO', 'SUBTRACAO', 'DIVISAO', 'MULTIPLICACAO')
t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_DIVISAO = r'/'
t_MULTIPLICACAO = r'\*'


def t_NUMERO(t):
  r'\d+'
  t.value = int(t.value)
  return t
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

t_ignore = ' \t\n'


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


lexer = lex.lex()
#
# # Test it out
data = '''
 3 + 4 - 10 + 20 - 2
 '''
lexer.input(data)