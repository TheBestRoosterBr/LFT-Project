from abc import abstractmethod, ABCMeta


class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitProgramProgramItem(self, program_item): pass

    @abstractmethod
    def visitProgramMultipleProgramItem(self, program_item, program): pass

    @abstractmethod
    def visitProgramItemVariableDeclaration(self, program_item):
        pass

    @abstractmethod
    def visitProgramItemFunction(self, program_item):
        pass

    @abstractmethod
    def visitProgramItemAssign(self, program_item):
        pass

    @abstractmethod
    def visitProgramItemType(self, program_item):
        pass

    @abstractmethod
    def visitGlobalAssignOneIdentifier(self, global_assign):
        pass

    @abstractmethod
    def visitGlobalAssignMultiplesIdentifiers(self, global_assign):
        pass

    @abstractmethod
    def visitBlockToEmptyBlock(self, block):
        pass

    @abstractmethod
    def visitBlockToBlockWithStatements(self, block):
        pass

    @abstractmethod
    def visitBlockStatementsToBlockStatement(self, block_statements):
        pass

    @abstractmethod
    def visitBlockStatementsToMultipleBlockStatements(self, block_statements):
        pass

    @abstractmethod
    def visitBlockStatementToStatement(self, block_statement):
        pass

    @abstractmethod
    def visitStatementToStatementWithoutTrailingSubstatement(self, statement):
        pass

    @abstractmethod
    def visitStatementToIfThenStatement(self, statement):
        pass

    @abstractmethod
    def visitStatementToIfThenElseStatement(self, statement):
        pass

    @abstractmethod
    def visitStatementToWhileStatement(self, statement):
        pass

    @abstractmethod
    def visitStatementToForStatement(self, statement):
        pass

    @abstractmethod
    def visitSWTSToBlockStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToSemicolonStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToExpressionListStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToSwitchStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToDoStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToBreakStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToContinueStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToReturnStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToLabelStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToGotoStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToVariableDeclarationStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSWTSToTypeDeclarationStatement(self, statement_without_trailing_substatement):
        pass

    @abstractmethod
    def visitSNSIStatementWithoutTrailingSubstatementNoShortIf(self, statement_no_short_if):
        pass

    @abstractmethod
    def visitSNSIIfThenElseStatementNoShortIf(self, statement_no_short_if):
        pass

    @abstractmethod
    def visitSNSIWhileStatementNoShortIf(self, statement_no_short_if):
        pass

    @abstractmethod
    def visitSNSIForStatementNoShortIf(self, statement_no_short_if):
        pass

    @abstractmethod
    def visitIfThenStatement(self, if_then_statement):
        pass

    @abstractmethod
    def visitIfThenElseStatement(self, if_then_else_statement):
        pass

    @abstractmethod
    def visitIfThenElseStatementNoShortIf(self, if_then_else_statement_no_short_if):
        pass

    @abstractmethod
    def visitWhileStatement(self, while_statement):
        pass

    @abstractmethod
    def visitWhileStatementNoShortIf(self, while_statement_no_short_if):
        pass

    @abstractmethod
    def visitDoStatement(self, do_statement):
        pass

    @abstractmethod
    def visitForParamsWithVariableDeclaration(self, for_params_with_variable_declaration):
        pass

    @abstractmethod
    def visitForParamsWithoutVariableDeclaration(self, for_params_without_variable_declaration):
        pass

    @abstractmethod
    def visitSemicolonForParam(self, semicolon_for_param):
        pass

    @abstractmethod
    def visitExpressionListForParam(self, expression_list_for_param):
        pass

    @abstractmethod
    def visitForStatement(self, for_statement):
        pass

    @abstractmethod
    def visitForStatementNoShortIf(self, for_statement_no_short_if):
        pass

    @abstractmethod
    def visitSwitchStatement(self, switch_statement):
        pass

    @abstractmethod
    def visitCaseSwitchItem(self, case_switch_item):
        pass

    @abstractmethod
    def visitDefaultSwitchItem(self, default_switch_item):
        pass

    @abstractmethod
    def visitReturnWithoutExpression(self, return_without_expression):
        pass

    @abstractmethod
    def visitReturnWithExpression(self, return_with_expression):
        pass

    @abstractmethod
    def visitFunction(self, function):
        pass

    @abstractmethod
    def visitFunctionSignatureWithParams(self, function_signature_with_params):
        pass

    @abstractmethod
    def visitFunctionSignatureWithoutParams(self, function_signature_without_params):
        pass

    @abstractmethod
    def visitTripleDot(self, triple_dot):
        pass

    @abstractmethod
    def visitSignatureParamListWithMoreParams(self, signature_param_list):
        pass

    @abstractmethod
    def visitSignatureParamListWithSingleParam(self, signature_param_list):
        pass

    @abstractmethod
    def visitTypeOnlySignatureParam(self, signature_param):
        pass

    @abstractmethod
    def visitTypeWithMultipleTimesSignatureParam(self, signature_param):
        pass

    @abstractmethod
    def visitTypeWithMultipleBracketSignatureParam(self, signature_param):
        pass

    @abstractmethod
    def visitTypeWithIdentifierSignatureParam(self, signature_param):
        pass

    @abstractmethod
    def visitTripleDotSignatureParam(self, signature_param):
        pass

    @abstractmethod
    def visitEmptyBracketMultipleBracketSignature(self, multiple_bracket_signature):
        pass

    @abstractmethod
    def visitBracketWithBoundsMultipleBracketSignature(self, multiple_bracket_signature):
        pass

    @abstractmethod
    def visitBracketWithBoundsConcrete(self, bracket_with_bounds):
        pass

    @abstractmethod
    def visitIdentifierNumberId(self, number_id):
        pass

    @abstractmethod
    def visitIntegerNumberNumberId(self, number_id):
        pass

    @abstractmethod
    def visitValueListConcrete(self, value_list):
        pass

    @abstractmethod
    def visitExpressionItem(self, value_list_item):
        pass

    @abstractmethod
    def visitValueListItem(self, value_list_item):
        pass

    @abstractmethod
    def visitVariableDeclarationListConcrete(self, variable_declaration_list):
        pass

    @abstractmethod
    def visitIdentifierListConcrete(self, identifier_list):
        pass

    @abstractmethod
    def visitIdentifierArrayList(self, identifier_list):
        pass

    @abstractmethod
    def visitIdentifierWithAssignList(self, identifier_list):
        pass

    @abstractmethod
    def visitIdentifierAssignArrayList(self, identifier_list):
        pass

    @abstractmethod
    def visitIdentifierAssignValueList(self, identifier_list):
        pass

    @abstractmethod
    def visitIdentifierListFunctionPointer(self, identifier_list):
        pass

    @abstractmethod
    def visitIdentifierListFunctionPointerAssign(self, identifier_list):
        pass

    @abstractmethod
    def visitIdentifierListFunctionPointerArray(self, identifier_list):
        pass

    @abstractmethod
    def visitIdentifierListFunctionPointerArrayAssign(self, identifier_list):
        pass

    @abstractmethod
    def visitFunctionPointerConcrete(self, function_pointer):
        pass

    @abstractmethod
    def visitFunctionPointerArrayConcrete(self, function_pointer_array):
        pass

    @abstractmethod
    def visitIdentifierOnly(self, identifier):
        pass

    @abstractmethod
    def visitIdentifierTimesIdentifier(self, identifier):
        pass

    @abstractmethod
    def visitIdentifierWithParentesis(self, identifier):
        pass

    @abstractmethod
    def visitTypeUserType(self, _type):
        pass

    @abstractmethod
    def visitTypePrimitiveType(self, _type):
        pass

    @abstractmethod
    def visitTypeWithModifier(self, _type):
        pass

    @abstractmethod
    def visitTypeModifierConcrete(self, type_modifier):
        pass

    @abstractmethod
    def visitStructDeclarationUserType(self, user_types):
        pass

    @abstractmethod
    def visitUnionDeclarationUserType(self, user_types):
        pass

    @abstractmethod
    def visitEnumDeclarationUserType(self, user_types):
        pass

    @abstractmethod
    def visitPrimitiveTypeConcrete(self, primitive_type):
        pass

    @abstractmethod
    def visitNamedStructDeclaration(self, struct_declaration):
        pass

    @abstractmethod
    def visitAnonymousStructDeclaration(self, struct_declaration):
        pass

    @abstractmethod
    def visitStructDeclarationOnlyIdentifier(self, struct_declaration):
        pass

    @abstractmethod
    def visitNamedUnionDeclaration(self, union_declaration):
        pass

    @abstractmethod
    def visitUnamedUnionDeclaration(self, union_declaration):
        pass

    @abstractmethod
    def visitUnionDeclarationOnlyIdentifier(self, union_declaration):
        pass

    @abstractmethod
    def visitNamedEnumDeclaration(self, enum_declaration):
        pass

    @abstractmethod
    def visitUnamedEnumDeclaration(self, enum_declaration):
        pass

    @abstractmethod
    def visitEnumDeclarationOnlyIdentifier(self, enum_declaration):
        pass

    @abstractmethod
    def visitStructOrUnionMemberListConcrete(self, struct_or_union_member_list):
        pass

    @abstractmethod
    def visitVariableListNoAssignConcrete(self, variable_list_no_assign):
        pass

    @abstractmethod
    def visitEnumItemListIdentifier(self, enum_item_list):
        pass

    @abstractmethod
    def visitEnumItemListIdentifierAssignExpression(self, enum_item_list):
        pass

    @abstractmethod
    def visitMultipleTimesConcrete(self, multiple_times):
        pass

    @abstractmethod
    def visitIntegerNumberConcrete(self, integer_number):
        pass

    @abstractmethod
    def visitExpressionListConcrete(self, expression_list):
        pass

    @abstractmethod
    def visitExpressionConcrete(self, expression):
        pass

    @abstractmethod
    def visitAssignmentOperatorConcrete(self, assignment_operator):
        pass

    @abstractmethod
    def visitAssignExpressionRecursion(self, assign_expression):
        pass

    @abstractmethod
    def visitAssignExpressionToTernary(self, assign_expression):
        pass

    @abstractmethod
    def visitTernaryConditionalExpressionRecursion(self, ternary_conditional_expression):
        pass

    @abstractmethod
    def visitTernaryConditionalExpressionToLogicalExpression(self, ternary_conditional_expression):
        pass

    @abstractmethod
    def visitLogicalExpressionConcrete(self, logical_expression):
        pass

    @abstractmethod
    def visitLogicalOrExpressionRecursion(self, logical_or_expression):
        pass

    @abstractmethod
    def visitLogicalOrExpressionToAndExpression(self, logical_or_expression):
        pass

    @abstractmethod
    def visitLogicalAndExpressionRecursion(self, logical_and_expression):
        pass

    @abstractmethod
    def visitLogicalAndExpressionToBitwiseOrExpression(self, logical_and_expression):
        pass

    @abstractmethod
    def visitBitwiseOrExpressionRecursion(self, bitwise_or_expression):
        pass

    @abstractmethod
    def visitBitwiseOrExpressionToXorBitwiseExpression(self, bitwise_or_expression):
        pass

    @abstractmethod
    def visitBitwiseXorExpressionRecursion(self, bitwise_xor_expression):
        pass

    @abstractmethod
    def visitBitwiseXorExpressionToBitwiseAndExpression(self, bitwise_xor_expression):
        pass

    @abstractmethod
    def visitBitwiseAndExpressionRecursion(self, bitwise_and_expression):
        pass

    @abstractmethod
    def visitBitwiseAndExpressionToEqualsExpression(self, bitwise_and_expression):
        pass

    @abstractmethod
    def visitIsEqualsExpressionRecursion(self, is_equals_expression):
        pass

    @abstractmethod
    def visitIsEqualsExpressionToNotEqualsExpression(self, is_equals_expression):
        pass

    @abstractmethod
    def visitIsNotEqualsExpressionRecursion(self, is_not_equals_expression):
        pass

    @abstractmethod
    def visitIsNotEqualsExpressionToGreaterThenExpression(self, is_not_equals_expression):
        pass

    @abstractmethod
    def visitGreaterThenExpressionRecursion(self, greater_then_expression):
        pass

    @abstractmethod
    def visitGreaterThenExpressionToGreaterEqualsExpression(self, greater_then_expression):
        pass

    @abstractmethod
    def visitGreaterEqualsExpressionRecursion(self, greater_equals_expression):
        pass

    @abstractmethod
    def visitGreaterEqualsExpressionToLessThenExpression(self, greater_equals_expression):
        pass

    @abstractmethod
    def visitLessThenExpressionRecursion(self, less_then_expression):
        pass

    @abstractmethod
    def visitLessThenExpressionToLessEqualsExpression(self, less_then_expression):
        pass

    @abstractmethod
    def visitLessEqualsExpressionRecursion(self, less_equals_expression):
        pass

    @abstractmethod
    def visitLessEqualsExpressionToLeftShiftExpression(self, less_equals_expression):
        pass

    @abstractmethod
    def visitLeftShiftExpressionRecursion(self, left_shift_expression):
        pass

    @abstractmethod
    def visitLeftShiftExpressionToRightShiftExpression(self, left_shift_expression):
        pass

    @abstractmethod
    def visitRightShiftExpressionRecursion(self, right_shift_expression):
        pass

    @abstractmethod
    def visitRightShiftExpressionToPlusExpression(self, right_shift_expression):
        pass

    @abstractmethod
    def visitPlusExpressionRecursion(self, plus_expression):
        pass

    @abstractmethod
    def visitPlusExpressionToMinusExpression(self, plus_expression):
        pass

    @abstractmethod
    def visitMinusExpressionRecursion(self, minus_expression):
        pass

    @abstractmethod
    def visitMinusExpressionToTimesExpression(self, minus_expression):
        pass

    @abstractmethod
    def visitTimesExpressionRecursion(self, times_expression):
        pass

    @abstractmethod
    def visitTimesExpressionToDivideExpression(self, times_expression):
        pass

    @abstractmethod
    def visitDivideExpressionRecursion(self, divide_expression):
        pass

    @abstractmethod
    def visitDivideExpressionToModulusExpression(self, divide_expression):
        pass

    @abstractmethod
    def visitModulusExpressionRecursion(self, modulus_expression):
        pass

    @abstractmethod
    def visitModulusExpressionToUnaryExpression(self, modulus_expression):
        pass

    @abstractmethod
    def visitUnaryOperatorConcrete(self, unary_operator):
        pass

    @abstractmethod
    def visitUnaryToPostifix(self, unary_expression):
        pass

    @abstractmethod
    def visitUnaryPreIncrementPostfixExpression(self, unary_expression):
        pass

    @abstractmethod
    def visitUnaryPreDecrementPostfixExpression(self, unary_expression):
        pass

    @abstractmethod
    def visitUnaryPostIncrementPostfixExpression(self, unary_expression):
        pass

    @abstractmethod
    def visitUnaryPostDecrementPostfixExpression(self, unary_expression):
        pass

    @abstractmethod
    def visitUnaryCastExpressionPostfixExpression(self, unary_expression):
        pass

    @abstractmethod
    def visitSizeofExpressionUnary(self, sizeof_expression):
        pass

    @abstractmethod
    def visitSizeofPostfixExpression(self, sizeof_expression):
        pass

    @abstractmethod
    def visitSizeofTypeExpression(self, sizeof_expression):
        pass

    @abstractmethod
    def visitCastExpressionType(self, cast_expression):
        pass

    @abstractmethod
    def visitPostfixExpressionBracket(self, postfix_expression):
        pass

    @abstractmethod
    def visitPostfixExpressionFunctionCallNoParams(self, postfix_expression):
        pass

    @abstractmethod
    def visitPostfixExpressionParenFunctionCall(self, postfix_expression):
        pass

    @abstractmethod
    def visitPostfixExpressionDot(self, postfix_expression):
        pass

    @abstractmethod
    def visitPostfixExpressionArrow(self, postfix_expression):
        pass

    @abstractmethod
    def visitPostfixToPrimaryExpression(self, postfix_expression):
        pass

    @abstractmethod
    def visitFunctionCallParametersConcrete(self, function_call_parameters):
        pass

    @abstractmethod
    def visitPrimaryExpressionConcrete(self, primary_expression):
        pass

    @abstractmethod
    def visitIdentifierExpressionToIdentifier(self, identifier_expression):
        pass

    @abstractmethod
    def visitIdentifierExpressionToString(self, identifier_expression):
        pass

    @abstractmethod
    def visitStringExpressionString(self, string_expression):
        pass

    @abstractmethod
    def visitStringExpressionNumber(self, string_expression):
        pass

    @abstractmethod
    def visitNumberToIntegerNumberExpression(self, number_expression):
        pass

    @abstractmethod
    def visitNumberToFloatNumberExpression(self, number_expression):
        pass

    @abstractmethod
    def visitNumberToCharacterExpression(self, number_expression):
        pass

    @abstractmethod
    def visitNumberToParentesisExpression(self, number_expression):
        pass

    @abstractmethod
    def visitParenthesisExpressionConcrete(self, parenthesis_expression):
        pass
