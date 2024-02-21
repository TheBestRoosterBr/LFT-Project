from abc import abstractmethod
from abc import ABC


# Gramática
# programa: listadecomandos
# listadecomandos: comando
#                | listadecomandos comando
# comando: VAR ID ATRIBUICAO expressao PONTOEVIRGULA
#         | ID ATRIBUICAO expressao PONTOEVIRGULA
#         | IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
#         | WHILE expressao DO listadecomandos ENDWHILE
# expressao: expressao MAIS expressao
#                  | expressao MENOS expressao
#                  | expressao VEZES expressao
#                  | expressao DIVIDE expressao
#                  | ID
#                  | NUMERO


# Programa
class Programa():
    def __init__(self, listadecomandos):
        self.listadecomandos = listadecomandos

    @abstractmethod
    def print(self):
        self.listadecomandos.print()


# Listadecomandos
class Listadecomandos(ABC):
    @abstractmethod
    def print(self):
        pass


class UmComando(Listadecomandos):
    def __init__(self, comando):
        self.comando = comando

    def print(self):
        print('[UmComando]', end='')
        self.comando.print()


class MaisdeUmComando(Listadecomandos):
    def __init__(self, listadecomandos, comando):
        self.comando = comando
        self.listadecomandos = listadecomandos

    def print(self):
        print('[MaisdeUmComando', end='')
        self.comando.print()
        self.listadecomandos.print()


# Comando
class Comando(ABC):
    @abstractmethod
    def print(self):
        pass


class DeclaracaoVariavel(Comando):
    def __init__(self, ID, expressao):
        self.ID = ID
        self.expressao = expressao

    def print(self):
        print('[DeclaracaoVariavel]', end='')
        self.expressao.print()


class AtribuicaoVariavel(Comando):
    def __init__(self, ID, expressao):
        self.ID = ID
        self.expressao = expressao

    def print(self):
        print('[AtribuicaoVariavel]')
        self.expressao.print()


class ComandoIfElse(Comando):
    def __init__(self, expressao, lista_de_comandos_if, lista_de_comandos_else):
        self.expressao = expressao
        self.lista_de_comandos_if = lista_de_comandos_if
        self.lista_de_comandos_else = lista_de_comandos_else

    def print(self):
        print('[ComandoIfElse]', end='')
        self.expressao.print()
        self.lista_de_comandos_if.print()
        self.lista_de_comandos_else.print()


class ComandoWhile(Comando):
    def __init__(self, expressao, lista_de_comandos):
        self.expressao = expressao
        self.lista_de_comandos = lista_de_comandos

    def print(self):
        print('[ComandoWhile]', end='')
        self.expressao.print()
        self.lista_de_comandos.print()


# Expressao
class Expressao(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def print(self):
        print('[Expressao]', end='')


class ExpressaoSoma(Expressao):
    def __init__(self, expressao1, expressao2):
        super().__init__()
        self.expressao1 = expressao1
        self.expressao2 = expressao2

    def print(self):
        print('[ExpressaoSoma]', end='')
        self.expressao1.print()
        self.expressao2.print()


class ExpressaoMenos(Expressao):
    def __init__(self, expressao1, expressao2):
        super().__init__()
        self.expressao1 = expressao1
        self.expressao2 = expressao2

    def print(self):
        print('[ExpressaoMenos]', end='')
        self.expressao1.print()
        self.expressao2.print()


class ExpressaoVezes(Expressao):
    def __init__(self, expressao1, expressao2):
        super().__init__()
        self.expressao1 = expressao1
        self.expressao2 = expressao2

    def print(self):
        print('[ExpressaoVezes]', end='')
        self.expressao1.print()
        self.expressao2.print()


class ExpressaoDivisao(Expressao):
    def __init__(self, expressao1, expressao2):
        super().__init__()
        self.expressao1 = expressao1
        self.expressao2 = expressao2

    def print(self):
        print('[ExpressaoDivisao]', end='')
        self.expressao1.print()
        self.expressao2.print()


class ExpressaoId(Expressao):
    def __init__(self, ID):
        super().__init__()
        self.ID = ID

    def print(self):
        print('[ExpressaoId]', end='')

class ExpressaoNumero(Expressao):
    def __init__(self, numero):
        self.numero = numero

    def print(self):
        print('[ExpressaoNumero]', end='')