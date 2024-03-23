from Projeto.lex.lex_luthor import *
import ply.yacc


def p_program(p):
    """
        program : program_item
                | program_item program
    """


def p_program_variable_declaration(p):
    """
        program_item : variable_declaration_list SEMICOLON
    """


def p_program_function(p):
    """
        program_item : function
    """


def p_program_assign(p):
    """
        program_item : global_assign_identifier_list
    """


def p_program_type(p):
    """
        program_item : type SEMICOLON
    """


def p_global_assign_identifier_list(p):
    """
        global_assign_identifier_list : IDENTIFIER ASSIGN expression
                                      | IDENTIFIER ASSIGN expression COMMA global_assign_identifier_list
    """


# Copiado do java
def p_block(p):
    """
        block : LBRACE RBRACE
              | LBRACE block_statements RBRACE
    """


def p_block_statements(p):
    """
        block_statements : block_statement
                        | block_statements block_statement
    """


def p_block_statement(p):
    """
        block_statement : statement
    """


def p_statement(p):
    """
        statement :   statement_without_trailing_substatement
                   |  if_then_statement
                   |  if_then_else_statement
                   |  while_statement
                   |  for_statement

    """


def p_statement_without_trailing_substatement(p):
    """
        statement_without_trailing_substatement : block
                                                | SEMICOLON
                                                | expression_list SEMICOLON
                                                | switch_stm
                                                | do_statement
                                                | KEYWORD_BREAK SEMICOLON
                                                | KEYWORD_CONTINUE SEMICOLON
                                                | return_stm SEMICOLON
                                                | IDENTIFIER COLON
                                                | KEYWORD_GOTO IDENTIFIER SEMICOLON
                                                | variable_declaration_list SEMICOLON
                                                | type SEMICOLON
    """


def p_statement_no_short_if(p):
    """
        statement_no_short_if : statement_without_trailing_substatement
                              | if_then_else_statement_no_short_if
                              | while_statement_no_short_if
                              | for_statement_no_short_if
    """


def p_if_then_statement(p):
    """
        if_then_statement : KEYWORD_IF LPAREN expression RPAREN statement
    """


def p_if_then_else_statement(p):
    """
        if_then_else_statement : KEYWORD_IF LPAREN expression RPAREN statement_no_short_if KEYWORD_ELSE statement
    """


def p_if_then_else_statement_no_short_if(p):
    """
        if_then_else_statement_no_short_if : KEYWORD_IF LPAREN expression RPAREN statement_no_short_if KEYWORD_ELSE statement_no_short_if
    """


def p_while_statement(p):
    """
        while_statement : KEYWORD_WHILE LPAREN expression RPAREN statement
    """


def p_while_statement_no_short_if(p):
    """
        while_statement_no_short_if : KEYWORD_WHILE LPAREN expression RPAREN statement_no_short_if
    """


def p_do_statement(p):
    """
        do_statement : KEYWORD_DO statement KEYWORD_WHILE LPAREN expression RPAREN SEMICOLON
    """


def p_for_params(p):
    """
        for_params : variable_declaration_list SEMICOLON for_param
                    | variable_declaration_list SEMICOLON for_param expression_list
                    | for_param for_param expression_list
                    | for_param for_param
    """


def p_for_param(p):
    """
        for_param : SEMICOLON
                  | expression_list SEMICOLON
    """


def p_for_statement(p):
    """
        for_statement : KEYWORD_FOR LPAREN for_params RPAREN statement
    """


def p_for_statement_no_short_if(p):
    """
        for_statement_no_short_if : KEYWORD_FOR LPAREN for_params RPAREN statement_no_short_if
    """


def p_switch_stm(p):
    """
        switch_stm : KEYWORD_SWITCH LPAREN expression RPAREN LBRACE switch_itens RBRACE
    """


def p_switch_itens(p):
    """
        switch_itens : KEYWORD_CASE expression COLON block_statements
                    | KEYWORD_DEFAULT COLON block_statements
                    | KEYWORD_CASE expression COLON block_statements switch_itens
                    | KEYWORD_DEFAULT COLON block_statements switch_itens
    """


def p_return_stm(p):
    """
        return_stm : KEYWORD_RETURN
                    | KEYWORD_RETURN expression
    """


def p_function(p):
    """
        function : function_signature block
    """


def p_funcion_signature(p):
    """
        function_signature : type identifier LPAREN signature_param_list RPAREN
                           | type identifier LPAREN RPAREN
    """


def p_triple_dot(p):
    """
        triple_dot : DOT DOT DOT
    """


def p_signature_param_list(p):
    """
        signature_param_list : signature_param COMMA signature_param_list
                             | signature_param

    """


def p_signature_param(p):
    """
        signature_param : type
                        | type multiple_times
                        | type multiple_bracket_signature
                        | type identifier
                        | type identifier multiple_bracket_signature
                        | triple_dot
    """


