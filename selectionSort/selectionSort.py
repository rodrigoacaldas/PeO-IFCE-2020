import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import time

def desenhaGrafico(x, y, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('selectionSort.png')

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

tamanhos_listas = [1000, 10000, 30000, 60000]
tempos = []

def selectionSort(lista):
    agora = time.time()
    loop = 0
    n = len(lista)
    #print(lista)
    for i in range(n):
        atual = lista[i]
        for j in range(i+1, n):
            loop = loop + 1
            if (atual > lista[j]):
                aux = atual
                atual = lista[j]
                lista[j] = aux
        lista[i] = atual

    depois = time.time()
    print("Loops feitos para a lista com", n, "numeros:", loop)
    #print(lista)
    return depois - agora

for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    tempo = selectionSort(lista)
    tempos.append(tempo)

desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo")