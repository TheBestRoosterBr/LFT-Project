from Projeto.lex.lex_luthor import *
import ply.yacc


def p_program(p):
    """
        program :
    """


def p_program_function_signature(p):
    """
        program : function_signature SEMICOLON program
    """


def p_program_variable_declaration(p):
    """
        program : variable_declaration SEMICOLON program
    """


def p_program_function(p):
    """
        program : function program
    """


def p_program_assign(p):
    """
        program : expression program
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
        user_types : KEYWORD_STRUCT IDENTIFIER
                   | KEYWORD_UNION IDENTIFIER
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
        expression : assign_exp
    """


def p_assign_operator(p):
    """
        assign_operator : ASSIGN
                        | TIMES_ASSIGN
                        | DIVIDE_ASSIGN
                        | MODULUS_ASSIGN
                        | PLUS_ASSIGN
                        | MINUS_ASSIGN
                        | SHIFT_LEFT_ASSIGN
                        | SHIFT_RIGHT_ASSIGN
                        | BITWISE_AND_ASSIGN
                        | BITWISE_XOR_ASSIGN
                        | BITWISE_OR_ASSIGN
    """


def p_assign_exp(p):
    """
        assign_exp : unary_exp assign_operator assign_exp
                    | ternary_conditional_exp
    """


def p_ternary_conditional_exp(p):
    """
        ternary_conditional_exp : logical_exp QUESTION_MARK expression COLON ternary_conditional_exp
                                | logical_exp
    """


def p_logical_exp(p):
    """
        logical_exp : logical_or_exp
    """


def p_logical_or_exp(p):
    """
        logical_or_exp : logical_or_exp LOGICAL_OR logical_and_exp
                        | logical_and_exp
    """


def p_logical_and_exp(p):
    """
        logical_and_exp : logical_and_exp LOGICAL_AND bitwise_or_exp
                        | bitwise_or_exp
    """


def p_bitwise_or_exp(p):
    """
        bitwise_or_exp : bitwise_or_exp BITWISE_OR bitwise_xor_exp
                        | bitwise_xor_exp
    """


def p_bitwise_xor_exp(p):
    """
        bitwise_xor_exp : bitwise_xor_exp BITWISE_XOR bitwise_and_exp
                        | bitwise_and_exp
    """


def p_bitwise_and_exp(p):
    """
        bitwise_and_exp : bitwise_and_exp BITWISE_AND is_equals_exp
                        | is_equals_exp
    """


def p_is_equals_exp(p):
    """
        is_equals_exp : is_equals_exp EQUALS_THEN is_not_equals_exp
                       | is_not_equals_exp
    """


def p_is_not_equals(p):
    """
        is_not_equals_exp : is_not_equals_exp NOT_EQUALS greater_then_exp
                          | greater_then_exp
    """


def p_greater_then_exp(p):
    """
        greater_then_exp : greater_then_exp GREATER_THEN greater_equals_exp
                         | greater_equals_exp
    """


def p_greater_equals_exp(p):
    """
         greater_equals_exp :  greater_equals_exp GREATER_EQUALS less_then_exp
                            | less_then_exp
    """


def p_less_then_exp(p):
    """
        less_then_exp : less_then_exp LESS_THEN less_equals_exp
                      | less_equals_exp
    """


def p_less_equals_exp(p):
    """
        less_equals_exp : less_equals_exp LESS_EQUALS left_shift_exp
                        | left_shift_exp

    """


def p_left_shift_exp(p):
    """
        left_shift_exp : left_shift_exp BITWISE_SHIFT_LEFT right_shift_exp
                        | right_shift_exp
    """


def p_right_shift_exp(p):
    """
        right_shift_exp : right_shift_exp BITWISE_SHIFT_RIGHT plus_exp
                        | plus_exp
    """


def p_plus_exp(p):
    """
        plus_exp : plus_exp PLUS minus_exp
                 | minus_exp
    """


def p_minus_exp(p):
    """
        minus_exp : minus_exp MINUS times_exp
                  | times_exp
    """


def p_times_exp(p):
    """
        times_exp : times_exp TIMES divide_exp
                  | divide_exp
    """


def p_divide_exp(p):
    """
        divide_exp : divide_exp DIVIDE modulus_exp
                    | modulus_exp
    """


def p_modulus_exp(p):
    """
        modulus_exp : modulus_exp MODULUS unary_exp
                    | unary_exp
    """


#Shift reduce
def p_unary_exp(p):
    """
        unary_exp : postfix_exp
                  | INCREMENT unary_exp
                  | DECREMENT unary_exp
                  | unary_operator unary_exp
                  | cast_exp unary_exp
                  | sizeof_exp

    """


def p_sizeof_exp(p):
    """
        sizeof_exp :  KEYWORD_SIZEOF unary_exp
                    | KEYWORD_SIZEOF type
                    | KEYWORD_SIZEOF pointer
    """


def p_cast_exp(p):
    """
        cast_exp : LPAREN type RPAREN
                 | LPAREN pointer RPAREN
    """


def p_unary_operator(p):
    """
        unary_operator : BITWISE_AND
                       | TIMES
                       | PLUS
                       | MINUS
                       | BITWISE_COMPLEMENT
                       | NOT
    """


def p_postfix_exp(p):
    """
        postfix_exp : postfix_exp LBRACKET expression RBRACKET
                    | postfix_exp LPAREN RPAREN
                    | postfix_exp LPAREN function_call_parameters RPAREN
                    | postfix_exp DOT IDENTIFIER
                    | postfix_exp ARROW IDENTIFIER
                    | postfix_exp INCREMENT
                    | postfix_exp DECREMENT
                    | primary_exp
    """


def p_function_call_parameters(p):
    """
        function_call_parameters : expression
                                  | expression COMMA function_call_parameters
    """


def p_primary_exp(p):
    """
        primary_exp : identifier_exp
    """


def p_identifier_exp(p):
    """
        identifier_exp : IDENTIFIER
                        | string_exp
    """


def p_string_exp(p):
    """
        string_exp : STRING
                    | number_exp
    """


def p_number_exp(p):
    """
        number_exp : integer_number
                    | FLOAT_NUMBER
                    | CHARACTER
                    | parentesis_exp
    """


#shift/reduce
def p_parentesis_exp(p):
    """
        parentesis_exp : LPAREN expression RPAREN
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
