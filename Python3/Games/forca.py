
def jogar():
    print("*********************************")
    print("***Bem vindo no jogo da Forca ***!")
    print("*********************************", end="\n\n")

    palavra_secreta = "banana"

    #lista usada de primeira maneira, para entendermos listas inicialmente. Em seguida fomos para tuplas.
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    #Enquanto não enforcou & não acertou.
    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip()
        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()