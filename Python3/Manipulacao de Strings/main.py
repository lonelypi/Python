from ExtratorArgumentosUrl import Extrator_Argumentos_Url

url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=700"

# index = url.find("moedadestino") + len("moedadestino") + 1
# sub_string = url[index:]
# print(sub_string)

argumentos_url = Extrator_Argumentos_Url(url)
argumentos_url_2 = Extrator_Argumentos_Url(url)
#moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
#valor = argumentos_url.extrai_valor()
#print(moeda_origem, moeda_destino, valor)


#print(argumentos_url)

print(id(argumentos_url), id(argumentos_url_2))
print(argumentos_url == argumentos_url_2)




'''

"https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
#https://bytebank.com.br/cambio?

url = "https://www.bytebank.com.br/cambio?moedaorigem=real"
index = url.find("=")
sub_string = url[index + 1:]

print(sub_string)

list_argumetos = url.split("?")

print(list_argumetos)

indice = url.find("?")
print(url[indice + 1:])

string = None
string_2 = " "

if string:
    print("Has something here")
else:
    print("there's nothing here")

print(f'{type(string)} e {type(string_2)}')
'''