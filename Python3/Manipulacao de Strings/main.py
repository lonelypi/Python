from ExtratorArgumentosUrl import Extrator_Argumentos_Url

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
print(Extrator_Argumentos_Url(url))



'''
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