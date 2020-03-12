import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import time

def desenhaGrafico(x, y, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('shellSort.png')

def geraLista(tam):
    lista = random.sample(range(0, tam + 1), tam)
    return lista

tamanhos_listas = [30000,40000,50000,60000,70000]
tempos = []

def insertSort(lista):
    agora = time.time()
    contador = 0
    n = len(lista)
    #print(lista)
    h = n//2
    while h > 0:
        i = h
        while i < len(lista):
            temp = lista[i]
            trocou = False
            j = i - h
            while j >= 0 and lista[j] > temp:
                lista[j+h] = lista[j]
                trocou = True
                j -= h
                contador += 1 #só pra saber quantos loops foi feito

            if trocou:
                lista[j+h] = temp

            i += 1

        h = h // 2


    depois = time.time()
    print("Loops feitos para a lista com", n, "numeros:", contador)
    #print(lista)

    return depois - agora

for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    tempo = insertSort(lista)
    tempos.append(tempo)

desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo")