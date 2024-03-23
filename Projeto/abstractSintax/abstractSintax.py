from abc import abstractmethod
from abc import ABCMeta


class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ProgramProgramItem(Program):
    def __init__(self, program_item):
        self.program_item = program_item

    def accept(self, visitor):
        pass


class ProgramMultipleProgramItem(Program):
    def __init__(self, program_item, program):
        self.program_item = program_item
        self.program = program

    def accept(self, visitor):
        pass


class ProgramItem(metaclass=ABCMeta):
    def accept(self, visitor):
        pass


class ProgramItemVairableDeclaration(ProgramItem):
    def __init__(self, variable_declaration_list):
        self.variable_declaration_list = variable_declaration_list

    def accept(self, visitor):
        pass


class ProgramItemFunction(ProgramItem):
    def __init__(self, function):
        self.funcion = function

    def accept(self, visitor):
        pass


class ProgramItemAssign(ProgramItem):
    def __init__(self, global_assign_identifier_list):
        self.global_assign_identifier_list = global_assign_identifier_list

    def accept(self, visitor):
        pass


class ProgramItemType(ProgramItem):
    def __init__(self, _type):
        self.type = _type

    def accept(self, visitor):
        pass


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


class GlobalAssignMultiplesIdentifiers(GlobalAssign):
    def __init__(self, identifier, expression, global_assign_identifier_list):
        self.identifier = identifier
        self.expression = expression
        self.global_assign_identifier_list = global_assign_identifier_list

    def accept(self, visitor):
        pass


class Block(metaclass=ABCMeta):
    def accept(self, visitor):
        pass


class BlockToEmptyBlock(Block):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class BlockToBlockWithStatements(Block):
    def __init__(self, block_statements):
        self.block_statements = block_statements

    def accept(self, visitor):
        pass


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


class BlockStatementsToMultipleBlockStatements(BlockStatements):
    def __init__(self, block_statements, block_statement):
        self.block_statements = block_statements
        self.block_statement = block_statement

    def accept(self, visitor):
        pass


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


class StatementToIfThenStatement(Statement):
    def __init__(self, if_then_statement):
        self.if_then_statement = if_then_statement

    def accept(self, visitor):
        pass


class StatementToIfThenElseStatement(Statement):
    def __init__(self, if_then_else_statement):
        self.if_then_else_statement = if_then_else_statement

    def accept(self, visitor):
        pass


class StatementToWhileStatement(Statement):
    def __init__(self, while_statement):
        self.while_statement = while_statement

    def accept(self, visitor):
        pass


class StatementToForStatement(Statement):
    def __init__(self, for_statement):
        self.for_statement = for_statement

    def accept(self, visitor):
        pass


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


class SWTSToSemicolonStatement(StatementWithoutTrailingSubstatement):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class SWTSToExpressionListStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, expression_list):
        self.expression_list = expression_list

    def accept(self, visitor):
        pass


class SWTSToSwitchStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, switch_stm):
        self.switch_stm = switch_stm

    def accept(self, visitor):
        pass


class SWTSToDoStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, do_statement):
        self.do_statement = do_statement

    def accept(self, visitor):
        pass


class SWTSToBreakStatement(StatementWithoutTrailingSubstatement):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class SWTSToContinueStatement(StatementWithoutTrailingSubstatement):
    def __init__(self):
        pass

    def accept(self, visitor):
        pass


class SWTSToReturnStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, return_stm):
        self.return_stm = return_stm

    def accept(self, visitor):
        pass


class SWTSToLabelStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass


class SWTSToGotoStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, identifier):
        self.identifier = identifier

    def accept(self, visitor):
        pass


class SWTSToVariableDeclarationStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, variable_declaration_list):
        self.variable_declaration_list = variable_declaration_list

    def accept(self, visitor):
        pass


class SWTSToTypeDeclarationStatement(StatementWithoutTrailingSubstatement):
    def __init__(self, _type):
        self.type = _type

    def accept(self, visitor):
        pass


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


