import ply.lex as lex

# Lista de nomes de tokens. Isso é sempre necessário
tokens = [
  'IDENTIFIER', 'NUMBER',
  'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
  'LPAREN', 'RPAREN',
  'SEMICOLON', 'EQUALS', 'COMENT'
] + [ 'KEYWORD_AUTO', 'KEYWORD_BREAK', 'KEYWORD_CASE', 'KEYWORD_CHAR', 'KEYWORD_CONST', 'KEYWORD_CONTINUE', 'KEYWORD_DEFAULT', 'KEYWORD_DO', 'KEYWORD_DOUBLE', 'KEYWORD_ELSE', 'KEYWORD_ENUM', 'KEYWORD_EXTERN', 'KEYWORD_FLOAT', 'KEYWORD_FOR', 'KEYWORD_GOTO', 'KEYWORD_IF', 'KEYWORD_INT', 'KEYWORD_LONG', 'KEYWORD_REGISTER', 'KEYWORD_RETURN', 'KEYWORD_SHORT', 'KEYWORD_SIGNED', 'KEYWORD_SIZEOF', 'KEYWORD_STATIC', 'KEYWORD_STRUCT', 'KEYWORD_SWITCH', 'KEYWORD_TYPEDEF', 'KEYWORD_UNION', 'KEYWORD_UNSIGNED', 'KEYWORD_VOID', 'KEYWORD_VOLATILE', 'KEYWORD_WHILE' ]

# Palavras-chave da linguagem
reserved = {
  'auto': 'KEYWORD_AUTO',
  'break': 'KEYWORD_BREAK',
  'case': 'KEYWORD_CASE',
  'char': 'KEYWORD_CHAR',
  'const': 'KEYWORD_CONST',
  'continue': 'KEYWORD_CONTINUE',
  'default': 'KEYWORD_DEFAULT',
  'do': 'KEYWORD_DO',
  'double': 'KEYWORD_DOUBLE',
  'else': 'KEYWORD_ELSE',
  'enum': 'KEYWORD_ENUM',
  'extern': 'KEYWORD_EXTERN',
  'float': 'KEYWORD_FLOAT',
  'for': 'KEYWORD_FOR',
  'goto': 'KEYWORD_GOTO',
  'if': 'KEYWORD_IF',
  'int': 'KEYWORD_INT',
  'long': 'KEYWORD_LONG',
  'register': 'KEYWORD_REGISTER',
  'return': 'KEYWORD_RETURN',
  'short': 'KEYWORD_SHORT',
  'signed': 'KEYWORD_SIGNED',
  'sizeof': 'KEYWORD_SIZEOF',
  'static': 'KEYWORD_STATIC',
  'struct': 'KEYWORD_STRUCT',
  'switch': 'KEYWORD_SWITCH',
  'typedef': 'KEYWORD_TYPEDEF',
  'union': 'KEYWORD_UNION',
  'unsigned': 'KEYWORD_UNSIGNED',
  'void': 'KEYWORD_VOID',
  'volatile': 'KEYWORD_VOLATILE',
  'while': 'KEYWORD_WHILE'
}

# Regras de expressão regular para tokens simples
t_COMENT = r'//([a-zA-Z_][a-zA-Z_0-9])*'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_EQUALS = r'='

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
lexer.input("""
#include <stdio.h>

int main() {

    #ODEIO VOCES TODOS
    for (int i = 0; i < 10; i++) {
        printf("Hello, world!\n");
    }

   return 0;
}
""")

# Realizando analise lexica
print('{:10s}{:10s}{:10s}{:10s}'.format("Token", "Lexema", "Linha", "Coluna"))
for tok in lexer:
    print('{:10s}{:10s}{:10s}{:10s}'.format(tok.type, str(tok.value), str(tok.lineno), str(tok.lexpos)))
