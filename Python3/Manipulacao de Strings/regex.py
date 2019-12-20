import re

email_um = "Meu numero e 1234-1234"
email_dois = "Fala comigo em 1234-1234 esse e o meu telefone"
email_tres = "1234-1234 e o meu celular"
email_quatro = "lalala 981231209 lalala lalala lal alalala 93425-0912 lalalalala 1234-1234"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email_quatro)
print(retorno)