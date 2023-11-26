import ply.lex as lex

tokens = ('NUMBER', 'WORD', "PLUS")
states = (('foo', 'exclusive'), ('bar', 'inclusive'))

t_WORD = r'[a-zA-Z]+'
t_ignore = ' \t'

t_foo_ignore = ' \t'
t_foo_NUMBER = r'\d+'  # Reconhece 'NUMBER' no estado 'foo'
t_foo_PLUS = r'\+' #PLUS no estado foo

t_bar_NUMBER = r'\d+'


def t_foo_newline(t):  #Reconhece quebra de linha no estado foo.
  r'\n'
  t.lexer.lineno += 1


def t_error(t):
  print('error in INITIAL state, %s' % t.value[0])
  t.lexer.skip(1)


def t_foo_error(t):
  print('error in foo state, %s' % t.value[0])
  t.lexer.skip(1)


def t_bar_error(t):
    print('error in bar state, %s' % t.value[0])
    t.lexer.skip(1)


def t_begin_foo(t):
  r'<foo>'
  t.lexer.begin('foo')


def t_foo_end_foo(t):
  r'\</foo\>'
  t.lexer.begin('INITIAL')

def t_begin_bar(t):
  r'<bar>'
  t.lexer.begin('bar')

def t_bar_end_bar(t):
  r'\</bar\>'
  t.lexer.begin('INITIAL')


lexer = lex.lex()
lex.input(" <bar> lft  muito legal </bar> <foo> 3322 + 34423 </foo> amer")
for l in lexer:
  print(l.value)