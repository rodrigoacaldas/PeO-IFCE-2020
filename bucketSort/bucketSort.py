import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import time

def desenhaGrafico(x, y, xl="Entradas", yl="Saídas",name="bucketSort"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

def geraLista(tam):
    lista = random.sample(range(1, tam+1), tam)
    return lista

tamanhos_listas = [15000,25000,35000,45000,55000]
tempos = []

def bucketSort(lista):
    bucket = [[], [], [], [], []]
    for i in range(len(lista)):
        divisor = len(lista)//5
        num = lista[i]
        if num < divisor:
            bucket[0].append(lista[i])

        elif num < divisor*2:
            bucket[1].append(lista[i])

        elif num < divisor*3:
            bucket[2].append(lista[i])

        elif num < divisor*4:
            bucket[3].append(lista[i])

        else:
            bucket[4].append(lista[i])

    for j in range(len(bucket)):
        lista_aux = insertSort(bucket[j])
        bucket[j] = lista_aux

    lista = []
    for listaAux in bucket:
        for num in listaAux:
            lista.append(num)

    return lista

def insertSort(lista):
    n = len(lista)
    # print(lista)
    for i in range(n):
        chave = lista[i]
        y = i - 1
        while chave < lista[y] and y >= 0:
            lista[y + 1] = lista[y]
            y -= 1
        lista[y + 1] = chave
    # print(lista)
    return lista


for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    print("lista com", tamanho)
    agora = time.time()
    ordenada = bucketSort(lista)
    depois = time.time()
    tempos.append(depois - agora)


desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo", "bucketSortListaAleatoria")
