from Projeto.lex.lex_luthor import *
import ply.yacc
import Projeto.abstractSintax.abstractSintax as AbsSintax


def p_program(p):
    """
        program : program_item
                | program_item program
    """

    if len(p) == 2:
        p[0] = AbsSintax.ProgramProgramItem(p[1])
    else:
        p[0] = AbsSintax.ProgramMultipleProgramItem(p[1], p[2])


def p_program_variable_declaration(p):
    """
        program_item : variable_declaration_list SEMICOLON
    """
    p[0] = AbsSintax.ProgramItemVairableDeclaration(p[1])


def p_program_function(p):
    """
        program_item : function
    """
    p[0] = AbsSintax.ProgramItemFunction(p[1])


def p_program_assign(p):
    """
        program_item : global_assign_identifier_list
    """
    p[0] = AbsSintax.ProgramItemAssign(p[1])


def p_program_type(p):
    """
        program_item : type SEMICOLON
    """
    p[0] = AbsSintax.ProgramItemType(p[1])


def p_global_assign_identifier_list(p):
    """
        global_assign_identifier_list : IDENTIFIER ASSIGN expression
                                      | IDENTIFIER ASSIGN expression COMMA global_assign_identifier_list
    """
    if len(p) == 4:
        p[0] = AbsSintax.GlobalAssignMultiplesIdentifiers(p[1], p[3], None)
    else:
        p[0] = AbsSintax.GlobalAssignMultiplesIdentifiers(p[1], p[3], p[5])


# Copiado do java
def p_block(p):
    """
        block : LBRACE RBRACE
              | LBRACE block_statements RBRACE
    """
    if len(p) == 3:
        p[0] = AbsSintax.BlockToEmptyBlock()
    else:
        p[0] = AbsSintax.BlockToBlockWithStatements(p[2])


def p_block_statements(p):
    """
        block_statements : block_statement
                        | block_statements block_statement
    """
    if len(p) == 2:
        p[0] = AbsSintax.BlockStatementsToBlockStatement(p[1])
    else:
        p[0] = AbsSintax.BlockStatementsToMultipleBlockStatements(p[1], p[2])


def p_block_statement(p):
    """
        block_statement : statement
    """
    p[0] = AbsSintax.BlockStatementToStatement(p[1])


def p_statement(p):
    """
        statement : statement_without_trailing_substatement
    """
    p[0] = AbsSintax.StatementToStatementWithoutTrailingSubstatement(p[1])


def p_statement_to_if_then_statement(p):
    """
        statement : if_then_statement
    """
    p[0] = AbsSintax.StatementToIfThenStatement(p[1])


def p_statement_to_if_then_else_statement(p):
    """
        statement : if_then_else_statement
    """
    p[0] = AbsSintax.StatementToIfThenElseStatement(p[1])


def p_statement_to_while_statement(p):
    """
        statement : while_statement
    """
    p[0] = AbsSintax.StatementToWhileStatement(p[1])


def p_statement_to_for_statement(p):
    """
        statement : for_statement
    """
    p[0] = AbsSintax.StatementToForStatement(p[1])


def p_statement_without_trailing_substatement(p):
    """
        statement_without_trailing_substatement : block
    """
    p[0] = AbsSintax.SWTSToBlockStatement(p[1])


def p_swts_to_semicolon(p):
    """
        statement_without_trailing_substatement : SEMICOLON
    """
    p[0] = AbsSintax.SWTSToSemicolonStatement()


def p_swts_to_expression_list(p):
    """
        statement_without_trailing_substatement : expression_list SEMICOLON
    """
    p[0] = AbsSintax.SWTSToExpressionListStatement(p[1])


def p_swts_to_switch_stm(p):
    """
        statement_without_trailing_substatement : switch_stm
    """
    p[0] = AbsSintax.SWTSToSwitchStatement(p[1])


def p_swts_to_do_statement(p):
    """
        statement_without_trailing_substatement : do_statement
    """
    p[0] = AbsSintax.SWTSToDoStatement(p[1])


def p_swts_to_break(p):
    """
        statement_without_trailing_substatement : KEYWORD_BREAK SEMICOLON
    """
    p[0] = AbsSintax.SWTSToBreakStatement()


def p_swts_to_continue(p):
    """
        statement_without_trailing_substatement : KEYWORD_CONTINUE SEMICOLON
    """
    p[0] = AbsSintax.SWTSToContinueStatement()


def p_swts_to_return_stm(p):
    """
        statement_without_trailing_substatement : return_stm SEMICOLON
    """
    p[0] = AbsSintax.SWTSToReturnStatement(p[1])


def p_swts_to_label(p):
    """
        statement_without_trailing_substatement : IDENTIFIER COLON
    """
    p[0] = AbsSintax.SWTSToLabelStatement(p[1])


