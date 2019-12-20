class Extrator_Argumentos_Url:
    def __init__(self, url):
        if self.url_eh_valido(url) and url.startswith("https://bytebank.com"):
            self.url = url.lower()
        else:
            raise LookupError("Url Inválida!!!!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moeda_origem, moeda_destino = self.extrai_argumentos()
        representacao_string = self.extrai_valor()
        return f"Valor: {representacao_string} \nMoeda Origem: {moeda_origem}" \
               f"\nMoeda Destino: {moeda_destino}"

    def __eq__(self, other):
        return self.url == other.url
    #Defino que a comparacao sera pelas urls e nao mais por ids.

    @staticmethod
    def url_eh_valido(url):
        if url:
            return True
        else:
            return False

    def extrai_argumentos(self):
        busca_moeda_origem = "moedaorigem="
        busca_moeda_destino = "moedadestino="
        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find("&")

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
            indice_final_moeda_origem = self.url.find("&")

            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)
        indice_final_moeda_destino = self.url.find("&valor")
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino

    def extrai_valor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.encontra_indice_inicial(busca_valor)
        valor = self.url[indice_inicial_valor:]
        return valor

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)