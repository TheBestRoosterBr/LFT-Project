import ply.lex as lex

# Lista de nomes de tokens. Isso é sempre necessário
tokens = [
  'IDENTIFIER', 'NUMBER',
  'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULUS',
  'EQUALS_THEN', 'NOT_EQUALS', 'GREATER_THEN', 'LESS_THEN', "LESS_EQUALS", 'GREATER_EQUALS',
  'LOGICAL_AND', 'LOGICAL_OR', 'NOT',
  'BITWISE_AND', 'BITWISE_OR', 'BITWISE_XOR', 'BITWISE_COMPLEMENT', 'BITWISE_SHIFT_LEFT', 'BITWISE_SHIFT_RIGHT',
  'INCREMENT', 'DECREMENT',
  'LPAREN', 'RPAREN',
  'LBRACKET', 'RBRACKET',
  'LBRACE', 'RBRACE',
  'SEMICOLON',
  'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'TIMES_ASSIGN', 'DIVIDE_ASSIGN', 'MODULUS_ASSIGN', 'SHIFT_LEFT_ASSIGN',
  'SHIFT_RIGHT_ASSIGN', 'BITWISE_AND_ASSIGN', 'BITWISE_OR_ASSIGN', 'BITWISE_XOR_ASSIGN',
  'COMMENT', 'MULTILINE_COMMENT',
  'STRING', 'CHARACTER',
  'COMMA', 'DOT',
  'QUESTION_MARK',
  'COLON',
  'ARROW',
  'PRE_PROCESSOR'
] + ['KEYWORD_AUTO', 'KEYWORD_BREAK', 'KEYWORD_CASE', 'KEYWORD_CONST', 'KEYWORD_CONTINUE',
     'KEYWORD_DEFAULT', 'KEYWORD_DO', 'KEYWORD_ELSE', 'KEYWORD_ENUM', 'KEYWORD_EXTERN',
     'KEYWORD_FOR', 'KEYWORD_GOTO', 'KEYWORD_IF', 'KEYWORD_REGISTER',
     'KEYWORD_RETURN', 'KEYWORD_SIGNED', 'KEYWORD_SIZEOF', 'KEYWORD_STATIC', 'KEYWORD_STRUCT',
     'KEYWORD_SWITCH', 'KEYWORD_TYPEDEF', 'KEYWORD_UNION', 'KEYWORD_UNSIGNED', 'KEYWORD_VOLATILE',
     'KEYWORD_WHILE'] + [
     'TYPE_CHAR', 'TYPE_DOUBLE', 'TYPE_FLOAT', 'TYPE_INT', 'TYPE_LONG', 'TYPE_SHORT', 'TYPE_VOID'
]


# Palavras-chave da linguagem
reserved = {
  'auto': 'KEYWORD_AUTO',
  'break': 'KEYWORD_BREAK',
  'case': 'KEYWORD_CASE',
  'const': 'KEYWORD_CONST',
  'continue': 'KEYWORD_CONTINUE',
  'default': 'KEYWORD_DEFAULT',
  'do': 'KEYWORD_DO',
  'else': 'KEYWORD_ELSE',
  'enum': 'KEYWORD_ENUM',
  'extern': 'KEYWORD_EXTERN',
  'for': 'KEYWORD_FOR',
  'goto': 'KEYWORD_GOTO',
  'if': 'KEYWORD_IF',
  'register': 'KEYWORD_REGISTER',
  'return': 'KEYWORD_RETURN',
  'signed': 'KEYWORD_SIGNED',
  'sizeof': 'KEYWORD_SIZEOF',
  'static': 'KEYWORD_STATIC',
  'struct': 'KEYWORD_STRUCT',
  'switch': 'KEYWORD_SWITCH',
  'typedef': 'KEYWORD_TYPEDEF',
  'union': 'KEYWORD_UNION',
  'unsigned': 'KEYWORD_UNSIGNED',
  'volatile': 'KEYWORD_VOLATILE',
  'while': 'KEYWORD_WHILE',

  'char': 'TYPE_CHAR',
  'double': 'TYPE_DOUBLE',
  'float': 'TYPE_FLOAT',
  'void': 'TYPE_VOID',
  'int': 'TYPE_INT',
  'long': 'TYPE_LONG',
  'short': 'TYPE_SHOT',
}
#Regras de comentários
t_COMMENT = r'//.*\n'
t_MULTILINE_COMMENT = r'/\*(.|\n)*?\*/'

