from abc import abstractmethod
from abc import ABCMeta

"""
    program : program_item
            | program_item program
"""


class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ProgramProgramItem(Program):
    def __init__(self, program_item):
        self.program_item = program_item

    def accept(self, visitor):
        pass

    def print(self):
        self.program_item.print()


class ProgramMultipleProgramItem(Program):
    def __init__(self, program_item, program):
        self.program_item = program_item
        self.program = program

    def accept(self, visitor):
        self.program_item.accept(visitor)
        self.program.accept(visitor)
        pass

    def print(self):
        self.program_item.print()
        self.program.print()


class ProgramItem(metaclass=ABCMeta):
    def accept(self, visitor):
        pass


"""
    program_item : variable_declaration_list SEMICOLON
"""


class ProgramItemVairableDeclaration(ProgramItem):
    def __init__(self, variable_declaration_list):
        self.variable_declaration_list = variable_declaration_list

    def accept(self, visitor):
        self.variable_declaration_list.accept(visitor)
        pass

    def print(self):
        self.variable_declaration_list.print()
        print(';')


"""
    program_item : function
"""


class ProgramItemFunction(ProgramItem):
    def __init__(self, function):
        self.funcion = function

    def accept(self, visitor):
        pass

    def print(self):
        self.funcion.print()
        pass


"""
    program_item : global_assign_identifier_list
"""


class ProgramItemAssign(ProgramItem):
    def __init__(self, global_assign_identifier_list):
        self.global_assign_identifier_list = global_assign_identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.global_assign_identifier_list.print()
        print(";")


"""
    program_item : type SEMICOLON
"""


class ProgramItemType(ProgramItem):
    def __init__(self, _type):
        self.type = _type

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()
        print(";")


"""
    global_assign_identifier_list : IDENTIFIER ASSIGN expression
                                  | IDENTIFIER ASSIGN expression COMMA global_assign_identifier_list
"""


class GlobalAssign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class GlobalAssignOneIdentifier(GlobalAssign):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def accept(self, visitor):
        pass

    def print(self):
        print(self.identifier, end='')
        print(" = ", end='')
        self.expression.print()


class GlobalAssignMultiplesIdentifiers(GlobalAssign):
    def __init__(self, identifier, expression, global_assign_identifier_list):
        self.identifier = identifier
        self.expression = expression
        self.global_assign_identifier_list = global_assign_identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        print(self.identifier, end='')
        print(" = ", end='')
        self.expression.print()

        if self.global_assign_identifier_list is not None:
            print(", ", end='')
            self.global_assign_identifier_list.print()


"""
    block : LBRACE RBRACE
          | LBRACE block_statements RBRACE
"""


class Block(metaclass=ABCMeta):
    def accept(self, visitor):
        pass



class BlockToEmptyBlock(Block):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass

    def print(self):
        print("{\n")
        print("}")


class BlockToBlockWithStatements(Block):
    def __init__(self, block_statements):
        self.block_statements = block_statements

    def accept(self, visitor):
        pass

    def print(self):
        print("{")
        self.block_statements.print()
        print("}")


# block_statements : block_statement
#                  | block_statements block_statement
class BlockStatements(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BlockStatementsToBlockStatement(BlockStatements):
    def __init__(self, block_statement):
        self.block_statement = block_statement

    def accept(self, visitor):
        pass

    def print(self):
        self.block_statement.print()


class BlockStatementsToMultipleBlockStatements(BlockStatements):
    def __init__(self, block_statements, block_statement):
        self.block_statements = block_statements
        self.block_statement = block_statement

    def accept(self, visitor):
        pass

    def print(self):
        self.block_statements.print()
        self.block_statement.print()



# block_statement : statement
class BlockStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BlockStatementToStatement(BlockStatement):
    def __init__(self, statement):
        self.statement = statement

    def accept(self, visitor):
        pass

    def print(self):
        self.statement.print()


# statement → statement_without_trailing_substatement
#            | if_then_statement
#            | if_then_else_statement
#            | while_statement
#            | for_statement
class Statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class StatementToStatementWithoutTrailingSubstatement(Statement):
    def __init__(self, statement_without_trailing_substatement):
        self.statement_without_trailing_substatement = statement_without_trailing_substatement

    def accept(self, visitor):
        pass

    def print(self):
        self.statement_without_trailing_substatement.print()


class StatementToIfThenStatement(Statement):
    def __init__(self, if_then_statement):
        self.if_then_statement = if_then_statement

    def accept(self, visitor):
        pass

    def print(self):
        self.if_then_statement.print()


class StatementToIfThenElseStatement(Statement):
    def __init__(self, if_then_else_statement):
        self.if_then_else_statement = if_then_else_statement

    def accept(self, visitor):
        pass

    def print(self):
        self.if_then_else_statement.print()


class StatementToWhileStatement(Statement):
    def __init__(self, while_statement):
        self.while_statement = while_statement

    def accept(self, visitor):
        pass

    def print(self):
        self.while_statement.print()


class StatementToForStatement(Statement):
    def __init__(self, for_statement):
        self.for_statement = for_statement

    def accept(self, visitor):
        pass

    def print(self):
        self.for_statement.print()


# statement_without_trailing_substatement → block
#                                          | SEMICOLON
#                                          | expression_list SEMICOLON
#                                          | switch_stm
#                                          | do_statement
#                                          | KEYWORD_BREAK SEMICOLON
#                                          | KEYWORD_CONTINUE SEMICOLON
#                                          | return_stm SEMICOLON
#                                          | IDENTIFIER COLON
#                                          | KEYWORD_GOTO IDENTIFIER SEMICOLON
#                                          | variable_declaration_list SEMICOLON
#                                          | type SEMICOLON
class StatementWithoutTrailingSubstatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SWTSToBlockStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, block):
        self.block = block

    def accept(self, visitor):
        pass

    def print(self):
        self.block.print()


class SWTSToSemicolonStatement(StatementWithoutTrailingSubstatement):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass

    def print(self):
        print(";")


class SWTSToExpressionListStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, expression_list):
        self.expression_list = expression_list

    def accept(self, visitor):
        pass

    def print(self):
        self.expression_list.print()
        print(";")


class SWTSToSwitchStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, switch_stm):
        self.switch_stm = switch_stm

    def accept(self, visitor):
        pass

    def print(self):
        self.switch_stm.print()


class SWTSToDoStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, do_statement):
        self.do_statement = do_statement

    def accept(self, visitor):
        pass

    def print(self):
        self.do_statement.print()


class SWTSToBreakStatement(StatementWithoutTrailingSubstatement):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass

    def print(self):
        print("break;")


class SWTSToContinueStatement(StatementWithoutTrailingSubstatement):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass

    def print(self):
        print("continue;")


class SWTSToReturnStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, return_stm):
        self.return_stm = return_stm

    def accept(self, visitor):
        pass

    def print(self):
        self.return_stm.print()
        print(";")


class SWTSToLabelStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print(self.identifier + ":")


class SWTSToGotoStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print('goto', self.identifier + ";")


class SWTSToVariableDeclarationStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, variable_declaration_list):
        self.variable_declaration_list = variable_declaration_list

    def accept(self, visitor):
        pass

    def print(self):
        self.variable_declaration_list.print()
        print(";")


class SWTSToTypeDeclarationStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, _type):
        self.type = _type

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()
        print(";")


# statement_no_short_if → statement_without_trailing_substatement
#                        | if_then_else_statement_no_short_if
#                        | while_statement_no_short_if
#                        | for_statement_no_short_if

class StatementNoShortIf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SNSIStatementWithoutTrailingSubstatementNoShortIf(StatementNoShortIf):
    def __init__(self, statement_without_trailing_substatement):
        self.statement_without_trailing_substatement = statement_without_trailing_substatement

    def accept(self, visitor):
        pass

    def print(self):
        self.statement_without_trailing_substatement.print()


class SNSIIfThenElseStatementNoShortIf(StatementNoShortIf):
    def __init__(self, if_then_else_statement_no_short_if):
        self.if_then_else_statement_no_short_if = if_then_else_statement_no_short_if

    def accept(self, visitor):
        pass

    def print(self):
        self.if_then_else_statement_no_short_if.print()


class SNSIWhileStatementNoShortIf(StatementNoShortIf):
    def __init__(self, while_statement_no_short_if):
        self.while_statement_no_short_if = while_statement_no_short_if

    def accept(self, visitor):
        pass

    def print(self):
        self.while_statement_no_short_if.print()


class SNSIForStatementNoShortIf(StatementNoShortIf):
    def __init__(self, for_statement_no_short_if):
        self.for_statement_no_short_if = for_statement_no_short_if

    def accept(self, visitor):
        pass

    def print(self):
        self.for_statement_no_short_if.print()


# if_then_statement : KEYWORD_IF LPAREN expression RPAREN statement
class IfThenStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IfThenStatementConcrete(IfThenStatement):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def accept(self, visitor):
        pass

    def print(self):
        print("if (", end='')
        self.expression.print()
        print(")", end='')
        self.statement.print()


# if_then_else_statement : KEYWORD_IF LPAREN expression RPAREN statement_no_short_if KEYWORD_ELSE statement

class IfThenElseStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IfThenElseStatementConcrete(IfThenElseStatement):
    def __init__(self, expression, statement_no_short_if, statement):
        self.expression = expression
        self.statement_no_short_if = statement_no_short_if
        self.statement = statement

    def accept(self, visitor):
        pass

    def print(self):
        print('if(', end='')
        self.expression.print()
        print(")")
        self.statement_no_short_if.print()
        print("else")
        self.statement.print()


# if_then_else_statement_no_short_if : KEYWORD_IF LPAREN expression RPAREN statement_no_short_if KEYWORD_ELSE statement_no_short_if
class IfThenElseStatementNoShortIf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IfThenElseStatementNoShortIfConcrete(IfThenElseStatementNoShortIf):
    def __init__(self, expression, statement_no_short_if_true, statement_no_short_if_false):
        self.expression = expression
        self.statement_no_short_if_true = statement_no_short_if_true
        self.statement_no_short_if_false = statement_no_short_if_false

    def accept(self, visitor):
        pass

    def print(self):
        print('if(', end='')
        self.expression.print()
        print(")")
        self.statement_no_short_if_true.print()
        print("else")
        self.statement_no_short_if_false.print()


# while_statement : KEYWORD_WHILE LPAREN expression RPAREN statement

class WhileStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class WhileStatementConcrete(WhileStatement):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def accept(self, visitor):
        pass

    def print(self):
        print("while(", end='')
        self.expression.print()
        print(")")
        self.statement.print()


# while_statement_no_short_if : KEYWORD_WHILE LPAREN expression RPAREN statement_no_short_if

class WhileStatementNoShortIf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class WhileStatementNoShortIfConcrete(WhileStatementNoShortIf):
    def __init__(self, expression, statement_no_short_if):
        self.expression = expression
        self.statement_no_short_if = statement_no_short_if

    def accept(self, visitor):
        pass

    def print(self):
        print("while(", end='')
        self.expression.print()
        print(')')
        self.statement_no_short_if.print()


# do_statement : KEYWORD_DO statement KEYWORD_WHILE LPAREN expression RPAREN SEMICOLON

class DoStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class DoStatementConcrete(DoStatement):
    def __init__(self, statement, expression):
        self.statement = statement
        self.expression = expression

    def accept(self, visitor):
        pass

    def print(self):
        print("do")
        self.statement.print()
        print("while(", end='')
        self.expression.print()
        print(");")


# for_params : variable_declaration_list SEMICOLON for_param
#            | variable_declaration_list SEMICOLON for_param expression_list
#            | for_param for_param expression_list
#            | for_param for_param
class ForParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ForParamsWithVariableDeclaration(ForParams):
    def __init__(self, variable_declaration_list, for_param, expression_list=None):
        self.variable_declaration_list = variable_declaration_list
        self.for_param = for_param
        self.expression_list = expression_list

    def accept(self, visitor):
        pass

    def print(self):
        self.variable_declaration_list.print()
        print(";", end='')
        self.for_param.print()
        print(";", end='')
        if self.expression_list is not None:
            self.expression_list.print()


class ForParamsWithoutVariableDeclaration(ForParams):
    def __init__(self, for_param1, for_param2, expression_list=None):
        self.for_param1 = for_param1
        self.for_param2 = for_param2
        self.expression_list = expression_list

    def accept(self, visitor):
        pass

    def print(self):
        self.for_param1.print()
        print(";", end='')
        self.for_param2.print()
        print(";", end='')
        if self.expression_list is not None:
            self.expression_list.print()


# for_param : SEMICOLON
#           | expression_list SEMICOLON

