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

tamanhos_listas = [20000,40000,60000,80000,100000]
tempos = []

def mergeSort(lista, primeiro, ultimo):
    if (primeiro < ultimo):
        meio = (primeiro + ultimo)//2
        mergeSort(lista, primeiro, meio)
        mergeSort(lista, meio+1, ultimo)
        junta(lista, primeiro, meio, ultimo)

    return

def junta(lista, primeiro, meio, ultimo):
    esq = lista[primeiro:meio]
    dir = lista[meio:ultimo+1]
    esq.append(99999999999999)
    dir.append(99999999999999)
    i = j = 0
    for k in range (primeiro, ultimo+1) :
        if esq[i] <= dir[j]:
            lista[k] = esq[i]
            i += 1
        else:
            lista[k] = dir[j]
            j += 1


for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    print("lista com", tamanho)
    agora = time.time()
    mergeSort(lista, 0 , len(lista)-1)
    depois = time.time()
    tempos.append(depois - agora)


desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo", "quickSortListaAleatoria")