def p_multiple_bracket_signature(p):
    """
        multiple_bracket_signature :  LBRACKET RBRACKET multiple_bracket_signature
                                    | LBRACKET RBRACKET
                                    | bracket_with_bounds multiple_bracket_signature
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


def p_value_list(p):
    """
        value_list : LBRACE value_list_item RBRACE
    """


def p_value_list_item(p):
    """
        value_list_item : expression
                        | expression COMMA value_list_item
                        | value_list
                        | value_list COMMA value_list_item
    """


def p_variable_declaration_list(p):
    """
        variable_declaration_list : type identifier_list
    """


def p_identifier_list(p):
    """
        identifier_list : identifier
                        | identifier COMMA identifier_list
    """


def p_identifier_list_array(p):
    """
        identifier_list :  identifier multiple_bracket_signature
                         | identifier multiple_bracket_signature COMMA identifier_list
    """


def p_assign_identifier_list(p):
    """
        identifier_list : identifier ASSIGN expression
                        | identifier ASSIGN expression COMMA identifier_list
    """


def p_assign_identifier_list_array(p):
    """
        identifier_list : identifier multiple_bracket_signature ASSIGN value_list
                       | identifier multiple_bracket_signature ASSIGN value_list COMMA identifier_list
    """


def p_assign_identifier_list_non_array(p):
    """
        identifier_list : identifier ASSIGN value_list
                        | identifier ASSIGN value_list COMMA identifier_list
    """


def p_function_pointer(p):
    """
        function_pointer : identifier LPAREN signature_param_list RPAREN
                         | identifier LPAREN RPAREN
    """


def p_function_pointer_array(p):
    """
        function_pointer_array : LPAREN TIMES identifier multiple_bracket_signature RPAREN LPAREN signature_param_list RPAREN
                               | LPAREN TIMES identifier multiple_bracket_signature RPAREN LPAREN RPAREN
    """


def p_identifier_list_function_pointer(p):
    """
        identifier_list : function_pointer
                        | function_pointer COMMA identifier_list
    """


def p_identifier_list_function_pointer_assign(p):
    """
        identifier_list : function_pointer ASSIGN expression
                        | function_pointer ASSIGN expression COMMA identifier_list
    """


def p_identifier_list_function_pointer_array(p):
    """
        identifier_list : function_pointer_array
                        | function_pointer_array COMMA identifier_list
    """


def p_identifier_list_function_pointer_array_assing(p):
    """
        identifier_list : function_pointer_array ASSIGN value_list
                        | function_pointer_array ASSIGN value_list COMMA identifier_list
    """


def p_identifier(p):
    """
        identifier :  IDENTIFIER
                    | TIMES identifier
                    | LPAREN identifier RPAREN
    """


def p_type(p):
    """
        type : user_types
             | primitive_types
             | type_modifier type
    """


def p_struct_declaration(p):
    """
        struct_declaration :  KEYWORD_STRUCT IDENTIFIER LBRACE RBRACE
                            | KEYWORD_STRUCT IDENTIFIER LBRACE struct_or_union_member_list RBRACE
                            | KEYWORD_STRUCT LBRACE RBRACE
                            | KEYWORD_STRUCT LBRACE struct_or_union_member_list RBRACE
                            | KEYWORD_STRUCT IDENTIFIER
    """


def p_union_declaration(p):
    """
        union_declaration :   KEYWORD_UNION IDENTIFIER LBRACE RBRACE
                            | KEYWORD_UNION IDENTIFIER LBRACE struct_or_union_member_list RBRACE
                            | KEYWORD_UNION LBRACE RBRACE
                            | KEYWORD_UNION LBRACE struct_or_union_member_list RBRACE
                            | KEYWORD_UNION IDENTIFIER
    """


def p_struct_or_union_member_list(p):
    """
        struct_or_union_member_list : variable_declaration_list_no_assign SEMICOLON
                                   | variable_declaration_list_no_assign SEMICOLON struct_or_union_member_list

    """


def p_variable_declaration_list_no_assign(p):
    """
        variable_declaration_list_no_assign : type variable_list_no_assign
    """


def p_variable_list_no_assign(p):
    """
        variable_list_no_assign : identifier
                                | variable_list_no_assign COMMA identifier
    """


def p_enum_declaration(p):
    """
        enum_declaration : KEYWORD_ENUM LBRACE enum_item_list RBRACE
                         | KEYWORD_ENUM IDENTIFIER LBRACE enum_item_list RBRACE
                         | KEYWORD_ENUM IDENTIFIER
    """


def p_enum_item_list(p):
    """
        enum_item_list : IDENTIFIER
                        | IDENTIFIER COMMA enum_item_list
                        | IDENTIFIER ASSIGN expression
                        | IDENTIFIER ASSIGN expression COMMA enum_item_list
    """


# Completar os modificadores de tipo ex: static int | unsingned long long int | short int
def p_type_modifier(p):
    """
        type_modifier :   KEYWORD_STATIC
                        | KEYWORD_UNSIGNED
                        | KEYWORD_VOLATILE
                        | KEYWORD_EXTERN
                        | KEYWORD_SIGNED
                        | KEYWORD_REGISTER
                        | KEYWORD_CONST
    """


def p_user_types(p):
    """
        user_types : struct_declaration
                   | union_declaration
                   | enum_declaration
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


def p_expression_list(p):
    """
        expression_list : expression
                        | expression COMMA expression_list
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


# Shift reduce
def p_unary_exp(p):
    """
        unary_exp : postfix_exp
                  | INCREMENT postfix_exp
                  | DECREMENT postfix_exp
                  | postfix_exp INCREMENT
                  | postfix_exp DECREMENT
                  | cast_exp postfix_exp
                  | sizeof_exp
                  | unary_operator unary_exp
    """


def p_sizeof_exp(p):
    """
        sizeof_exp :  KEYWORD_SIZEOF postfix_exp
                    | KEYWORD_SIZEOF LPAREN type RPAREN
                    | KEYWORD_SIZEOF LPAREN type multiple_times RPAREN
    """


def p_cast_exp(p):
    """
        cast_exp : LPAREN type RPAREN
                 | LPAREN type multiple_times RPAREN
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


# shift/reduce
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
    with open("parser_test.c", "r") as file:
        for line in file:
            if not line.startswith('#'):
                input += line

    l.input(input)
    parser = ply.yacc.yacc()
    result = parser.parse()


if __name__ == "__main__":
    main()
    print("Nenhum erro sintático detectado")
