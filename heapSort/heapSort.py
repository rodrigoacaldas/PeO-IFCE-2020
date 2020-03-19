import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import time

def desenhaGrafico(x, y, xl="Entradas", yl="Saídas",name="heapSort"):
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

def heapSort(lista):
    montaArvore(lista)

    tamanho_lista = len(lista)

    for i in range(len(lista)-1, 0, -1):
        aux = lista[i]
        lista[i] = lista[0]
        lista[0] = aux
        tamanho_lista = tamanho_lista -1
        ordenaArvore(lista, 0, tamanho_lista)

    return lista

def montaArvore(lista):
    posicao = int((len(lista)-1) / 2)
    for i in range(posicao, -1, -1):
        ordenaArvore(lista, i, len(lista))


def ordenaArvore(lista, posicao, tam_vertor):
    ind_filho_1 = 2 * posicao + 1
    ind_filho_2 = ind_filho_1 + 1

    if ind_filho_1 < tam_vertor:
        # se estivermos dentro do vetor testar qual maior filho
        if ind_filho_2 < tam_vertor:
            if lista[ind_filho_1] < lista[ind_filho_2]:
                ind_filho_1 = ind_filho_2

        #compara filho com o pai
        if lista[ind_filho_1] > lista[posicao]:
            aux = lista[ind_filho_1]
            lista[ind_filho_1] = lista[posicao]
            lista[posicao] = aux

            ordenaArvore(lista, ind_filho_1, tam_vertor)


for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    print("lista com", tamanho)
    agora = time.time()
    ordenada = heapSort(lista)
    depois = time.time()
    tempos.append(depois - agora)


desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo", "heapSortListaAleatoria")
