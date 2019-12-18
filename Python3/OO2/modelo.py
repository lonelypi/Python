class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def valores_diferentes_para_filme(self):
        pass

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas






##################MAIN DO CODIGO, ONDE OS TESTES DAS CLASSES DO CURSO DE OO2 IRAO OCORRER!! ##############


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.nome = 'vingadores - guerra inifinita parte 2'
vingadores.dar_likes()
print(f"{vingadores.nome} - {vingadores.duracao} : {vingadores.likes} ")

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
print(f"{atlanta.nome} - {atlanta.temporadas} : {atlanta.likes} ")