def p_swts_to_goto(p):
    """
        statement_without_trailing_substatement : KEYWORD_GOTO IDENTIFIER SEMICOLON
    """
    p[0] = AbsSintax.SWTSToGotoStatement(p[2])


def p_swts_to_variable_declaration_list(p):
    """
        statement_without_trailing_substatement : variable_declaration_list SEMICOLON
    """
    p[0] = AbsSintax.SWTSToVariableDeclarationStatement(p[1])


def p_swts_to_type(p):
    """
        statement_without_trailing_substatement : type SEMICOLON
    """
    p[0] = AbsSintax.SWTSToTypeDeclarationStatement(p[1])


def p_statement_no_short_if(p):
    """
        statement_no_short_if : statement_without_trailing_substatement
    """
    p[0] = AbsSintax.SNSIStatementWithoutTrailingSubstatementNoShortIf(p[1])


def p_statement_no_short_if_2(p):
    """
        statement_no_short_if : if_then_else_statement_no_short_if
    """
    p[0] = AbsSintax.SNSIIfThenElseStatementNoShortIf(p[1])


def p_statement_no_short_if_3(p):
    """
        statement_no_short_if : while_statement_no_short_if
    """
    p[0] = AbsSintax.SNSIWhileStatementNoShortIf(p[1])


def p_statement_no_short_if_4(p):
    """
        statement_no_short_if : for_statement_no_short_if
    """
    p[0] = AbsSintax.SNSIForStatementNoShortIf(p[1])


def p_if_then_statement(p):
    """
        if_then_statement : KEYWORD_IF LPAREN expression RPAREN statement
    """
    p[0] = AbsSintax.IfThenStatementConcrete(p[3], p[5])


def p_if_then_else_statement(p):
    """
        if_then_else_statement : KEYWORD_IF LPAREN expression RPAREN statement_no_short_if KEYWORD_ELSE statement
    """
    p[0] = AbsSintax.IfThenElseStatementConcrete(p[3], p[5], p[7])


def p_if_then_else_statement_no_short_if(p):
    """
        if_then_else_statement_no_short_if : KEYWORD_IF LPAREN expression RPAREN statement_no_short_if KEYWORD_ELSE statement_no_short_if
    """
    p[0] = AbsSintax.IfThenElseStatementNoShortIfConcrete(p[3], p[5], p[7])


def p_while_statement(p):
    """
        while_statement : KEYWORD_WHILE LPAREN expression RPAREN statement
    """
    p[0] = AbsSintax.WhileStatementConcrete(p[3], p[5])


def p_while_statement_no_short_if(p):
    """
        while_statement_no_short_if : KEYWORD_WHILE LPAREN expression RPAREN statement_no_short_if
    """
    p[0] = AbsSintax.WhileStatementNoShortIfConcrete(p[3], p[5])


def p_do_statement(p):
    """
        do_statement : KEYWORD_DO statement KEYWORD_WHILE LPAREN expression RPAREN SEMICOLON
    """
    p[0] = AbsSintax.DoStatementConcrete(p[2], p[5])


def p_for_params_1(p):
    """
        for_params : variable_declaration_list SEMICOLON for_param
    """
    p[0] = AbsSintax.ForParamsWithVariableDeclaration(p[1], p[3])


def p_for_params_2(p):
    """
        for_params : variable_declaration_list SEMICOLON for_param expression_list
    """
    p[0] = AbsSintax.ForParamsWithVariableDeclaration(p[1], p[3], p[4])


def p_for_params_3(p):
    """
        for_params : for_param for_param expression_list
    """
    p[0] = AbsSintax.ForParamsWithoutVariableDeclaration(p[1], p[2], p[3])


def p_for_params_4(p):
    """
        for_params : for_param for_param
    """
    p[0] = AbsSintax.ForParamsWithoutVariableDeclaration(p[1], p[2])


def p_for_param(p):
    """
        for_param : SEMICOLON
                  | expression_list SEMICOLON
    """
    if len(p) == 3:
        p[0] = AbsSintax.ExpressionListForParam(p[1])
    else:
        p[0] = AbsSintax.SemicolonForParam()


def p_for_statement(p):
    """
        for_statement : KEYWORD_FOR LPAREN for_params RPAREN statement
    """
    p[0] = AbsSintax.ForStatementConcrete(p[3], p[5])


def p_for_statement_no_short_if(p):
    """
        for_statement_no_short_if : KEYWORD_FOR LPAREN for_params RPAREN statement_no_short_if
    """
    p[0] = AbsSintax.ForStatementNoShortIfConcrete(p[3], p[5])


def p_switch_stm(p):
    """
        switch_stm : KEYWORD_SWITCH LPAREN expression RPAREN LBRACE switch_itens RBRACE
    """
    p[0] = AbsSintax.SwitchStatementConcrete(p[3], p[6])


def p_switch_itens_1(p):
    """
        switch_itens : KEYWORD_CASE expression COLON block_statements
    """
    p[0] = AbsSintax.CaseSwitchItem(p[2], p[4])


def p_switch_itens_2(p):
    """
        switch_itens : KEYWORD_DEFAULT COLON block_statements
    """
    p[0] = AbsSintax.DefaultSwitchItem(p[3])


def p_switch_itens_3(p):
    """
        switch_itens : KEYWORD_CASE expression COLON block_statements switch_itens
    """
    p[0] = AbsSintax.CaseSwitchItem(p[2], p[4], p[5])


def p_switch_itens_4(p):
    """
        switch_itens : KEYWORD_DEFAULT COLON block_statements switch_itens
    """
    p[0] = AbsSintax.DefaultSwitchItem(p[3], p[4])


def p_return_stm(p):
    """
        return_stm : KEYWORD_RETURN
                    | KEYWORD_RETURN expression
    """
    if len(p) == 3:
        p[0] = AbsSintax.ReturnWithExpression(p[2])
    else:
        p[0] = AbsSintax.ReturnWithoutExpression()


def p_function(p):
    """
        function : function_signature block
    """
    p[0] = AbsSintax.FunctionConcrete(p[1], p[2])


def p_funcion_signature(p):
    """
        function_signature : type identifier LPAREN signature_param_list RPAREN
                           | type identifier LPAREN RPAREN
    """
    if len(p) == 6:
        p[0] = AbsSintax.FunctionSignatureWithParams(p[1], p[2], p[4])
    elif len(p) == 5:
        p[0] = AbsSintax.FunctionSignatureWithoutParams(p[1], p[2])


def p_triple_dot(p):
    """
        triple_dot : DOT DOT DOT
    """
    p[0] = AbsSintax.TripleDotConcrete()


def p_signature_param_list(p):
    """
        signature_param_list : signature_param COMMA signature_param_list
                             | signature_param

    """
    if len(p) == 2:
        p[0] = AbsSintax.SignatureParamListWithSingleParam(p[1])
    else:
        p[0] = AbsSintax.SignatureParamListWithMoreParams(p[1], p[3])


def p_signature_param_1(p):
    """
        signature_param : type
    """
    p[0] = AbsSintax.TypeOnlySignatureParam(p[1])


def p_signature_param_2(p):
    """
        signature_param : type multiple_times
    """
    p[0] = AbsSintax.TypeWithMultipleTimesSignatureParam(p[1], p[2])


def p_signature_param_3(p):
    """
        signature_param : type multiple_bracket_signature
    """
    p[0] = AbsSintax.TypeWithMultipleBracketSignatureParam(p[1], p[2])


def p_signature_param_4(p):
    """
        signature_param : type identifier
    """
    p[0] = AbsSintax.TypeWithIdentifierSignatureParam(p[1], p[2])


def p_signature_param_5(p):
    """
        signature_param : type identifier multiple_bracket_signature
    """
    p[0] = AbsSintax.TypeWithIdentifierSignatureParam(p[1], p[2], p[3])


def p_signature_param_6(p):
    """
        signature_param : triple_dot
    """
    p[0] = AbsSintax.TripleDotSignatureParam()


def p_multiple_bracket_signature_1(p):
    """
        multiple_bracket_signature : LBRACKET RBRACKET multiple_bracket_signature
    """
    p[0] = AbsSintax.EmptyBracketMultipleBracketSignature(p[3])


def p_multiple_bracket_signature_2(p):
    """
        multiple_bracket_signature : LBRACKET RBRACKET
    """
    p[0] = AbsSintax.EmptyBracketMultipleBracketSignature()


def p_multiple_bracket_signature_3(p):
    """
        multiple_bracket_signature : bracket_with_bounds multiple_bracket_signature
    """
    p[0] = AbsSintax.BracketWithBoundsMultipleBracketSignature(p[1], p[2])


def p_multiple_bracket_signature_4(p):
    """
        multiple_bracket_signature : bracket_with_bounds
    """
    p[0] = AbsSintax.BracketWithBoundsMultipleBracketSignature(p[1])


def p_bracket_with_bounds(p):
    """
        bracket_with_bounds : LBRACKET number_id RBRACKET
    """
    p[0] = AbsSintax.BracketWithBoundsConcrete(p[2])


def p_number_id_1(p):
    """
        number_id : IDENTIFIER
    """
    p[0] = AbsSintax.IdentifierNumberId(p[1])


def p_number_id_2(p):
    """
        number_id : integer_number
    """
    p[0] = AbsSintax.IntegerNumberNumberId(p[1])


def p_value_list(p):
    """
        value_list : LBRACE value_list_item RBRACE
                    | LBRACE RBRACE
    """
    if len(p) == 4:
        p[0] = AbsSintax.ValueListConcrete(p[2])
    elif len(p) == 3:
        p[0] = AbsSintax.ValueListConcrete()


