from Projeto.lex.lex_luthor import *
import ply.yacc


def p_program(p):
    """
        program : function_signature SEMICOLON program
                | variable_declaration SEMICOLON program
                | function program
                |
    """


def p_command_block(p):
    """
        command_block : LBRACE RBRACE
                      | LBRACE command_list RBRACE
    """


def p_command_list(p):
    """
        command_list : command command_list
                    | command
    """


def p_command(p):
    """
        command : variable_declaration SEMICOLON
                | variable_declaration ASSIGN expression SEMICOLON
                | IDENTIFIER ASSIGN expression SEMICOLON
                | expression SEMICOLON
                | SEMICOLON
    """


def p_function(p):
    """
        function : function_signature command_block
    """


def p_funcion_signature(p):
    """
        function_signature : type IDENTIFIER LPAREN signature_param_list RPAREN
                            | pointer IDENTIFIER LPAREN signature_param_list RPAREN
                            | type IDENTIFIER LPAREN RPAREN
                            | pointer IDENTIFIER LPAREN RPAREN
    """


def p_signature_param_list(p):
    """
        signature_param_list : signature_param COMMA signature_param
                             | signature_param
    """


def p_signature_param(p):
    """
        signature_param : type
                        | pointer
                        | type multiple_bracket_signature
                        | pointer multiple_bracket_signature
                        | variable_declaration
                        | variable_declaration multiple_bracket_signature
    """


def p_multiple_bracket_signature(p):
    """
        multiple_bracket_signature : LBRACKET RBRACKET multiple_bracket_with_bounds
                                    | multiple_bracket_with_bounds

    """


def p_multiple_bracket_with_bounds(p):
    """
        multiple_bracket_with_bounds : bracket_with_bounds multiple_bracket_with_bounds
                                     | bracket_with_bounds
    """


def p_bracket_with_bounds(p):
    """
        bracket_with_bounds : LBRACKET number_id RBRACKET
    """


def p_number_id(p):
    """
        number_id : IDENTIFIER
                  | integer_number
    """


def p_variable_declaration(p):
    """
        variable_declaration : type IDENTIFIER
                             | pointer IDENTIFIER
    """


def p_pointer(p):
    """
        pointer : type multiple_times
    """


def p_type(p):
    """
        type : user_types
            | primitive_types
    """


def p_user_types(p):
    """
        user_types : IDENTIFIER
                    | KEYWORD_STRUCT IDENTIFIER
    """


def p_primitive_types(p):
    """
        primitive_types : TYPE_CHAR
                        | TYPE_INT
                        | TYPE_SHORT
                        | TYPE_LONG
                        | TYPE_FLOAT
                        | TYPE_DOUBLE
                        | TYPE_VOID
    """


def p_multiple_times(p):
    """
        multiple_times : TIMES multiple_times
                        | TIMES
    """


def p_integer_number(p):
    """
        integer_number : NUMBER
                       | BINARY_NUMBER
                       | HEXADECIMAL_NUMBER
                       | OCTAL_NUMBER
    """


def p_expression(p):
    """
        expression : and_assign_bitwise_operator
    """


def p_and_assign_bitwise_operator(p):
    """
        and_assign_bitwise_operator : xor_assign_bitwise_operator BITWISE_AND_ASSIGN and_assign_bitwise_operator
                                    | xor_assign_bitwise_operator
    """


def p_xor_assign_bitwise_operator(p):
    """
        xor_assign_bitwise_operator : or_assign_bitwise_operator BITWISE_XOR_ASSIGN xor_assign_bitwise_operator
                                    | or_assign_bitwise_operator
    """


def p_or_assign_bitwise_operator(p):
    """
        or_assign_bitwise_operator : or_assign_bitwise_operator BITWISE_OR_ASSIGN left_shift_bitwise_assign
                                    | left_shift_bitwise_assign
    """


def p_left_shift_bitwise_assign(p):
    """
        left_shift_bitwise_assign : IDENTIFIER
                                  | integer_number
    """


def p_error(p):
    if p:
        print("Erro de sintaxe na linha %d: %s" % (p.lineno, p.value))
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")
    exit(1)


def main():
    l = lex.lex()

    input = ""
    with open("parser\\parser_test.c", "r") as file:
        for line in file:
            if not line.startswith('#'):
                input += line

    l.input(input)
    parser = ply.yacc.yacc()
    result = parser.parse()


if __name__ == "__main__":
    main()
    print("Nenhum erro sintático detectado")
