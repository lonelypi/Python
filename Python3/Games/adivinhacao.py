import random

# fim das importações #

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(0, 101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nível é a dificuldade?")
    print("(1) Fácil, (2) Médio e (3) Difícil.")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        numero = int(chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        print("Você digitou: ", chute_str)

        if(acertou):
            print(f"Você acertou! E fez {pontos} pontos")
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #exemplo: 40 - 20 = 20
            pontos = pontos - pontos_perdidos

        # rodada += 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()