def p_value_list_item1(p):
    """
        value_list_item : expression
                        | expression COMMA value_list_item

    """
    if len(p) == 2:
        p[0] = AbsSintax.ValueListItem(p[1])
    elif len(p) == 4:
        p[0] = AbsSintax.ValueListItem(p[1], p[3])


def p_value_list_item2(p):
    """
        value_list_item :  value_list
                        | value_list COMMA value_list_item
    """
    if len(p) == 2:
        p[0] = AbsSintax.ValueListItem(p[1])
    elif len(p) == 4:
        p[0] = AbsSintax.ValueListItem(p[1], p[3])


def p_variable_declaration_list(p):
    """
        variable_declaration_list : type identifier_list
    """
    p[0] = AbsSintax.VariableDeclarationListConcrete(p[1], p[2])


def p_identifier_list(p):
    """
        identifier_list : identifier
                        | identifier COMMA identifier_list
    """
    if len(p) == 2:
        p[0] = AbsSintax.IdentifierListConcrete(p[1])
    elif len(p) == 4:
        p[0] = AbsSintax.IdentifierListConcrete(p[1], p[3])


def p_identifier_list_array(p):
    """
        identifier_list : identifier multiple_bracket_signature
                         | identifier multiple_bracket_signature COMMA identifier_list
    """
    if len(p) == 3:
        p[0] = AbsSintax.IdentifierArrayList(p[1], p[2])
    elif len(p) == 5:
        p[0] = AbsSintax.IdentifierArrayList(p[1], p[2], p[4])


def p_assign_identifier_list(p):
    """
        identifier_list : identifier ASSIGN expression
                        | identifier ASSIGN expression COMMA identifier_list
    """
    if len(p) == 4:
        p[0] = AbsSintax.IdentifierWithAssignList(p[1], p[3])
    elif len(p) == 6:
        p[0] = AbsSintax.IdentifierWithAssignList(p[1], p[3], p[5])


def p_assign_identifier_list_array(p):
    """
        identifier_list : identifier multiple_bracket_signature ASSIGN value_list
                       | identifier multiple_bracket_signature ASSIGN value_list COMMA identifier_list
    """
    if len(p) == 5:
        p[0] = AbsSintax.IdentifierAssignArrayList(p[1], p[2], p[4])
    elif len(p) == 7:
        p[0] = AbsSintax.IdentifierAssignArrayList(p[1], p[2], p[4], p[6])


def p_assign_identifier_list_non_array(p):
    """
        identifier_list : identifier ASSIGN value_list
                        | identifier ASSIGN value_list COMMA identifier_list
    """
    if len(p) == 4:
        p[0] = AbsSintax.IdentifierAssignValueList(p[1], p[3])
    elif len(p) == 6:
        p[0] = AbsSintax.IdentifierAssignValueList(p[1], p[3], p[5])


def p_identifier_list_function_pointer(p):
    """
        identifier_list : function_pointer
                        | function_pointer COMMA identifier_list
    """
    if len(p) == 2:
        p[0] = AbsSintax.IdentifierListFunctionPointer(p[1])
    elif len(p) == 4:
        p[0] = AbsSintax.IdentifierListFunctionPointer(p[1], p[3])


def p_identifier_list_function_pointer_assign(p):
    """
        identifier_list : function_pointer ASSIGN expression
                        | function_pointer ASSIGN expression COMMA identifier_list
    """
    if len(p) == 4:
        p[0] = AbsSintax.IdentifierListFunctionPointerAssign(p[1], p[3])
    elif len(p) == 6:
        p[0] = AbsSintax.IdentifierListFunctionPointerAssign(p[1], p[3], p[5])


def p_identifier_list_function_pointer_array(p):
    """
        identifier_list : function_pointer_array
                        | function_pointer_array COMMA identifier_list
    """
    if len(p) == 2:
        p[0] = AbsSintax.IdentifierListFunctionPointerArray(p[1])
    elif len(p) == 4:
        p[0] = AbsSintax.IdentifierListFunctionPointerArray(p[1], p[3])


def p_identifier_list_function_pointer_array_assing(p):
    """
        identifier_list : function_pointer_array ASSIGN value_list
                        | function_pointer_array ASSIGN value_list COMMA identifier_list
    """
    if len(p) == 4:
        p[0] = AbsSintax.IdentifierListFunctionPointerArrayAssign(p[1], p[3])
    elif len(p) == 6:
        p[0] = AbsSintax.IdentifierListFunctionPointerArrayAssign(p[1], p[3], p[5])


def p_function_pointer(p):
    """
        function_pointer : identifier LPAREN signature_param_list RPAREN
                         | identifier LPAREN RPAREN
    """
    if len(p) == 5:
        p[0] = AbsSintax.FunctionPointerConcrete(p[1], p[3])
    elif len(p) == 4:
        p[0] = AbsSintax.FunctionPointerConcrete(p[1])


