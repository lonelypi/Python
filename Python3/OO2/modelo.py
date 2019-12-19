#################################Classe Mãe###################################################
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

    def imprime(self):
        print(f"{self._nome} - {self.ano} - {self._likes} Likes")

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

#######################Classes filhas de Programa##########################################

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"

    def valores_diferentes_para_filme(self):
        pass


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"


#Playlist(list)##Uso como se fosse list, list é um tipo, que é interavel
class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)



######################MAIN DO CODIGO, ONDE OS TESTES DAS CLASSES DO CURSO DE OO2 IRAO OCORRER!!#########################
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
panico = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)
vingadores.nome = 'vingadores - guerra inifinita parte 2'


vingadores.dar_likes()
atlanta.dar_likes()
panico.dar_likes()
panico.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
filmes_e_series = [vingadores, atlanta, demolidor, panico]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f"\nTamanho da playlist: {len(playlist_fim_de_semana)}\n\nPlaylist:".title())

for programa in playlist_fim_de_semana:
    print(programa)

print(f"\nTá ou não está? {demolidor in playlist_fim_de_semana}")

# for programa in filmes_e_series:
#     detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
#     programa.imprime()