class ForParam(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SemicolonForParam(ForParam):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass

    def print(self):
        pass


class ExpressionListForParam(ForParam):
    def __init__(self, expression_list):
        self.expression_list = expression_list

    def accept(self, visitor):
        pass

    def print(self):
        self.expression_list.print()


# for_statement : KEYWORD_FOR LPAREN for_params RPAREN statement

class ForStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ForStatementConcrete(ForStatement):
    def __init__(self, for_params, statement):
        self.for_params = for_params
        self.statement = statement

    def accept(self, visitor):
        pass

    def print(self):
        print("for(", end='')
        self.for_params.print()
        print(")")
        self.statement.print()


# for_statement_no_short_if : KEYWORD_FOR LPAREN for_params RPAREN statement_no_short_if

class ForStatementNoShortIf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ForStatementNoShortIfConcrete(ForStatementNoShortIf):
    def __init__(self, for_params, statement_no_short_if):
        self.for_params = for_params
        self.statement_no_short_if = statement_no_short_if

    def accept(self, visitor):
        pass

    def print(self):
        print("for(", end='')
        self.for_params.print()
        print(")")
        self.statement_no_short_if.print()


# switch_stm : KEYWORD_SWITCH LPAREN expression RPAREN LBRACE switch_itens RBRACE

class SwitchStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SwitchStatementConcrete(SwitchStatement):
    def __init__(self, expression, switch_itens):
        self.expression = expression
        self.switch_itens = switch_itens

    def accept(self, visitor):
        pass

    def print(self):
        print('switch(', end='')
        self.expression.print()
        print(") {")
        self.switch_itens.print()
        print('}')


# switch_itens : KEYWORD_CASE expression COLON block_statements
#              | KEYWORD_DEFAULT COLON block_statements
#              | KEYWORD_CASE expression COLON block_statements switch_itens
#              | KEYWORD_DEFAULT COLON block_statements switch_itens

class SwitchItems(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class CaseSwitchItem(SwitchItems):
    def __init__(self, expression, block_statements, next_switch_items=None):
        self.expression = expression
        self.block_statements = block_statements
        self.next_switch_items = next_switch_items

    def accept(self, visitor):
        pass

    def print(self):
        print('case ', end='')
        self.expression.print()
        print(":")
        self.block_statements.print()
        if self.next_switch_items is not None:
            self.next_switch_items.print()


class DefaultSwitchItem(SwitchItems):
    def __init__(self, block_statements, next_switch_items=None):
        self.block_statements = block_statements
        self.next_switch_items = next_switch_items

    def accept(self, visitor):
        pass

    def print(self):
        print("default;")


# return_stm : KEYWORD_RETURN
#            | KEYWORD_RETURN expression

class ReturnStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ReturnWithoutExpression(ReturnStatement):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass

    def print(self):
        print('return', end='')


class ReturnWithExpression(ReturnStatement):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        pass

    def print(self):
        print("return ", end='')
        self.expression.print()


# function : function_signature block

class Function(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class FunctionConcrete(Function):
    def __init__(self, function_signature, block):
        self.function_signature = function_signature
        self.block = block

    def accept(self, visitor):
        pass

    def print(self):
        self.function_signature.print()
        self.block.print()



# function_signature : type identifier LPAREN signature_param_list RPAREN
#                    | type identifier LPAREN RPAREN

class FunctionSignature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class FunctionSignatureWithParams(FunctionSignature):
    def __init__(self, _type, identifier, signature_param_list):
        self.type = _type
        self.identifier = identifier
        self.signature_param_list = signature_param_list

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()
        print(" ", end='')
        self.identifier.print()

        print('(', end='')
        self.signature_param_list.print()
        print(')', end='')


class FunctionSignatureWithoutParams(FunctionSignature):
    def __init__(self, _type, identifier):
        self.type = _type
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()
        print(" ", end='')
        self.identifier.print()
        print('(', end='')
        print(')', end='')


# triple_dot : DOT DOT DOT
class TripleDot(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class TripleDotConcrete(TripleDot):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass

    def print(self):
        print('...', end='')


# signature_param_list : signature_param COMMA signature_param_list
#                      | signature_param

class SignatureParamList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SignatureParamListWithMoreParams(SignatureParamList):
    def __init__(self, signature_param, signature_param_list):
        self.signature_param = signature_param
        self.signature_param_list = signature_param_list

    def accept(self, visitor):
        pass

    def print(self):
        self.signature_param.print()
        print(', ', end='')
        self.signature_param_list.print()


class SignatureParamListWithSingleParam(SignatureParamList):
    def __init__(self, signature_param):
        self.signature_param = signature_param

    def accept(self, visitor):
        pass

    def print(self):
        self.signature_param.print()


# signature_param : type
#                 | type multiple_times
#                 | type multiple_bracket_signature
#                 | type identifier
#                 | type identifier multiple_bracket_signature
#                 | triple_dot

class SignatureParam(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class TypeOnlySignatureParam(SignatureParam):
    def __init__(self, _type):
        self.type = _type

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()


class TypeWithMultipleTimesSignatureParam(SignatureParam):
    def __init__(self, _type, multiple_times):
        self.type = _type
        self.multiple_times = multiple_times

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()
        self.multiple_times.print()


class TypeWithMultipleBracketSignatureParam(SignatureParam):
    def __init__(self, _type, multiple_bracket_signature):
        self.type = _type
        self.multiple_bracket_signature = multiple_bracket_signature

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()
        self.multiple_bracket_signature.print()


class TypeWithIdentifierSignatureParam(SignatureParam):
    def __init__(self, _type, identifier, multiple_bracket_signature=None):
        self.type = _type
        self.identifier = identifier
        self.multiple_bracket_signature = multiple_bracket_signature

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()
        print(' ', end='')
        self.identifier.print()
        if self.multiple_bracket_signature is not None:
            self.multiple_bracket_signature.print()


class TripleDotSignatureParam(SignatureParam):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass

    def print(self):
        print('...', end='')


# multiple_bracket_signature : LBRACKET RBRACKET multiple_bracket_signature
#                             | LBRACKET RBRACKET
#                             | bracket_with_bounds multiple_bracket_signature
#                             | bracket_with_bounds

class MultipleBracketSignature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class EmptyBracketMultipleBracketSignature(MultipleBracketSignature):
    def __init__(self, next_signature=None):
        self.next_signature = next_signature

    def accept(self, visitor):
        pass

    def print(self):
        print('[]', end='')
        if self.next_signature is not None:
            self.next_signature.print()


class BracketWithBoundsMultipleBracketSignature(MultipleBracketSignature):
    def __init__(self, bracket_with_bounds, next_signature=None):
        self.bracket_with_bounds = bracket_with_bounds
        self.next_signature = next_signature

    def accept(self, visitor):
        pass

    def print(self):
        self.bracket_with_bounds.print()
        if self.next_signature is not None:
            self.next_signature.print()


# bracket_with_bounds : LBRACKET number_id RBRACKET

class BracketWithBounds(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BracketWithBoundsConcrete(BracketWithBounds):
    def __init__(self, number_id):
        self.number_id = number_id

    def accept(self, visitor):
        pass

    def print(self):
        print('[', end='')
        self.number_id.print()
        print(']', end='')


# number_id : IDENTIFIER
#           | integer_number

class NumberId(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IdentifierNumberId(NumberId):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print(self.identifier, end='')


class IntegerNumberNumberId(NumberId):
    def __init__(self, integer_number):
        self.integer_number = integer_number

    def accept(self, visitor):
        pass

    def print(self):
        self.integer_number.print()


class ValueList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ValueListConcrete(ValueList):
    def __init__(self, value_list_item=None):
        self.value_list_item = value_list_item

    def accept(self, visitor):
        pass

    def print(self):
        print('{', end='')
        if self.value_list_item is not None:
            self.value_list_item.print()
        print('}', end='')


"""
    value_list_item : expression
                    | expression COMMA value_list_item
                    | value_list
                    | value_list COMMA value_list_item
"""


class ValueListItem(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ExpressionItem(ValueListItem):
    def __init__(self, expression, next_items=None):
        self.expression = expression
        self.next_items = next_items

    def accept(self, visitor):
        pass


class ValueListItem(ValueListItem):
    def __init__(self, value_list, next_items=None):
        self.value_list = value_list
        self.next_items = next_items

    def accept(self, visitor):
        pass

    def print(self):
        self.value_list.print()
        if self.next_items is not None:
            print(", ", end='')
            self.next_items.print()


"""
    variable_declaration_list : type identifier_list
"""


class VariableDeclarationList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class VariableDeclarationListConcrete(VariableDeclarationList):
    def __init__(self, _type, identifier_list):
        self.type = _type
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()
        print(' ', end='')
        self.identifier_list.print()


class IdentifierList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


"""
    identifier_list : identifier
                    | identifier COMMA identifier_list
"""


class IdentifierListConcrete(IdentifierList):
    def __init__(self, identifier, identifier_list=None):
        self.identifier = identifier
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.identifier.print()
        if self.identifier_list is not None:
            print(", ", end='')
            self.identifier_list.print()


"""
    identifier_list :  identifier multiple_bracket_signature
                     | identifier multiple_bracket_signature COMMA identifier_list
"""


class IdentifierArrayList(IdentifierList):
    def __init__(self, identifier, multiple_bracket_signature, identifier_list=None):
        self.identifier = identifier
        self.multiple_bracket_signature = multiple_bracket_signature
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.identifier.print()
        self.multiple_bracket_signature.print()
        if self.identifier_list is not None:
            self.identifier_list.print()


"""
    identifier_list : identifier ASSIGN expression
                    | identifier ASSIGN expression COMMA identifier_list
"""


class IdentifierWithAssignList(IdentifierList):
    def __init__(self, identifier, expression, identifier_list=None):
        self.identifier = identifier
        self.expression = expression
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.identifier.print()
        print(' = ', end='')
        self.expression.print()

        if self.identifier_list is not None:
            print(', ', end='')
            self.identifier_list.print()


"""
    identifier_list : identifier multiple_bracket_signature ASSIGN value_list
                   | identifier multiple_bracket_signature ASSIGN value_list COMMA identifier_list
"""


class IdentifierAssignArrayList(IdentifierList):
    def __init__(self, identifier, multiple_bracket_signature, value_list, identifier_list=None):
        self.identifier = identifier
        self.multiple_bracket_signature = multiple_bracket_signature
        self.value_list = value_list
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.identifier.print()
        print(' = ', end='')
        self.multiple_bracket_signature.print()
        print(' = ', end='')
        self.value_list.print()
        if self.identifier_list is not None:
            print(", ", end='')
            self.identifier_list.print()


"""
    identifier_list : identifier ASSIGN value_list
                    | identifier ASSIGN value_list COMMA identifier_list
"""


class IdentifierAssignValueList(IdentifierList):
    def __init__(self, identifier, value_list, identifier_list=None):
        self.identifier = identifier
        self.value_list = value_list
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.identifier.print()
        print(' = ', end='')
        self.value_list.print()
        if self.identifier_list is not None:
            print(', ', end='')
            self.identifier_list.print()

    """
        identifier_list : function_pointer
                        | function_pointer COMMA identifier_list
    """


class IdentifierListFunctionPointer(IdentifierList):
    def __init__(self, function_pointer, identifier_list=None):
        self.function_pointer = function_pointer
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.function_pointer.print()
        if self.identifier_list is not None:
            print(', ', end='')
            self.identifier_list.print()


"""
    identifier_list : function_pointer ASSIGN expression
                    | function_pointer ASSIGN expression COMMA identifier_list
"""


class IdentifierListFunctionPointerAssign(IdentifierList):
    def __init__(self, function_pointer, expression, identifier_list=None):
        self.function_pointer = function_pointer
        self.expression = expression
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.function_pointer.print()
        print(' = ', end='')
        self.expression.print();
        if (self.identifier_list is not None):
            print(', ', end='')
            self.identifier_list.print()


"""
    identifier_list : function_pointer_array
                    | function_pointer_array COMMA identifier_list
"""


class IdentifierListFunctionPointerArray(IdentifierList):
    def __init__(self, function_pointer_array, identifier_list=None):
        self.function_pointer_array = function_pointer_array
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.function_pointer_array.print()
        if self.identifier_list is not None:
            print(', ', end='')
            self.identifier_list.print()


"""
    identifier_list : function_pointer_array ASSIGN value_list
                    | function_pointer_array ASSIGN value_list COMMA identifier_list
"""


class IdentifierListFunctionPointerArrayAssign(IdentifierList):
    def __init__(self, function_pointer_array, value_list, identifier_list=None):
        self.function_pointer_array = function_pointer_array
        self.value_list = value_list
        self.identifier_list = identifier_list

    def accept(self, visitor):
        pass

    def print(self):
        self.function_pointer_array.print()
        print(" = ", end='')
        self.value_list.print()
        if self.identifier_list is not None:
            print(', ', end='')
            self.identifier_list.print()


"""
    function_pointer : identifier LPAREN signature_param_list RPAREN
                     | identifier LPAREN RPAREN
"""


class FunctionPointer(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class FunctionPointerConcrete(FunctionPointer):
    def __init__(self, identifier, signature_param_list=None):
        self.identifier = identifier
        self.signature_param_list = signature_param_list

    def accept(self, visitor):
        pass

    def print(self):
        self.identifier.print()
        print('(', end='')
        if self.signature_param_list is not None:
            self.signature_param_list.print()
        print(')', end='')


"""
    function_pointer_array : LPAREN TIMES identifier multiple_bracket_signature RPAREN LPAREN signature_param_list RPAREN
                           | LPAREN TIMES identifier multiple_bracket_signature RPAREN LPAREN RPAREN
"""


class FunctionPointerArray(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class FunctionPointerArrayConcrete(FunctionPointerArray):
    def __init__(self, identifier, multiple_bracket_signature, signature_param_list=None):
        self.identifier = identifier
        self.multiple_bracket_signature = multiple_bracket_signature
        self.signature_param_list = signature_param_list

    def accept(self, visitor):
        pass

    def print(self):
        print('(', end='')
        self.identifier.print()
        self.multiple_bracket_signature.print()
        print(')', end='')
        print('(', end='')
        if self.signature_param_list is not None:
            self.signature_param_list.print()
        print(')', end='')


"""
    identifier :  IDENTIFIER
                | TIMES identifier
                | LPAREN identifier RPAREN
"""


class Identifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IdentifierOnly(Identifier):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print(self.identifier, end='')


class IdentifierTimesIdentifier(Identifier):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print("*", end='')
        self.identifier.print()


class IdentifierWithParentesis(Identifier):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print("(", end='')
        self.identifier.print()
        print(")", end='')


"""
    type : user_types
         | primitive_types
         | type_modifier type
"""


class Type(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class TypeUserType(Type):
    def __init__(self, user_types):
        self.user_types = user_types

    def accept(self, visitor):
        pass

    def print(self):
        self.user_types.print()


class TypePrimitiveType(Type):
    def __init__(self, primitive_type):
        self.primitive_type = primitive_type

    def accept(self, visitor):
        pass

    def print(self):
        self.primitive_type.print()


"""
    type_modifier :   KEYWORD_STATIC
                    | KEYWORD_UNSIGNED
                    | KEYWORD_VOLATILE
                    | KEYWORD_EXTERN
                    | KEYWORD_SIGNED
                    | KEYWORD_REGISTER
                    | KEYWORD_CONST
"""


class TypeWithModifier(Type):
    def __init__(self, type_modifier, _type):
        self.type_modifier = type_modifier
        self.type = _type

    def accept(self, visitor):
        pass

    def print(self):
        self.type_modifier.print()
        self.type.print()


class TypeModifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class TypeModifierConcrete(TypeModifier):
    def __init__(self, type_modifier):
        self.type_modifier = type_modifier

    def accept(self, visitor):
        pass

    def print(self):
        print(self.type_modifier, end=' ')


"""
    user_types : struct_declaration
               | union_declaration
               | enum_declaration
"""


class UserTypes(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class StructDeclarationUserType(UserTypes):
    def __init__(self, struct_declaration):
        self.struct_declaration = struct_declaration

    def accept(self, visitor):
        pass

    def print(self):
        self.struct_declaration.print()


class UnionDeclarationUserType(UserTypes):
    def __init__(self, union_declaration):
        self.union_declaration = union_declaration

    def accept(self, visitor):
        pass

    def print(self):
        self.union_declaration.print()


class EnumDeclarationUserType(UserTypes):
    def __init__(self, enum_declaration):
        self.enum_declaration = enum_declaration

    def accept(self, visitor):
        pass

    def print(self):
        self.enum_declaration.print()


"""
    primitive_types : TYPE_CHAR
                    | TYPE_INT
                    | TYPE_SHORT
                    | TYPE_LONG
                    | TYPE_FLOAT
                    | TYPE_DOUBLE
                    | TYPE_VOID
"""


class PrimitiveType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class PrimitiveTypeConcrete(PrimitiveType):
    def __init__(self, primitive_type):
        self.primitive_type = primitive_type

    def accept(self, visitor):
        pass

    def print(self):
        print(self.primitive_type, end='')


"""
    struct_declaration :  KEYWORD_STRUCT IDENTIFIER LBRACE RBRACE
                        | KEYWORD_STRUCT IDENTIFIER LBRACE struct_or_union_member_list RBRACE
                        | KEYWORD_STRUCT LBRACE RBRACE
                        | KEYWORD_STRUCT LBRACE struct_or_union_member_list RBRACE
                        | KEYWORD_STRUCT IDENTIFIER
"""


class StructDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class NamedStructDeclaration(StructDeclaration):
    def __init__(self, identifier, member_list=None):
        self.identifier = identifier
        self.member_list = member_list

    def accept(self, visitor):
        pass

    def print(self):
        print("struct ", self.identifier, " {")
        if self.member_list is not None:
            self.member_list.print()
        print("}", end='')


class UnamedStructDeclaration(StructDeclaration):
    def __init__(self, member_list=None):
        self.member_list = member_list

    def accept(self, visitor):
        pass

    def print(self):
        print("struct {")
        if self.member_list is not None:
            self.member_list.print()
        print("}", end='')


class StructDeclarationOnlyIdentifier(StructDeclaration):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print("struct ", self.identifier, end='')


"""
    union_declaration :   KEYWORD_UNION IDENTIFIER LBRACE RBRACE
                        | KEYWORD_UNION IDENTIFIER LBRACE struct_or_union_member_list RBRACE
                        | KEYWORD_UNION LBRACE RBRACE
                        | KEYWORD_UNION LBRACE struct_or_union_member_list RBRACE
                        | KEYWORD_UNION IDENTIFIER
"""


class UnionDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class NamedUnionDeclaration(UnionDeclaration):
    def __init__(self, identifier, member_list=None):
        self.identifier = identifier
        self.member_list = member_list

    def accept(self, visitor):
        pass

    def print(self):
        print("union ", self.identifier, " {")
        if self.member_list is not None:
            self.member_list.print()
        print("}", end='')


class UnamedUnionDeclaration(UnionDeclaration):
    def __init__(self, member_list=None):
        self.member_list = member_list

    def accept(self, visitor):
        pass

    def print(self):
        print("union {")
        if self.member_list is not None:
            self.member_list.print()
        print("}", end='')


class UnionDeclarationOnlyIdentifier(UnionDeclaration):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print("union ", self.identifier, end='')


"""
    enum_declaration : KEYWORD_ENUM LBRACE enum_item_list RBRACE
                     | KEYWORD_ENUM IDENTIFIER LBRACE enum_item_list RBRACE
                     | KEYWORD_ENUM IDENTIFIER
"""


class EnumDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class NamedEnumDeclaration(EnumDeclaration):
    def __init__(self, identifier, member_list):
        self.identifier = identifier
        self.member_list = member_list

    def accept(self, visitor):
        pass

    def print(self):
        print("enum", self.identifier, "{ ")
        self.member_list.print()
        print("}", end='')


class UnamedEnumDeclaration(EnumDeclaration):
    def __init__(self, member_list):
        self.member_list = member_list

    def accept(self, visitor):
        pass

    def print(self):
        print("enum { ")
        self.member_list.print()
        print("}", end='')


class EnumDeclarationOnlyIdentifier(EnumDeclaration):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print("enum ", self.identifier, end='')


"""
    struct_or_union_member_list : variable_declaration_list_no_assign SEMICOLON
                               | variable_declaration_list_no_assign SEMICOLON struct_or_union_member_list

"""


class StructOrUnionMemberList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class StructOrUnionMemberListConcrete(StructOrUnionMemberList):
    def __init__(self, variable_declaration_list_no_assign, next_struct_or_union_member_list=None):
        self.variable_declaration_list_no_assign = variable_declaration_list_no_assign
        self.next_struct_or_union_member_list = next_struct_or_union_member_list

    def accept(self, visitor):
        pass

    def print(self):
        self.variable_declaration_list_no_assign.print()
        if self.next_struct_or_union_member_list is not None:
            self.next_struct_or_union_member_list.print()


"""
    variable_declaration_list_no_assign : type variable_list_no_assign
"""


class VariableDeclarationListNoAssign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class VariableDeclarationListNoAssignConcrete(VariableDeclarationListNoAssign):
    def __init__(self, _type, variable_list_no_assign):
        self.type = _type
        self.variable_list_no_assign = variable_list_no_assign

    def accept(self, visitor):
        pass

    def print(self):
        self.type.print()
        print(" ", end='')
        self.variable_list_no_assign.print()
        print(";")


"""
    variable_list_no_assign : identifier
                            | variable_list_no_assign COMMA identifier
"""


class VariableListNoAssign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class VariableListNoAssignConcrete(VariableListNoAssign):
    def __init__(self, identifier, next_variable_list_no_assign=None):
        self.identifier = identifier
        self.next_variable_list_no_assign = next_variable_list_no_assign

    def accept(self, visitor):
        pass

    def print(self):
        self.identifier.print()
        if self.next_variable_list_no_assign is not None:
            print(", ", end='')
            self.next_variable_list_no_assign.print()


"""
    enum_item_list : IDENTIFIER
                    | IDENTIFIER COMMA enum_item_list
                    | IDENTIFIER ASSIGN expression
                    | IDENTIFIER ASSIGN expression COMMA enum_item_list
"""


class EnumItemList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class EnumItemListIdentifier(EnumItemList):
    def __init__(self, identifier, next_enum_item_list=None):
        self.identifier = identifier
        self.next_enum_item_list = next_enum_item_list

    def accept(self, visitor):
        pass

    def print(self):
        print(self.identifier, end='')
        if self.next_enum_item_list is not None:
            print(", ", end='')
            self.next_enum_item_list.print()
        else:
            print()


class EnumItemListIdentifierAssignExpression(EnumItemList):
    def __init__(self, identifier, expression, next_enum_item_list=None):
        self.identifier = identifier
        self.expression = expression
        self.next_enum_item_list = next_enum_item_list

    def accept(self, visitor):
        pass

    def print(self):
        print(self.identifier, '= ', end='')
        self.expression.print()
        if self.next_enum_item_list is not None:
            print(", ", end='')
            self.next_enum_item_list.print()
        else:
            print()


"""
    multiple_times : TIMES multiple_times
                    | TIMES
"""


class MultipleTimes(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class MultipleTimesConcrete(MultipleTimes):
    def __init__(self, next_times=None):
        self.next_times = next_times

    def accept(self, visitor):
        pass

    def print(self):
        print('*', end='')
        if self.next_times is not None:
            self.next_times.print()


"""
    integer_number : NUMBER
                   | BINARY_NUMBER
                   | HEXADECIMAL_NUMBER
                   | OCTAL_NUMBER
"""


class IntegerNumber(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IntegerNumberConcrete(IntegerNumber):
    def __init__(self, number):
        self.number = number

    def accept(self, visitor):
        pass

    def print(self):
        print(self.number, end='')


"""
    expression_list : expression
                    | expression COMMA expression_list
"""


class ExpressionList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ExpressionListConcrete(ExpressionList):
    def __init__(self, expression, next_expressions=None):
        self.expression = expression
        self.next_expressions = next_expressions

    def accept(self, visitor):
        pass

    def print(self):
        self.expression.print()
        if self.next_expressions is not None:
            print(", ", end='')
            self.next_expressions.print()


"""
    expression : assign_exp
"""


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ExpressionConcrete(Expression):
    def __init__(self, assign_exp):
        self.assign_exp = assign_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.assign_exp.print()


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


class AssignmentOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class AssignmentOperatorConcrete(AssignmentOperator):
    def __init__(self, operator):
        self.operator = operator

    def accept(self, visitor):
        pass

    def print(self):
        print(self.operator, end='')


"""
    assign_exp : unary_exp assign_operator assign_exp
                | ternary_conditional_exp
"""


class AssignExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class AssignExpressionRecursion(AssignExpression):
    def __init__(self, unary_exp, assign_operator, assign_exp):
        self.unary_exp = unary_exp
        self.assign_operator = assign_operator
        self.assign_exp = assign_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.unary_exp.print()
        print(' ', end='')
        self.assign_operator.print()
        print(' ', end='')
        self.assign_exp.print()


class AssignExpressionToTernary(AssignExpression):
    def __init__(self, ternary_expression):
        self.ternary_expression = ternary_expression

    def accept(self, visitor):
        pass

    def print(self):
        self.ternary_expression.print()


"""
    ternary_conditional_exp : logical_exp QUESTION_MARK expression COLON ternary_conditional_exp
                            | logical_exp
"""


class TernaryConditionalExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class TernaryConditionalExpressionRecursion(TernaryConditionalExpression):
    def __init__(self, logical_expression, expression, ternary_expression):
        self.logical_expression = logical_expression
        self.expression = expression
        self.ternary_expression = ternary_expression

    def accept(self, visitor):
        pass

    def print(self):
        self.logical_expression.print()
        print(" ? ", end='')
        self.expression.print()
        print(" : ", end='')
        self.ternary_expression.print()


class TernaryConditionalExpressionToLogicalExpression(TernaryConditionalExpression):
    def __init__(self, logical_exp):
        self.logical_exp = logical_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.logical_exp.print()


"""
    logical_exp : logical_or_exp
"""


class LogicalExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class LogicalExpressionConcrete(LogicalExpression):
    def __init__(self, logical_or_exp):
        self.logical_or_exp = logical_or_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.logical_or_exp.print()


"""
    logical_or_exp : logical_or_exp LOGICAL_OR logical_and_exp
                    | logical_and_exp
"""


class LogicalOrExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class LogicalOrExpressionRecursion(LogicalOrExpression):
    def __init__(self, logical_or_exp, logical_and_exp):
        self.logical_or_exp = logical_or_exp
        self.logical_and_exp = logical_and_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.logical_or_exp.print()
        print(" || ", end='')
        self.logical_and_exp.print()


class LogicalOrExpressionToAndExpression(LogicalOrExpression):
    def __init__(self, logical_and_exp):
        self.logical_and_exp = logical_and_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.logical_and_exp.print()


"""
    logical_and_exp : logical_and_exp LOGICAL_AND bitwise_or_exp
                    | bitwise_or_exp
"""


class LogicalAndExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class LogicalAndExpressionRecursion(LogicalAndExpression):
    def __init__(self, logical_and_exp, bitwise_or_exp):
        self.logical_and_exp = logical_and_exp
        self.bitwise_or_exp = bitwise_or_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.logical_and_exp.print()
        print(" && ", end='')
        self.bitwise_or_exp.print()


class LogicalAndExpressionToBitwiseOrExpression(LogicalAndExpression):
    def __init__(self, bitwise_or_exp):
        self.bitwise_or_exp = bitwise_or_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.bitwise_or_exp.print()


"""
    bitwise_or_exp : bitwise_or_exp BITWISE_OR bitwise_xor_exp
                    | bitwise_xor_exp
"""


class BitwiseOrExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BitwiseOrExpressionRecursion(BitwiseOrExpression):
    def __init__(self, bitwise_or_exp, bitwise_xor_exp):
        self.bitwise_or_exp = bitwise_or_exp
        self.bitwise_xor_exp = bitwise_xor_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.bitwise_or_exp.print()
        print(" | ", end='')
        self.bitwise_xor_exp.print()


class BitwiseOrExpressionToXorBitwiseExpression(BitwiseOrExpression):
    def __init__(self, bitwise_xor_exp):
        self.bitwise_xor_exp = bitwise_xor_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.bitwise_xor_exp.print()


"""
    bitwise_xor_exp : bitwise_xor_exp BITWISE_XOR bitwise_and_exp
                    | bitwise_and_exp
"""


class BitwiseXorExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BitwiseXorExpressionRecursion(BitwiseXorExpression):
    def __init__(self, bitwise_xor_exp, bitwise_and_exp):
        self.bitwise_xor_exp = bitwise_xor_exp
        self.bitwise_and_exp = bitwise_and_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.bitwise_xor_exp.print()
        print(" ^ ", end='')
        self.bitwise_and_exp.print()


class BitwiseXorExpressionToBitwiseAndExpression(BitwiseXorExpression):
    def __init__(self, bitwise_and_exp):
        self.bitwise_and_exp = bitwise_and_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.bitwise_and_exp.print()


"""
    bitwise_and_exp : bitwise_and_exp BITWISE_AND is_equals_exp
                    | is_equals_exp
"""


class BitwiseAndExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BitwiseAndExpressionRecursion(BitwiseAndExpression):
    def __init__(self, bitwise_and_exp, is_equals_exp):
        self.bitwise_and_exp = bitwise_and_exp
        self.is_equals_exp = is_equals_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.bitwise_and_exp.print()
        print(" & ", end='')
        self.is_equals_exp.print()


class BitwiseAndExpressionToEqualsExpression(BitwiseAndExpression):
    def __init__(self, is_equals_exp):
        self.is_equals_exp = is_equals_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.is_equals_exp.print()


"""
    is_equals_exp : is_equals_exp EQUALS_THEN is_not_equals_exp
                   | is_not_equals_exp
"""


class IsEqualsExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IsEqualsExpressionRecursion(IsEqualsExpression):
    def __init__(self, is_equals_exp, is_not_equals_exp):
        self.is_equals_exp = is_equals_exp
        self.is_not_equals_exp = is_not_equals_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.is_equals_exp.print()
        print(" == ", end='')
        self.is_not_equals_exp.print()


class IsEqualsExpressionToNotEqualsExpression(IsEqualsExpression):
    def __init__(self, is_not_equals_exp):
        self.is_not_equals_exp = is_not_equals_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.is_not_equals_exp.print()


"""
    is_not_equals_exp : is_not_equals_exp NOT_EQUALS greater_then_exp
                      | greater_then_exp
"""


class IsNotEqualsExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IsNotEqualsExpressionRecursion(IsNotEqualsExpression):
    def __init__(self, is_not_equals_exp, greater_then_exp):
        self.is_not_equals_exp = is_not_equals_exp
        self.greater_then_exp = greater_then_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.is_not_equals_exp.print()
        print(" != ", end='')
        self.greater_then_exp.print()


class IsNotEqualsExpressionToGreaterThenExpression(IsNotEqualsExpression):
    def __init__(self, greater_then_exp):
        self.greater_then_exp = greater_then_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.greater_then_exp.print()


"""
    greater_then_exp : greater_then_exp GREATER_THEN greater_equals_exp
                     | greater_equals_exp
"""


class GreaterThenExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class GreaterThenExpressionRecursion(GreaterThenExpression):
    def __init__(self, greater_then_exp, greater_equals_exp):
        self.greater_then_exp = greater_then_exp
        self.greater_equals_exp = greater_equals_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.greater_then_exp.print()
        print(" > ", end='')
        self.greater_equals_exp.print()


class GreaterThenExpressionToGreaterEqualsExpression(GreaterThenExpression):
    def __init__(self, greater_equals_exp):
        self.greater_equals_exp = greater_equals_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.greater_equals_exp.print()


"""
     greater_equals_exp :  greater_equals_exp GREATER_EQUALS less_then_exp
                        | less_then_exp
"""


class GreaterEqualsExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class GreaterEqualsExpressionRecursion(GreaterEqualsExpression):
    def __init__(self, greater_equals_exp, less_then_exp):
        self.greater_equals_exp = greater_equals_exp
        self.less_then_exp = less_then_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.greater_equals_exp.print()
        print(" >= ", end='')
        self.less_then_exp.print()


class GreaterEqualsExpressionToLessThenExpression(GreaterEqualsExpression):
    def __init__(self, less_then_exp):
        self.less_then_exp = less_then_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.less_then_exp.print()


"""
    less_then_exp : less_then_exp LESS_THEN less_equals_exp
                  | less_equals_exp
"""


class LessThenExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class LessThenExpressionRecursion(LessThenExpression):
    def __init__(self, less_then_exp, less_equals_exp):
        self.less_then_exp = less_then_exp
        self.less_equals_exp = less_equals_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.less_then_exp.print()
        print(" < ", end='')
        self.less_equals_exp.print()


class LessThenExpressionToLessEqualsExpression(LessThenExpression):
    def __init__(self, less_equals_exp):
        self.less_equals_exp = less_equals_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.less_equals_exp.print()


"""
    less_equals_exp : less_equals_exp LESS_EQUALS left_shift_exp
                    | left_shift_exp
"""


class LessEqualsExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class LessEqualsExpressionRecursion(LessEqualsExpression):
    def __init__(self, less_equals_exp, left_shift_exp):
        self.less_equals_exp = less_equals_exp
        self.left_shift_exp = left_shift_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.less_equals_exp.print()
        print(" <= ", end='')
        self.left_shift_exp.print()


class LessEqualsExpressionToLeftShiftExpression(LessEqualsExpression):
    def __init__(self, left_shift_exp):
        self.left_shift_exp = left_shift_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.left_shift_exp.print()


"""
    left_shift_exp : left_shift_exp BITWISE_SHIFT_LEFT right_shift_exp
                    | right_shift_exp
"""


class LeftShiftExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class LeftShiftExpressionRecursion(LeftShiftExpression):
    def __init__(self, left_shift_exp, right_shift_exp):
        self.left_shift_exp = left_shift_exp
        self.right_shift_exp = right_shift_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.left_shift_exp.print()
        print(" << ", end='')
        self.right_shift_exp.print()


class LeftShiftExpressionToRightShiftExpression(LeftShiftExpression):
    def __init__(self, right_shift_exp):
        self.right_shift_exp = right_shift_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.right_shift_exp.print()


"""
    right_shift_exp : right_shift_exp BITWISE_SHIFT_RIGHT plus_exp
                    | plus_exp
"""


class RightShiftExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class RightShiftExpressionRecursion(RightShiftExpression):
    def __init__(self, right_shift_exp, plus_exp):
        self.right_shift_exp = right_shift_exp
        self.plus_exp = plus_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.right_shift_exp.print()
        print(" >> ", end='')
        self.plus_exp.print()


class RightShiftExpressionToPlusExpression(RightShiftExpression):
    def __init__(self, plus_exp):
        self.plus_exp = plus_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.plus_exp.print()


"""
    plus_exp : plus_exp PLUS minus_exp
             | minus_exp
"""


class PlusExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class PlusExpressionRecursion(PlusExpression):
    def __init__(self, plus_exp, minus_exp):
        self.plus_exp = plus_exp
        self.minus_exp = minus_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.plus_exp.print()
        print(" + ", end='')
        self.minus_exp.print()


class PlusExpressionToMinusExpression(PlusExpression):
    def __init__(self, minus_exp):
        self.minus_exp = minus_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.minus_exp.print()


"""
    minus_exp : minus_exp MINUS times_exp
              | times_exp
"""


class MinusExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class MinusExpressionRecursion(MinusExpression):
    def __init__(self, minus_exp, times_exp):
        self.minus_exp = minus_exp
        self.times_exp = times_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.minus_exp.print()
        print(" - ", end='')
        self.times_exp.print()


class MinusExpressionToTimesExpression(MinusExpression):
    def __init__(self, times_exp):
        self.times_exp = times_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.times_exp.print()


"""
    times_exp : times_exp TIMES divide_exp
              | divide_exp
"""


class TimesExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class TimesExpressionRecursion(TimesExpression):
    def __init__(self, times_exp, divide_exp):
        self.times_exp = times_exp
        self.divide_exp = divide_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.times_exp.print()
        print(" * ", end='')
        self.divide_exp.print()


class TimesExpressionToDivideExpression(TimesExpression):
    def __init__(self, divide_exp):
        self.divide_exp = divide_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.divide_exp.print()


"""
    divide_exp : divide_exp DIVIDE modulus_exp
                | modulus_exp
"""


class DivideExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class DivideExpressionRecursion(DivideExpression):
    def __init__(self, divide_exp, modulus_exp):
        self.divide_exp = divide_exp
        self.modulus_exp = modulus_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.divide_exp.print()
        print(" / ", end='')
        self.modulus_exp.print()


class DivideExpressionToModulusExpression(DivideExpression):
    def __init__(self, modulus_exp):
        self.modulus_exp = modulus_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.modulus_exp.print()


"""
    modulus_exp : modulus_exp MODULUS unary_exp
                | unary_exp
"""


class ModulusExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ModulusExpressionRecursion(ModulusExpression):
    def __init__(self, modulus_exp, unary_exp):
        self.modulus_exp = modulus_exp
        self.unary_exp = unary_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.modulus_exp.print()
        print(" % ", end='')
        self.unary_exp.print()


class ModulusExpressionToUnaryExpression(ModulusExpression):
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.unary_exp.print()


"""
    unary_operator : BITWISE_AND
                   | TIMES
                   | PLUS
                   | MINUS
                   | BITWISE_COMPLEMENT
                   | NOT
"""


class UnaryOperator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class UnaryOperatorConcrete(UnaryOperator):
    def __init__(self, operator):
        self.operator = operator

    def accept(self, visitor):
        pass

    def print(self):
        print(self.operator, end='')


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


class UnaryExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class UnaryToPostifix(UnaryExpression):
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.postfix_exp.print()


class UnaryPreIncrementPostfixExpression(UnaryExpression):
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def accept(self, visitor):
        pass

    def print(self):
        print("++", end='')
        self.postfix_exp.print()


class UnaryPreDecrementPostfixExpression(UnaryExpression):
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def accept(self, visitor):
        pass

    def print(self):
        print("--", end='')
        self.postfix_exp.print()


class UnaryPostIncrementPostfixExpression(UnaryExpression):
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.postfix_exp.print()
        print("++", end='')


class UnaryPostDecrementPostfixExpression(UnaryExpression):
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.postfix_exp.print()
        print("--", end='')


class UnaryCastExpressionPostfixExpression(UnaryExpression):
    def __init__(self, cast_exp, postfix_exp):
        self.cast_exp = cast_exp
        self.postfix_exp = postfix_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.cast_exp.print()
        print(" ", end='')
        self.postfix_exp.print()


class SizeofExpressionUnary(UnaryExpression):
    def __init__(self, sizeof_exp):
        self.sizeof_exp = sizeof_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.sizeof_exp.print()


class UnaryOperatorUnaryExpression(UnaryExpression):
    def __init__(self, unary_operator, unary_exp):
        self.unary_operator = unary_operator
        self.unary_exp = unary_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.unary_operator.print()
        self.unary_exp.print()


"""
    sizeof_exp :  KEYWORD_SIZEOF postfix_exp
                | KEYWORD_SIZEOF LPAREN type RPAREN
                | KEYWORD_SIZEOF LPAREN type multiple_times RPAREN
"""


class SizeofExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SizeofPostfixExpression(SizeofExpression):
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def accept(self, visitor):
        pass

    def print(self):
        print("sizeof(", end='')
        self.postfix_exp.print()
        print(")", end='')


class SizeofTypeExpression(SizeofExpression):
    def __init__(self, _type, multiple_times=None):
        self.type = _type
        self.multiple_times = multiple_times

    def accept(self, visitor):
        pass

    def print(self):
        print("sizeof(", end='')
        self.type.print()
        if self.multiple_times is not None:
            self.multiple_times.print()
        print(")", end='')


"""
    cast_exp : LPAREN type RPAREN
             | LPAREN type multiple_times RPAREN
"""


class CastExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class CastExpressionType(CastExpression):
    def __init__(self, _type, multiple_times=None):
        self.type = _type
        self.multiple_times = multiple_times

    def accept(self, visitor):
        pass

    def print(self):
        print("(", end='')
        self.type.print()
        if self.multiple_times is not None:
            self.multiple_times.print()
        print(")", end='')


"""
    postfix_exp : postfix_exp LBRACKET expression RBRACKET
                | postfix_exp LPAREN RPAREN
                | postfix_exp LPAREN function_call_parameters RPAREN
                | postfix_exp DOT IDENTIFIER
                | postfix_exp ARROW IDENTIFIER
                | primary_exp
"""


class PostfixExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class PostfixExpressionBracket(PostfixExpression):
    def __init__(self, postfix_exp, expression):
        self.postfix_exp = postfix_exp
        self.expression = expression

    def accept(self, visitor):
        pass

    def print(self):
        self.postfix_exp.print()
        print("[", end='')
        self.expression.print()
        print("]", end='')


class PostfixExpressionFunctionCallNoParams(PostfixExpression):
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.postfix_exp.print()
        print("()", end='')


class PostfixExpressionParenFunctionCall(PostfixExpression):
    def __init__(self, postfix_exp, function_call_parameters):
        self.postfix_exp = postfix_exp
        self.function_call_parameters = function_call_parameters

    def accept(self, visitor):
        pass

    def print(self):
        self.postfix_exp.print()
        print("(", end='')
        self.function_call_parameters.print()
        print(")", end='')


class PostfixExpressionDot(PostfixExpression):
    def __init__(self, postfix_exp, identifier):
        self.postfix_exp = postfix_exp
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        self.postfix_exp.print()
        print('.', end='')
        print(self.identifier, end='')


class PostfixExpressionArrow(PostfixExpression):
    def __init__(self, postfix_exp, identifier):
        self.postfix_exp = postfix_exp
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        self.postfix_exp.print()
        print('->', end='')
        print(self.identifier, end='')


class PostfixToPrimaryExpression(PostfixExpression):
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.primary_exp.print()


"""
    function_call_parameters : expression
                              | expression COMMA function_call_parameters
"""


class FunctionCallParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class FunctionCallParametersConcrete(FunctionCallParameters):
    def __init__(self, expression, function_call_parameters=None):
        self.expression = expression
        self.function_call_parameters = function_call_parameters

    def accept(self, visitor):
        pass

    def print(self):
        self.expression.print()
        if self.function_call_parameters is not None:
            print(", ", end='')
            self.function_call_parameters.print()


"""
    primary_exp : identifier_exp
"""


class PrimaryExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class PrimaryExpressionConcrete(PrimaryExpression):
    def __init__(self, identifier_exp):
        self.identifier_exp = identifier_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.identifier_exp.print()


"""
    identifier_exp : IDENTIFIER
                    | string_exp
"""


class IdentifierExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class IdentifierExpressionToIdentifier(IdentifierExpression):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass

    def print(self):
        print(self.identifier, end='')


class IdentifierExpressionToString(IdentifierExpression):
    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        pass

    def print(self):
        self.string.print()


"""
    string_exp : STRING
                | number_exp
"""


class StringExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class StringExpressionString(StringExpression):
    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        pass

    def print(self):
        print(self.string, end='')


class StringExpressionNumber(StringExpression):
    def __init__(self, number_exp):
        self.number_exp = number_exp

    def accept(self, visitor):
        pass

    def print(self):
        self.number_exp.print()


"""
    number_exp : integer_number
                | FLOAT_NUMBER
                | CHARACTER
                | parentesis_exp
"""


class NumberExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class NumberToIntegerNumberExpression(NumberExpression):
    def __init__(self, integer_number):
        self.integer_number = integer_number

    def accept(self, visitor):
        pass

    def print(self):
        self.integer_number.print()


class NumberToFloatNumberExpression(NumberExpression):
    def __init__(self, float_number):
        self.float_number = float_number

    def accept(self, visitor):
        pass

    def print(self):
        print(self.float_number, end='')


class NumberToCharacterExpression(NumberExpression):
    def __init__(self, character):
        self.character = character

    def accept(self, visitor):
        pass

    def print(self):
        print(self.character, end='')


class NumberToParentesisExpression(NumberExpression):
    def __init__(self, parentesis_expression):
        self.parentesis_expression = parentesis_expression

    def accept(self, visitor):
        pass

    def print(self):
        self.parentesis_expression.print()


"""
    parentesis_exp : LPAREN expression RPAREN
"""


class ParenthesisExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ParenthesisExpressionConcrete(ParenthesisExpression):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        pass

    def print(self):
        print("(", end='')
        self.expression.print()
        print(")", end='')
