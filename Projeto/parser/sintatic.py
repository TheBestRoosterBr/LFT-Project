from Projeto.lex.lex_luthor import *
import ply.yacc


def p_program(p):
    """
        program : function_declaration program
                | function program
                |
    """


def p_function_declaration(p):
    """
        function_declaration : signature SEMICOLON
    """


def p_command_block(p):
    """
        command_block : LBRACE commands RBRACE
                        | LBRACE RBRACE
    """


def p_commands(p):
    """
        commands : command commands
                | command
    """


def p_command(p):
    """
        command : data_type IDENTIFIER SEMICOLON
                | while_loop
                | assign SEMICOLON
                | define_and_assign SEMICOLON
                | expression SEMICOLON
                | command_block
                | SEMICOLON
                | array_definition SEMICOLON
    """


def p_while_signature(p):
    """
        while_signature : KEYWORD_WHILE LPAREN expression RPAREN
    """


def p_while_loop(p):
    """
        while_loop : while_signature command_block
                    | while_signature command
    """


def p_assign(p):
    """
        assign : IDENTIFIER ASSIGN expression
    """


def p_define_and_assign(p):
    """
        define_and_assign : type assign
                         | pointer assign
    """


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


def p_number(p):
    """
        number : NUMBER
                | FLOAT_NUMBER
                | BINARY_NUMBER
                | HEXADECIMAL_NUMBER
                | OCTAL_NUMBER
    """


def p_function(p):
    """
        function : signature command_block
    """


def p_signature(p):
    """
        signature : type IDENTIFIER function_parameters
                  | pointer IDENTIFIER function_parameters
    """


def p_function_parameters(p):
    """
        function_parameters : LPAREN parameters_list RPAREN
                            | LPAREN RPAREN
    """


def p_parameters_list(p):
    """
            parameters_list : data_definition COMMA parameters_list
            | data_definition
            | array_definition COMMA parameters_list
            | array_definition
            | array_declaration COMMA parameters_list
            | array_declaration
    """


def p_array_declaration(p):
    """
        array_declaration : data_definition IDENTIFIER LBRACKET RBRACKET
    """


def p_array_definition(p):
    """
        array_definition : data_definition IDENTIFIER multiple_bracket_array
    """


def p_sized_bracket_array(p):
    """
        sized_bracket_array : LBRACKET IDENTIFIER RBRACKET
                            | LBRACKET NUMBER RBRACKET
    """


def p_multiple_bracket_array(p):
    """
        multiple_bracket_array :  sized_bracket_array multiple_bracket_array
                                | sized_bracket_array
    """


# Types
def p_data_type(p):
    """
        data_type : type
        | pointer
    """


def p_type(p):
    """
        type : primitive_types
             | user_types
    """


def p_primitive_types(p):
    """
        primitive_types : TYPE_CHAR
            |  TYPE_DOUBLE
            |  TYPE_FLOAT
            |  TYPE_INT
            |  TYPE_LONG
            |  TYPE_SHORT
            |  TYPE_VOID
    """


def p_user_types(p):
    """
        user_types : IDENTIFIER
                    | KEYWORD_STRUCT IDENTIFIER
    """


def p_pointer(p):
    """
        pointer : type TIMES multiple_pointer
                | type TIMES
    """


def p_multiple_pointer(p):
    """
        multiple_pointer : TIMES multiple_pointer
                         | TIMES
    """


# Fim dos tipos

def p_error(p):
    if p:
        print("Erro de sintaxe na linha %d: %s" % (p.lineno, p.value))
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")
    exit(1)


def main():
    l = lex.lex()
    l.input("""
        
        void teste();
    
        int main(int argc, char * argv[]){
            int a[1];
            {
                char *** a = "Da quele jeito";
            }
            
            while(int a = 0)
                while(a > 10){
                    while(a < 90){
                        float PI = 10;
                    }
                }
            
            struct Person p; 
            Person p;
            void * a;
            void * b;
        }
        
        int fatorial(int a){
            int result = 1;
            int i = 1;
            while(i <= a){
                result = result * i;
            }
            
        }
    """)
    parser = ply.yacc.yacc(debug=True)
    result = parser.parse()


if __name__ == "__main__":
    main()
    print("Nenhum erro sintático detectado")
