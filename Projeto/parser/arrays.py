from Projeto.parser import  *


def p_array_declaration(p):
    """
        array_declaration : type IDENTIFIER LBRACKET RBRACKET
                          | pointer IDENTIFIER LBRACKET RBRACKET
    """


def p_array_definition(p):
    """
        array_definition : static_array_definition
                         | runtime_array_definition
    """


def p_static_array_definition(p):
    """
        static_array_definition : type IDENTIFIER LBRACKET NUMBER RBRACKET
                                | pointer IDENTIFIER LBRACKET NUMBER RBRACKET
    """


def p_runtime_array_definition(p):
    """
         runtime_array_definition : type IDENTIFIER LBRACKET IDENTIFIER RBRACKET
                                 | pointer IDENTIFIER LBRACKET IDENTIFIER RBRACKET
    """
