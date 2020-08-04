from random import randint

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_menor = 0
numero_maior = 100
numero_secreto = randint(numero_menor, numero_maior)
total_de_tentativas = 0
acertou = False

def pesquisa_binaria(esquerda , direita):
    chute = (esquerda + direita) // 2
    return chute

while not acertou:
    print("Tentativa {} ".format(total_de_tentativas))

    chute = pesquisa_binaria(numero_menor, numero_maior)
    print("Pesquisa binaria escolheu ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("A Pesquisa Binaria acertou em {} tentativas!".format(total_de_tentativas))
        break
    else:
        if (maior):
            print("Errou! A Pesquisa Binaria foi maior do que o número secreto.")
            numero_maior = chute
        elif (menor):
            print("Errou! A Pesquisa Binaria foi menor do que o número secreto.")
            numero_menor = chute
        total_de_tentativas += 1

print("Fim do jogo")