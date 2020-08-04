from random import randint

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_menor = numero_menor_maquina = 0
numero_maior = numero_maior_maquina = 100
numero_secreto = randint(numero_menor, numero_maior)

total_de_tentativas_humana = 0
total_de_tentativas_maquina = 0
acertou_humano = False
acertou_maquina = False

while not acertou_humano:
    print("Tentativa Humana {} ".format(total_de_tentativas_humana))

    chute_str = input("Digite um número entre {} de {} ".format(numero_menor, numero_maior))
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if (chute < numero_menor or chute > numero_maior):
        print("Você deve digitar um número entre {} e {}!".format(numero_menor, numero_maior))
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
            numero_maior = chute
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            numero_menor = chute
        total_de_tentativas_humana += 1

print("Fim do jogo Humano!")


def pesquisa_binaria(esquerda , direita):
    chute = (esquerda + direita) // 2
    return chute


while not acertou_maquina:

    chute = pesquisa_binaria(numero_menor_maquina, numero_maior_maquina)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        break
    else:
        if (maior):
            numero_maior_maquina = chute
        elif (menor):
            numero_menor_maquina = chute
        total_de_tentativas_maquina += 1


print("Você descobriu o numero secreto em {} tentativas".format(total_de_tentativas_humana))
print("O computador descobriu o numero secreto em {} tentativas".format(total_de_tentativas_maquina))

