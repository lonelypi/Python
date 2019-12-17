# Definição de uma classe em Python para iniciar com OO
class Conta:

    # Construtor do Python, self cria os atributos da classe.
    def __init__(self, numero, titular, saldo=0.0, limite=1000.0):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero  # Definimos como atributos privados ao colocar duas _ _ seguidos no nome do
        self.__titular = titular  # atributo. Servindo como aviso para os desenvolvedores.
        self.__saldo = saldo
        self.__limite = limite


    ##Propriedades realizadas para fazer getters and setters, em python usamos a annotation @ pra property##

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    ##########################################################################################################

    def extrato(self):
        print(f"Saldo {self.__saldo} do {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print(f"Valor sacado com sucesso!")
        else:
            print(f"O valor {valor} passou do limite!")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

        ##Uma classe deve ser coesa, deve ter uma única responsabilidade, um única razão para se alterar.##