t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'
t_QUESTION_MARK = r'\?'
t_COMMA = r','
t_ARROW = r'->'

#Operadores Especiais
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'


t_ASSIGN = r'='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MODULUS_ASSIGN = r'%='
t_SHIFT_LEFT_ASSIGN = r'<<='
t_SHIFT_RIGHT_ASSIGN = r'>>='
t_BITWISE_AND_ASSIGN = r'&='
t_BITWISE_OR_ASSIGN = r'\|='
t_BITWISE_XOR_ASSIGN = r'\^='


#Operadores aritméticos
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_MODULUS = r'%'

#Operadores de atribuição 'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'TIMES_ASSIGN', 'DIVIDE_ASSIGN', 'MODULUS_ASSIGN',
# 'SHIFT_LEFT_ASSIGN', 'SHIFT_RIGHT_ASSIGN', 'BITWISE_AND_ASSIGN', 'BITWISE_OR_ASSIGN', 'BITWISE_XOR_ASSIGN',

#Operadores de comparação
t_EQUALS_THEN = r'=='
t_NOT_EQUALS = r'!='
t_GREATER_THEN = r'>'
t_LESS_THEN = r'<'
t_GREATER_EQUALS = '>='
t_LESS_EQUALS = '<='

#Operadores Lógicos
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_NOT = '\!'

#BITWISE 'BITWISE_AND', 'BITWISE_OR', 'BITWISE_XOR', 'BITWISE_COMPLEMENT', 'BITWISE_SHIFT_LEFT', 'BITWISE_SHIFT_RIGHT',
t_BITWISE_AND = r'&'
t_BITWISE_OR = r'\|'
t_BITWISE_XOR = r'\^'
t_BITWISE_COMPLEMENT = r'~'
t_BITWISE_SHIFT_LEFT = r'<<'
t_BITWISE_SHIFT_RIGHT = r'>>'

#Parentesis
t_LPAREN = r'\('
t_RPAREN = r'\)'

#Colchetes
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

#Chaves
t_LBRACE = r'{'
t_RBRACE = r'}'


#Regras de Strings e Char
def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = bytes(t.value, "utf-8").decode("unicode_escape")
    return t

def t_CHARACTER(t):
    r"'([^'\\]|\\.)'"
    t.value = bytes(t.value, "utf-8").decode("unicode_escape")
    return t

# Regra complexa para identificadores (inclui palavras-chave)
def t_IDENTIFIER(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = reserved.get(t.value, 'IDENTIFIER') # Verifica palavras reservadas
   return t

# Regra para números
def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_PREPROCESSOR(t):
    r'\#(include|define|if|ifdef|ifndef|else|elif|endif|undef|error|pragma).*'
    t.type = 'PRE_PROCESSOR'
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

# Regra para contar números de linha
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

# Regra para lidar com erros
def t_error(t):
   print("Caractere ilegal '%s'" % t.value[0])
   t.lexer.skip(1)
lexer = lex.lex()

file = '/mnt/e/Documentos/Projetos/C_CPP/CopiaDaSaxa/FreshFish/src/board.c'

code = ''
with open(file, 'r') as f:
    code = f.read()
lexer.input(code)

# Realizando analise lexica
for tok in lexer:
    print('{}  {}  {}'.format(tok.type, str(tok.value), str(tok.lineno)))