def p_function_pointer_array(p):
    """
        function_pointer_array : LPAREN TIMES identifier multiple_bracket_signature RPAREN LPAREN signature_param_list RPAREN
                               | LPAREN TIMES identifier multiple_bracket_signature RPAREN LPAREN RPAREN
    """
    if len(p) == 9:
        p[0] = AbsSintax.FunctionPointerArrayConcrete(p[3], p[4], p[7])
    elif len(p) == 8:
        p[0] = AbsSintax.FunctionPointerArrayConcrete(p[3], p[4])


def p_identifier_1(p):
    """
        identifier : IDENTIFIER
    """
    p[0] = AbsSintax.IdentifierOnly(p[1])


def p_identifier_2(p):
    """
        identifier : TIMES identifier
    """
    p[0] = AbsSintax.IdentifierTimesIdentifier(p[2])


def p_identifier_3(p):
    """
        identifier : LPAREN identifier RPAREN
    """
    p[0] = AbsSintax.IdentifierWithParentesis(p[2])


def p_type_1(p):
    """
        type : user_types
    """
    p[0] = AbsSintax.TypeUserType(p[1])


def p_type_2(p):
    """
        type : primitive_types
    """
    p[0] = AbsSintax.TypePrimitiveType(p[1])


def p_type_3(p):
    """
        type : type_modifier type
    """
    p[0] = AbsSintax.TypeWithModifier(p[1], p[2])


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
    p[0] = AbsSintax.TypeModifierConcrete(p[1])


def p_user_types_1(p):
    """
        user_types : struct_declaration
    """
    p[0] = AbsSintax.StructDeclarationUserType(p[1])


def p_user_types_2(p):
    """
        user_types : union_declaration
    """
    p[0] = AbsSintax.UnionDeclarationUserType(p[1])


def p_user_types_3(p):
    """
        user_types : enum_declaration
    """
    p[0] = AbsSintax.EnumDeclarationUserType(p[1])


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
    p[0] = AbsSintax.PrimitiveTypeConcrete(p[1])


def p_struct_declaration_1(p):
    """
        struct_declaration : KEYWORD_STRUCT IDENTIFIER LBRACE RBRACE
    """
    p[0] = AbsSintax.NamedStructDeclaration(p[2])


def p_struct_declaration_2(p):
    """
        struct_declaration : KEYWORD_STRUCT IDENTIFIER LBRACE struct_or_union_member_list RBRACE
    """
    p[0] = AbsSintax.NamedStructDeclaration(p[2], p[4])


def p_struct_declaration_3(p):
    """
        struct_declaration : KEYWORD_STRUCT LBRACE RBRACE
    """
    p[0] = AbsSintax.UnamedStructDeclaration()


def p_struct_declaration_4(p):
    """
        struct_declaration : KEYWORD_STRUCT LBRACE struct_or_union_member_list RBRACE
    """
    p[0] = AbsSintax.UnamedStructDeclaration(p[3])


def p_struct_declaration_5(p):
    """
        struct_declaration : KEYWORD_STRUCT IDENTIFIER
    """
    p[0] = AbsSintax.StructDeclarationOnlyIdentifier(p[2])


def p_union_declaration_1(p):
    """
        union_declaration : KEYWORD_UNION IDENTIFIER LBRACE RBRACE
    """
    p[0] = AbsSintax.NamedUnionDeclaration(p[2])


def p_union_declaration_2(p):
    """
        union_declaration : KEYWORD_UNION IDENTIFIER LBRACE struct_or_union_member_list RBRACE
    """
    p[0] = AbsSintax.NamedUnionDeclaration(p[2], p[4])


def p_union_declaration_3(p):
    """
        union_declaration : KEYWORD_UNION LBRACE RBRACE
    """
    p[0] = AbsSintax.UnamedStructDeclaration()


def p_union_declaration_4(p):
    """
        union_declaration : KEYWORD_UNION LBRACE struct_or_union_member_list RBRACE
    """
    p[0] = AbsSintax.UnamedStructDeclaration(p[3])


def p_union_declaration_5(p):
    """
        union_declaration : KEYWORD_UNION IDENTIFIER
    """
    p[0] = AbsSintax.UnionDeclarationOnlyIdentifier(p[2])


def p_enum_declaration_1(p):
    """
        enum_declaration : KEYWORD_ENUM LBRACE enum_item_list RBRACE
    """
    p[0] = AbsSintax.UnamedEnumDeclaration(p[3])


def p_enum_declaration_2(p):
    """
        enum_declaration : KEYWORD_ENUM IDENTIFIER LBRACE enum_item_list RBRACE
    """
    p[0] = AbsSintax.NamedEnumDeclaration(p[2], p[4])


def p_enum_declaration_3(p):
    """
        enum_declaration : KEYWORD_ENUM IDENTIFIER
    """
    p[0] = AbsSintax.EnumDeclarationOnlyIdentifier(p[2])


