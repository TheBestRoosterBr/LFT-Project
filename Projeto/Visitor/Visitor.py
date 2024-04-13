from AbstractVisitor import AbstractVisitor
from Projeto.parser.sintatic import *

tab = 0


def blank():
    p = ''
    for i in range(tab):
        p = p + ' '
    return p


class Visitor(AbstractVisitor):
    def visitProgramProgramItem(self, program_item):
        program_item.program_item.print()
        program_item.program_item.accept(self)

    def visitProgramMultipleProgramItem(self, program_item, program):
        program_item.program_item.accept(self)
        program.program.accept(self)

    def visitProgramItemVariableDeclaration(self, program_item):
        program_item.variable_declaration_list.accept(self)

    def visitProgramItemFunction(self, program_item):
        program_item.function.print()
        program_item.function.accept(self)
        pass

    def visitProgramItemAssign(self, program_item):
        pass

    def visitProgramItemType(self, program_item):
        pass

    def visitGlobalAssignOneIdentifier(self, global_assign):
        pass

    def visitGlobalAssignMultiplesIdentifiers(self, global_assign):
        pass

    def visitBlockToEmptyBlock(self, block):
        pass

    def visitBlockToBlockWithStatements(self, block):
        pass

    def visitBlockStatementsToBlockStatement(self, block_statements):
        pass

    def visitBlockStatementsToMultipleBlockStatements(self, block_statements):
        pass

    def visitBlockStatementToStatement(self, block_statement):
        pass

    def visitStatementToStatementWithoutTrailingSubstatement(self, statement):
        pass

    def visitStatementToIfThenStatement(self, statement):
        pass

    def visitStatementToIfThenElseStatement(self, statement):
        pass

    def visitStatementToWhileStatement(self, statement):
        pass

    def visitStatementToForStatement(self, statement):
        pass

    def visitSWTSToBlockStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToSemicolonStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToExpressionListStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToSwitchStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToDoStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToBreakStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToContinueStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToReturnStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToLabelStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToGotoStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToVariableDeclarationStatement(self, statement_without_trailing_substatement):
        pass

    def visitSWTSToTypeDeclarationStatement(self, statement_without_trailing_substatement):
        pass

    def visitSNSIStatementWithoutTrailingSubstatementNoShortIf(self, statement_no_short_if):
        pass

    def visitSNSIIfThenElseStatementNoShortIf(self, statement_no_short_if):
        pass

    def visitSNSIWhileStatementNoShortIf(self, statement_no_short_if):
        pass

    def visitSNSIForStatementNoShortIf(self, statement_no_short_if):
        pass

    def visitIfThenStatement(self, if_then_statement):
        pass

    def visitIfThenElseStatement(self, if_then_else_statement):
        pass

    def visitIfThenElseStatementNoShortIf(self, if_then_else_statement_no_short_if):
        pass

    def visitWhileStatement(self, while_statement):
        pass

    def visitWhileStatementNoShortIf(self, while_statement_no_short_if):
        pass

    def visitDoStatement(self, do_statement):
        pass

    def visitForParamsWithVariableDeclaration(self, for_params_with_variable_declaration):
        pass

    def visitForParamsWithoutVariableDeclaration(self, for_params_without_variable_declaration):
        pass

    def visitSemicolonForParam(self, semicolon_for_param):
        pass

    def visitExpressionListForParam(self, expression_list_for_param):
        pass

    def visitForStatement(self, for_statement):
        pass

    def visitForStatementNoShortIf(self, for_statement_no_short_if):
        pass

    def visitSwitchStatement(self, switch_statement):
        pass

    def visitCaseSwitchItem(self, case_switch_item):
        pass

    def visitDefaultSwitchItem(self, default_switch_item):
        pass

    def visitReturnWithoutExpression(self, return_without_expression):
        pass

    def visitReturnWithExpression(self, return_with_expression):
        pass

    def visitFunction(self, function):
        pass

    def visitFunctionSignatureWithParams(self, function_signature_with_params):
        pass

    def visitFunctionSignatureWithoutParams(self, function_signature_without_params):
        pass

    def visitTripleDot(self, triple_dot):
        pass

    def visitSignatureParamListWithMoreParams(self, signature_param_list):
        pass

    def visitSignatureParamListWithSingleParam(self, signature_param_list):
        pass

    def visitTypeOnlySignatureParam(self, signature_param):
        pass

    def visitTypeWithMultipleTimesSignatureParam(self, signature_param):
        pass

    def visitTypeWithMultipleBracketSignatureParam(self, signature_param):
        pass

    def visitTypeWithIdentifierSignatureParam(self, signature_param):
        pass

    def visitTripleDotSignatureParam(self, signature_param):
        pass

    def visitEmptyBracketMultipleBracketSignature(self, multiple_bracket_signature):
        pass

    def visitBracketWithBoundsMultipleBracketSignature(self, multiple_bracket_signature):
        pass

    def visitBracketWithBoundsConcrete(self, bracket_with_bounds):
        pass

    def visitIdentifierNumberId(self, number_id):
        pass

    def visitIntegerNumberNumberId(self, number_id):
        pass

    def visitValueListConcrete(self, value_list):
        pass

    def visitExpressionItem(self, value_list_item):
        pass

    def visitValueListItem(self, value_list_item):
        pass

    def visitVariableDeclarationListConcrete(self, variable_declaration_list):
        pass

    def visitIdentifierListConcrete(self, identifier_list):
        pass

    def visitIdentifierArrayList(self, identifier_list):
        pass

    def visitIdentifierWithAssignList(self, identifier_list):
        pass

    def visitIdentifierAssignArrayList(self, identifier_list):
        pass

    def visitIdentifierAssignValueList(self, identifier_list):
        pass

    def visitIdentifierListFunctionPointer(self, identifier_list):
        pass

    def visitIdentifierListFunctionPointerAssign(self, identifier_list):
        pass

    def visitIdentifierListFunctionPointerArray(self, identifier_list):
        pass

    def visitIdentifierListFunctionPointerArrayAssign(self, identifier_list):
        pass

    def visitFunctionPointerConcrete(self, function_pointer):
        pass

    def visitFunctionPointerArrayConcrete(self, function_pointer_array):
        pass

    def visitIdentifierOnly(self, identifier):
        pass

    def visitIdentifierTimesIdentifier(self, identifier):
        pass

    def visitIdentifierWithParentesis(self, identifier):
        pass

    def visitTypeUserType(self, _type):
        pass

    def visitTypePrimitiveType(self, _type):
        pass

    def visitTypeWithModifier(self, _type):
        pass

    def visitTypeModifierConcrete(self, type_modifier):
        pass

    def visitStructDeclarationUserType(self, user_types):
        pass

    def visitUnionDeclarationUserType(self, user_types):
        pass

    def visitEnumDeclarationUserType(self, user_types):
        pass

    def visitPrimitiveTypeConcrete(self, primitive_type):
        pass

    def visitNamedStructDeclaration(self, struct_declaration):
        pass

    def visitAnonymousStructDeclaration(self, struct_declaration):
        pass

    def visitStructDeclarationOnlyIdentifier(self, struct_declaration):
        pass

    def visitNamedUnionDeclaration(self, union_declaration):
        pass

    def visitUnamedUnionDeclaration(self, union_declaration):
        pass

    def visitUnionDeclarationOnlyIdentifier(self, union_declaration):
        pass

    def visitNamedEnumDeclaration(self, enum_declaration):
        pass

    def visitUnamedEnumDeclaration(self, enum_declaration):
        pass

    def visitEnumDeclarationOnlyIdentifier(self, enum_declaration):
        pass

    def visitStructOrUnionMemberListConcrete(self, struct_or_union_member_list):
        pass

    def visitVariableListNoAssignConcrete(self, variable_list_no_assign):
        pass

    def visitEnumItemListIdentifier(self, enum_item_list):
        pass

    def visitEnumItemListIdentifierAssignExpression(self, enum_item_list):
        pass

    def visitMultipleTimesConcrete(self, multiple_times):
        pass

    def visitIntegerNumberConcrete(self, integer_number):
        pass

    def visitExpressionListConcrete(self, expression_list):
        pass

    def visitExpressionConcrete(self, expression):
        pass

    def visitAssignmentOperatorConcrete(self, assignment_operator):
        pass

    def visitAssignExpressionRecursion(self, assign_expression):
        pass

    def visitAssignExpressionToTernary(self, assign_expression):
        pass

    def visitTernaryConditionalExpressionRecursion(self, ternary_conditional_expression):
        pass

    def visitTernaryConditionalExpressionToLogicalExpression(self, ternary_conditional_expression):
        pass

    def visitLogicalExpressionConcrete(self, logical_expression):
        pass

    def visitLogicalOrExpressionRecursion(self, logical_or_expression):
        pass

    def visitLogicalOrExpressionToAndExpression(self, logical_or_expression):
        pass

    def visitLogicalAndExpressionRecursion(self, logical_and_expression):
        pass

    def visitLogicalAndExpressionToBitwiseOrExpression(self, logical_and_expression):
        pass

    def visitBitwiseOrExpressionRecursion(self, bitwise_or_expression):
        pass

    def visitBitwiseOrExpressionToXorBitwiseExpression(self, bitwise_or_expression):
        pass

    def visitBitwiseXorExpressionRecursion(self, bitwise_xor_expression):
        pass

    def visitBitwiseXorExpressionToBitwiseAndExpression(self, bitwise_xor_expression):
        pass

    def visitBitwiseAndExpressionRecursion(self, bitwise_and_expression):
        pass

    def visitBitwiseAndExpressionToEqualsExpression(self, bitwise_and_expression):
        pass

    def visitIsEqualsExpressionRecursion(self, is_equals_expression):
        pass

    def visitIsEqualsExpressionToNotEqualsExpression(self, is_equals_expression):
        pass

    def visitIsNotEqualsExpressionRecursion(self, is_not_equals_expression):
        pass

    def visitIsNotEqualsExpressionToGreaterThenExpression(self, is_not_equals_expression):
        pass

    def visitGreaterThenExpressionRecursion(self, greater_then_expression):
        pass

    def visitGreaterThenExpressionToGreaterEqualsExpression(self, greater_then_expression):
        pass

    def visitGreaterEqualsExpressionRecursion(self, greater_equals_expression):
        pass

    def visitGreaterEqualsExpressionToLessThenExpression(self, greater_equals_expression):
        pass

    def visitLessThenExpressionRecursion(self, less_then_expression):
        pass

    def visitLessThenExpressionToLessEqualsExpression(self, less_then_expression):
        pass

    def visitLessEqualsExpressionRecursion(self, less_equals_expression):
        pass

    def visitLessEqualsExpressionToLeftShiftExpression(self, less_equals_expression):
        pass

    def visitLeftShiftExpressionRecursion(self, left_shift_expression):
        pass

    def visitLeftShiftExpressionToRightShiftExpression(self, left_shift_expression):
        pass

    def visitRightShiftExpressionRecursion(self, right_shift_expression):
        pass

    def visitRightShiftExpressionToPlusExpression(self, right_shift_expression):
        pass

    def visitPlusExpressionRecursion(self, plus_expression):
        pass

    def visitPlusExpressionToMinusExpression(self, plus_expression):
        pass

    def visitMinusExpressionRecursion(self, minus_expression):
        pass

    def visitMinusExpressionToTimesExpression(self, minus_expression):
        pass

    def visitTimesExpressionRecursion(self, times_expression):
        pass

    def visitTimesExpressionToDivideExpression(self, times_expression):
        pass

    def visitDivideExpressionRecursion(self, divide_expression):
        pass

    def visitDivideExpressionToModulusExpression(self, divide_expression):
        pass

    def visitModulusExpressionRecursion(self, modulus_expression):
        pass

    def visitModulusExpressionToUnaryExpression(self, modulus_expression):
        pass

    def visitUnaryOperatorConcrete(self, unary_operator):
        pass

    def visitUnaryToPostifix(self, unary_expression):
        pass

    def visitUnaryPreIncrementPostfixExpression(self, unary_expression):
        pass

    def visitUnaryPreDecrementPostfixExpression(self, unary_expression):
        pass

    def visitUnaryPostIncrementPostfixExpression(self, unary_expression):
        pass

    def visitUnaryPostDecrementPostfixExpression(self, unary_expression):
        pass

    def visitUnaryCastExpressionPostfixExpression(self, unary_expression):
        pass

    def visitSizeofExpressionUnary(self, sizeof_expression):
        pass

    def visitSizeofPostfixExpression(self, sizeof_expression):
        pass

    def visitSizeofTypeExpression(self, sizeof_expression):
        pass

    def visitCastExpressionType(self, cast_expression):
        pass

    def visitPostfixExpressionBracket(self, postfix_expression):
        pass

    def visitPostfixExpressionFunctionCallNoParams(self, postfix_expression):
        pass

    def visitPostfixExpressionParenFunctionCall(self, postfix_expression):
        pass

    def visitPostfixExpressionDot(self, postfix_expression):
        pass

    def visitPostfixExpressionArrow(self, postfix_expression):
        pass

    def visitPostfixToPrimaryExpression(self, postfix_expression):
        pass

    def visitFunctionCallParametersConcrete(self, function_call_parameters):
        pass

    def visitPrimaryExpressionConcrete(self, primary_expression):
        pass

    def visitIdentifierExpressionToIdentifier(self, identifier_expression):
        print(identifier_expression.identifier)

    def visitIdentifierExpressionToString(self, identifier_expression):
        pass

    def visitStringExpressionString(self, string_expression):
        pass

    def visitStringExpressionNumber(self, string_expression):
        pass

    def visitNumberToIntegerNumberExpression(self, number_expression):
        pass

    def visitNumberToFloatNumberExpression(self, number_expression):
        pass

    def visitNumberToCharacterExpression(self, number_expression):
        pass

    def visitNumberToParentesisExpression(self, number_expression):
        pass

    def visitParenthesisExpressionConcrete(self, parenthesis_expression):
        pass


def main():
    _lexer = lex.lex()

    _input = ""
    with open("../parser/parser_test.c", "r") as file:
        for line in file:
            if not line.startswith('#'):
                _input += line

    _lexer.input(_input)
    parser = ply.yacc.yacc()
    result = parser.parse()

    result.print()


if __name__ == "__main__":
    main()
    print("Nenhum erro sintático detectado")
