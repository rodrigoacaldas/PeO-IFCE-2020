import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import time

def desenhaGrafico(x, y, xl="Entradas", yl="Saídas",name="selectionSort"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

def geraLista(tam):
    lista = random.sample(range(0, tam+1), tam)
    return lista

tamanhos_listas = [100000,200000,300000,400000,500000]
tempos = []

def quickSort(lista, esq, dir):
    if(esq < dir):
        j = separar(lista, esq, dir)
        quickSort(lista, esq, j-1)
        quickSort(lista, j+1, dir)
    return

def separar(lista, esq, dir):
    i = esq + 1
    j = dir
    pivo = lista[esq]
    while (i <= j):
        if (lista[i] <= pivo):
            i = i + 1
        elif (lista[j] > pivo):
            j = j - 1
        elif (i <= j):
            trocar(lista, i, j)
            i = i + 1
            j = j - 1

    trocar(lista, esq, j)
    return j

def trocar(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    print("lista com", tamanho)
    agora = time.time()
    quickSort(lista, 0 , len(lista)-1)
    depois = time.time()
    #print(lista)
    tempos.append(depois - agora)


desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo", "quickSortListaAleatoria")
