class Extrator_Argumentos_Url:
    def __init__(self, url):
        if self.url_eh_valido(url):
            self.url = url
        else:
            raise LookupError("Url Inválida!!!!")

    @staticmethod
    def url_eh_valido(git url):
        if url:
            return True
        else:
            return False