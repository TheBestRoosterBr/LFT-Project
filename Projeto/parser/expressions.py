from Projeto.parser import  *


def p_assign(p):
    """
        assign : IDENTIFIER ASSIGN expression
    """


def p_define_and_assign(p):
    """
        define_and_assign : type assign
                         | pointer assign
    """


def p_expression2(p):
    """
        expression2 : LOGICAL_AND expression
                    | LOGICAL_OR expression
                    | PLUS expression
                    | MINUS expression
                    | TIMES expression
                    | DIVIDE expression
                    | MODULUS expression
                    | EQUALS_THEN expression
                    | NOT_EQUALS expression
                    | GREATER_THEN expression
                    | LESS_THEN expression
                    | LESS_EQUALS expression
                    | GREATER_EQUALS expression
                    | LPAREN expression RPAREN
                    | expression
                    | IDENTIFIER
                    | number
                    | STRING
                    | CHARACTER
                    | assign
                    | define_and_assign


    """



def p_expression(p):
    """
        expression : expression expression2
                    | NOT expression
                    | expression2
    """