class SNSIIfThenElseStatementNoShortIf(StatementNoShortIf):
    def __init__(self, if_then_else_statement_no_short_if):
        self.if_then_else_statement_no_short_if = if_then_else_statement_no_short_if

    def accept(self, visitor):
        pass


class SNSIWhileStatementNoShortIf(StatementNoShortIf):
    def __init__(self, while_statement_no_short_if):
        self.while_statement_no_short_if = while_statement_no_short_if

    def accept(self, visitor):
        pass


class SNSIForStatementNoShortIf(StatementNoShortIf):
    def __init__(self, for_statement_no_short_if):
        self.for_statement_no_short_if = for_statement_no_short_if

    def accept(self, visitor):
        pass


# if_then_statement : KEYWORD_IF LPAREN expression RPAREN statement
class IfThenStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteIfThenStatement(IfThenStatement):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def accept(self, visitor):
        pass


# if_then_else_statement : KEYWORD_IF LPAREN expression RPAREN statement_no_short_if KEYWORD_ELSE statement

class IfThenElseStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteIfThenElseStatement(IfThenElseStatement):
    def __init__(self, expression, statement_no_short_if, statement):
        self.expression = expression
        self.statement_no_short_if = statement_no_short_if
        self.statement = statement

    def accept(self, visitor):
        pass


# if_then_else_statement_no_short_if : KEYWORD_IF LPAREN expression RPAREN statement_no_short_if KEYWORD_ELSE statement_no_short_if
class IfThenElseStatementNoShortIf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteIfThenElseStatementNoShortIf(IfThenElseStatementNoShortIf):
    def __init__(self, expression, statement_no_short_if_true, statement_no_short_if_false):
        self.expression = expression
        self.statement_no_short_if_true = statement_no_short_if_true
        self.statement_no_short_if_false = statement_no_short_if_false

    def accept(self, visitor):
        pass


# while_statement : KEYWORD_WHILE LPAREN expression RPAREN statement

class WhileStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteWhileStatement(WhileStatement):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def accept(self, visitor):
        pass


# while_statement_no_short_if : KEYWORD_WHILE LPAREN expression RPAREN statement_no_short_if

class WhileStatementNoShortIf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteWhileStatementNoShortIf(WhileStatementNoShortIf):
    def __init__(self, expression, statement_no_short_if):
        self.expression = expression
        self.statement_no_short_if = statement_no_short_if

    def accept(self, visitor):
        pass


# do_statement : KEYWORD_DO statement KEYWORD_WHILE LPAREN expression RPAREN SEMICOLON

class DoStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteDoStatement(DoStatement):
    def __init__(self, statement, expression):
        self.statement = statement
        self.expression = expression

    def accept(self, visitor):
        pass


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


class ForParamsWithoutVariableDeclaration(ForParams):
    def __init__(self, for_param1, for_param2, expression_list=None):
        self.for_param1 = for_param1
        self.for_param2 = for_param2
        self.expression_list = expression_list

    def accept(self, visitor):
        pass


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


class ExpressionListForParam(ForParam):
    def __init__(self, expression_list):
        self.expression_list = expression_list

    def accept(self, visitor):
        pass


# for_statement : KEYWORD_FOR LPAREN for_params RPAREN statement

class ForStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteForStatement(ForStatement):
    def __init__(self, for_params, statement):
        self.for_params = for_params
        self.statement = statement

    def accept(self, visitor):
        pass


# for_statement_no_short_if : KEYWORD_FOR LPAREN for_params RPAREN statement_no_short_if

class ForStatementNoShortIf(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteForStatementNoShortIf(ForStatementNoShortIf):
    def __init__(self, for_params, statement_no_short_if):
        self.for_params = for_params
        self.statement_no_short_if = statement_no_short_if

    def accept(self, visitor):
        pass


# switch_stm : KEYWORD_SWITCH LPAREN expression RPAREN LBRACE switch_itens RBRACE

class SwitchStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteSwitchStatement(SwitchStatement):
    def __init__(self, expression, switch_itens):
        self.expression = expression
        self.switch_itens = switch_itens

    def accept(self, visitor):
        pass


