from lex_luthor import *
import ply.yacc


def p_program(p):
    """
        program : function_declaration program
                | function program
                | empty
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
                | empty
    """


def p_command(p):
    """
        command : data_definition SEMICOLON
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
    """


def p_parameters_list(p):
    """
            parameters_list : data_definition COMMA parameters_list
            | data_definition
            | array_definition
            | array_declaration
            | empty
    """


def p_array_declaration(p):
    """
        array_declaration : type IDENTIFIER LBRACKET RBRACKET
                          | pointer IDENTIFIER LBRACKET RBRACKET
    """


def p_data_definition(p):
    """
        data_definition : type IDENTIFIER
                        | pointer IDENTIFIER
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


def p_type(p):
    """
        type : TYPE_CHAR
            |  TYPE_DOUBLE
            |  TYPE_FLOAT
            |  TYPE_INT
            |  TYPE_LONG
            |  TYPE_SHORT
            |  TYPE_VOID
    """


def p_pointer(p):
    """
        pointer : type TIMES multiple_pointer
    """


def p_multiple_pointer(p):
    """
        multiple_pointer : TIMES multiple_pointer 
        | empty
    """


def p_empty(p):
    """empty : """
    p[0] = None


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
            void * a;
            void * b;
        }
        
        int fatorial(int a){
            int a;
        }
    """)
    parser = ply.yacc.yacc(debug=True)
    result = parser.parse()


if __name__ == "__main__":
    main()
    print("Nenhum erro sintático detectado")