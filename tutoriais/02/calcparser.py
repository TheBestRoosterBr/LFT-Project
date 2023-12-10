# -------------------------
# calcparser.py
# ----------------------

import ply.yacc as yacc
import ply.lex as lex
from lingexpslex import tokens


def p_exp_soma(p):
    '''exp : exp SOMA exp1'''
    p[0] = p[1] + p[3]

def p_exp_subtracao(p):
    '''exp : exp SUBTRACAO exp1'''
    p[0] = p[1] - p[3]

def p_exp_exp1(p):
    '''exp : exp1'''
    p[0] = p[1]

def p_exp1_multiplicacao(p):
    '''exp1 : exp1 MULTIPLICACAO exp2'''
    p[0] = p[1] * p[3]

def p_exp1_divisao(p):
    '''exp1 : exp1 DIVISAO exp2'''
    p[0] = p[1] / p[3]

def p_exp1_exp2(p):
    '''exp1 : exp2'''
    p[0] = p[1]

def p_exp2_numero(p):
    '''exp2 : NUMERO'''
    p[0] = p[1]



parser = yacc.yacc()  # Criação do analisador sintático
expressao = input("Digite a expressao: ")
result = parser.parse(expressao)  # Execução da análise sintática.

print(result)