def p_struct_or_union_member_list(p):
    """
        struct_or_union_member_list : variable_declaration_list_no_assign SEMICOLON
                                   | variable_declaration_list_no_assign SEMICOLON struct_or_union_member_list
    """
    if len(p) == 3:
        p[0] = AbsSintax.StructOrUnionMemberListConcrete(p[1])
    else:
        p[0] = AbsSintax.StructOrUnionMemberListConcrete(p[1], p[3])


def p_variable_declaration_list_no_assign(p):
    """
        variable_declaration_list_no_assign : type variable_list_no_assign
    """
    p[0] = AbsSintax.VariableDeclarationListNoAssignConcrete(p[1], p[2])


def p_variable_list_no_assign(p):
    """
        variable_list_no_assign : identifier
                                | variable_list_no_assign COMMA identifier
    """
    if len(p) == 2:
        p[0] = AbsSintax.VariableListNoAssignConcrete(p[1])
    else:
        p[0] = AbsSintax.VariableListNoAssignConcrete(p[3], p[1])


def p_enum_item_list_1(p):
    """
        enum_item_list : IDENTIFIER
    """
    p[0] = AbsSintax.EnumItemListIdentifier(p[1])


def p_enum_item_list_2(p):
    """
        enum_item_list : IDENTIFIER COMMA enum_item_list
    """
    p[0] = AbsSintax.EnumItemListIdentifier(p[1], p[3])


def p_enum_item_list_3(p):
    """
        enum_item_list : IDENTIFIER ASSIGN expression
    """
    p[0] = AbsSintax.EnumItemListIdentifierAssignExpression(p[1], p[3])


def p_enum_item_list_4(p):
    """
        enum_item_list : IDENTIFIER ASSIGN expression COMMA enum_item_list
    """
    p[0] = AbsSintax.EnumItemListIdentifierAssignExpression(p[1], p[3], p[5])


def p_multiple_times(p):
    """
        multiple_times : TIMES multiple_times
                        | TIMES
    """
    if len(p) == 3:
        p[0] = AbsSintax.MultipleTimesConcrete(p[2])
    else:
        p[0] = AbsSintax.MultipleTimesConcrete()


def p_integer_number(p):
    """
        integer_number : NUMBER
                       | BINARY_NUMBER
                       | HEXADECIMAL_NUMBER
                       | OCTAL_NUMBER
    """
    p[0] = AbsSintax.IntegerNumberConcrete(p[1])


def p_expression_list(p):
    """
        expression_list : expression
                        | expression COMMA expression_list
    """
    if len(p) == 2:
        p[0] = AbsSintax.ExpressionListConcrete(p[1])
    else:
        p[0] = AbsSintax.ExpressionListConcrete(p[1], p[3])


def p_expression(p):
    """
        expression : assign_exp
    """
    p[0] = AbsSintax.ExpressionConcrete(p[1])


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
    p[0] = AbsSintax.AssignmentOperatorConcrete(p[1])


def p_assign_exp(p):
    """
        assign_exp : unary_exp assign_operator assign_exp
                    | ternary_conditional_exp
    """
    if len(p) == 3:
        p[0] = AbsSintax.AssignExpressionRecursion(p[1], p[2], p[3])
    else:
        p[0] = AbsSintax.AssignExpressionToTernary(p[1])


def p_ternary_conditional_exp(p):
    """
        ternary_conditional_exp : logical_exp QUESTION_MARK expression COLON ternary_conditional_exp
                                | logical_exp
    """
    if len(p) == 6:
        p[0] = AbsSintax.TernaryConditionalExpressionRecursion(p[1], p[3], p[5])
    else:
        p[0] = AbsSintax.TernaryConditionalExpressionToLogicalExpression(p[1])


def p_logical_exp(p):
    """
        logical_exp : logical_or_exp
    """
    p[0] = AbsSintax.LogicalExpressionConcrete(p[1])


def p_logical_or_exp(p):
    """
        logical_or_exp : logical_or_exp LOGICAL_OR logical_and_exp
                        | logical_and_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.LogicalOrExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.LogicalOrExpressionToAndExpression(p[1])


def p_logical_and_exp(p):
    """
        logical_and_exp : logical_and_exp LOGICAL_AND bitwise_or_exp
                        | bitwise_or_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.LogicalAndExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.LogicalAndExpressionToBitwiseOrExpression(p[1])


def p_bitwise_or_exp(p):
    """
        bitwise_or_exp : bitwise_or_exp BITWISE_OR bitwise_xor_exp
                        | bitwise_xor_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.BitwiseOrExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.BitwiseOrExpressionToXorBitwiseExpression(p[1])


def p_bitwise_xor_exp(p):
    """
        bitwise_xor_exp : bitwise_xor_exp BITWISE_XOR bitwise_and_exp
                        | bitwise_and_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.BitwiseXorExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.BitwiseXorExpressionToBitwiseAndExpression(p[1])


def p_bitwise_and_exp(p):
    """
        bitwise_and_exp : bitwise_and_exp BITWISE_AND is_equals_exp
                        | is_equals_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.BitwiseAndExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.BitwiseAndExpressionToEqualsExpression(p[1])


def p_is_equals_exp(p):
    """
        is_equals_exp : is_equals_exp EQUALS_THEN is_not_equals_exp
                       | is_not_equals_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.IsEqualsExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.IsEqualsExpressionToNotEqualsExpression(p[1])


def p_is_not_equals(p):
    """
        is_not_equals_exp : is_not_equals_exp NOT_EQUALS greater_then_exp
                          | greater_then_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.IsNotEqualsExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.IsNotEqualsExpressionToGreaterThenExpression(p[1])


def p_greater_then_exp(p):
    """
        greater_then_exp : greater_then_exp GREATER_THEN greater_equals_exp
                         | greater_equals_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.GreaterThenExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.GreaterThenExpressionToGreaterEqualsExpression(p[1])


def p_greater_equals_exp(p):
    """
         greater_equals_exp : greater_equals_exp GREATER_EQUALS less_then_exp
                            | less_then_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.GreaterEqualsExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.GreaterEqualsExpressionToLessThenExpression(p[1])


def p_less_then_exp(p):
    """
        less_then_exp : less_then_exp LESS_THEN less_equals_exp
                      | less_equals_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.LessThenExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.LessThenExpressionToLessEqualsExpression(p[1])


def p_less_equals_exp(p):
    """
        less_equals_exp : less_equals_exp LESS_EQUALS left_shift_exp
                        | left_shift_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.LessEqualsExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.LessEqualsExpressionToLeftShiftExpression(p[1])


def p_left_shift_exp(p):
    """
        left_shift_exp : left_shift_exp BITWISE_SHIFT_LEFT right_shift_exp
                        | right_shift_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.LeftShiftExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.LeftShiftExpressionToRightShiftExpression(p[1])


def p_right_shift_exp(p):
    """
        right_shift_exp : right_shift_exp BITWISE_SHIFT_RIGHT plus_exp
                        | plus_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.RightShiftExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.RightShiftExpressionToPlusExpression(p[1])


def p_plus_exp(p):
    """
        plus_exp : plus_exp PLUS minus_exp
                 | minus_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.PlusExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.PlusExpressionToMinusExpression(p[1])


def p_minus_exp(p):
    """
        minus_exp : minus_exp MINUS times_exp
                 | times_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.MinusExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.MinusExpressionToTimesExpression(p[1])


def p_times_exp(p):
    """
        times_exp : times_exp TIMES divide_exp
                 | divide_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.TimesExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.TimesExpressionToDivideExpression(p[1])


def p_divide_exp(p):
    """
        divide_exp : divide_exp DIVIDE modulus_exp
                    | modulus_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.DivideExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.DivideExpressionToModulusExpression(p[1])


def p_modulus_exp(p):
    """
        modulus_exp : modulus_exp MODULUS unary_exp
                    | unary_exp
    """
    if len(p) == 4:
        p[0] = AbsSintax.ModulusExpressionRecursion(p[1], p[3])
    else:
        p[0] = AbsSintax.ModulusExpressionToUnaryExpression(p[1])


def p_unary_operator(p):
    """
        unary_operator : BITWISE_AND
                       | TIMES
                       | PLUS
                       | MINUS
                       | BITWISE_COMPLEMENT
                       | NOT
    """
    p[0] = AbsSintax.UnaryOperatorConcrete(p[1])


def p_unary_exp_1(p):
    """
        unary_exp : postfix_exp
    """
    p[0] = AbsSintax.UnaryToPostifix(p[1])


def p_unary_exp_2(p):
    """
        unary_exp : INCREMENT postfix_exp
    """
    p[0] = AbsSintax.UnaryPreIncrementPostfixExpression(p[2])


def p_unary_exp_3(p):
    """
        unary_exp : DECREMENT postfix_exp
    """
    p[0] = AbsSintax.UnaryPreDecrementPostfixExpression(p[2])


def p_unary_exp_4(p):
    """
        unary_exp : postfix_exp INCREMENT
    """
    p[0] = AbsSintax.UnaryPostIncrementPostfixExpression(p[1])


def p_unary_exp_5(p):
    """
        unary_exp : postfix_exp DECREMENT
    """
    p[0] = AbsSintax.UnaryPostDecrementPostfixExpression(p[1])


def p_unary_exp_6(p):
    """
        unary_exp : cast_exp postfix_exp
    """
    p[0] = AbsSintax.UnaryCastExpressionPostfixExpression(p[1], p[2])


def p_unary_exp_7(p):
    """
        unary_exp : sizeof_exp
    """
    p[0] = AbsSintax.SizeofExpressionUnary(p[1])


def p_unary_exp_8(p):
    """
        unary_exp : unary_operator unary_exp
    """
    p[0] = AbsSintax.UnaryOperatorUnaryExpression(p[1], p[2])


def p_sizeof_exp(p):
    """
        sizeof_exp :  KEYWORD_SIZEOF postfix_exp
                    | KEYWORD_SIZEOF LPAREN type RPAREN
                    | KEYWORD_SIZEOF LPAREN type multiple_times RPAREN
    """
    if len(p) == 3:
        p[0] = AbsSintax.SizeofPostfixExpression(p[2])
    elif len(p) == 5:
        p[0] = AbsSintax.SizeofTypeExpression(p[3])
    else:
        p[0] = AbsSintax.SizeofTypeExpression(p[3], p[4])


def p_cast_exp(p):
    """
        cast_exp : LPAREN type RPAREN
                 | LPAREN type multiple_times RPAREN
    """
    if len(p) == 4:
        p[0] = AbsSintax.CastExpressionType(p[2])
    else:
        p[0] = AbsSintax.CastExpressionType(p[2], p[3])


def p_postfix_exp_1(p):
    """
        postfix_exp : postfix_exp LBRACKET expression RBRACKET
    """
    p[0] = AbsSintax.PostfixExpressionBracket(p[1], p[3])


def p_postfix_exp_2(p):
    """
        postfix_exp : postfix_exp LPAREN RPAREN
    """
    p[0] = AbsSintax.PostfixExpressionFunctionCallNoParams(p[1])


def p_postfix_exp_3(p):
    """
        postfix_exp : postfix_exp LPAREN function_call_parameters RPAREN
    """
    p[0] = AbsSintax.PostfixExpressionParenFunctionCall(p[1], p[3])


def p_postfix_exp_4(p):
    """
        postfix_exp : postfix_exp DOT IDENTIFIER
    """
    p[0] = AbsSintax.PostfixExpressionDot(p[1], p[3])


def p_postfix_exp_5(p):
    """
        postfix_exp : postfix_exp ARROW IDENTIFIER
    """
    p[0] = AbsSintax.PostfixExpressionArrow(p[1], p[3])


def p_postfix_exp_6(p):
    """
        postfix_exp : primary_exp
    """
    p[0] = AbsSintax.PostfixToPrimaryExpression(p[1])


def p_function_call_parameters(p):
    """
        function_call_parameters : expression
                                  | expression COMMA function_call_parameters
    """
    if len(p) == 2:
        p[0] = AbsSintax.FunctionCallParametersConcrete(p[1])
    else:
        p[0] = AbsSintax.FunctionCallParametersConcrete(p[1], p[3])


def p_primary_exp(p):
    """
        primary_exp : identifier_exp
    """
    p[0] = AbsSintax.PrimaryExpressionConcrete(p[1])


def p_identifier_exp_1(p):
    """
        identifier_exp : IDENTIFIER
    """
    p[0] = AbsSintax.IdentifierExpressionToIdentifier(p[1])


def p_identifier_exp_2(p):
    """
        identifier_exp : string_exp
    """
    p[0] = AbsSintax.IdentifierExpressionToString(p[1])


def p_string_exp_1(p):
    """
        string_exp : STRING
    """
    p[0] = AbsSintax.StringExpressionString(p[1])


def p_string_exp_2(p):
    """
        string_exp : number_exp
    """
    p[0] = AbsSintax.StringExpressionNumber(p[1])


def p_number_exp_1(p):
    """
        number_exp : integer_number
    """
    p[0] = AbsSintax.NumberToIntegerNumberExpression(p[1])


def p_number_exp_2(p):
    """
        number_exp : FLOAT_NUMBER
    """
    p[0] = AbsSintax.NumberToFloatNumberExpression(p[1])


def p_number_exp_3(p):
    """
        number_exp : CHARACTER
    """
    p[0] = AbsSintax.NumberToCharacterExpression(p[1])


def p_number_exp_4(p):
    """
        number_exp : parentesis_exp
    """
    p[0] = AbsSintax.NumberToParentesisExpression(p[1])


def p_parentesis_exp(p):
    """
        parentesis_exp : LPAREN expression RPAREN
    """
    p[0] = AbsSintax.ParenthesisExpressionConcrete(p[2])


def p_error(p):
    if p:
        print("Erro de sintaxe na linha %d: %s" % (p.lineno, p.value))
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")
    exit(1)


def main():
    _lexer = lex.lex()

    _input = ""
    with open("parser_test.c", "r") as file:
        for line in file:
            if not line.startswith('#'):
                _input += line

    _lexer.input(_input)
    parser = ply.yacc.yacc()
    parser.parse()


if __name__ == "__main__":
    main()
    print("Nenhum erro sintático detectado")
