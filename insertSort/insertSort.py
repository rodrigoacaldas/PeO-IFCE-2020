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
    fig.savefig('insertSort.png')

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

tamanhos_listas = [1000, 10000, 30000, 60000]
tempos = []

def insertSort(lista):
    agora = time.time()
    n = len(lista)
    #print(lista)
    contador = 0
    for i in range(n):
        chave = lista[i]
        y = i - 1
        while chave < lista[y] and y >= 0:
            lista[y + 1] = lista[y]
            y -= 1
            contador += 1
        lista[y + 1] = chave
        contador += 1

    depois = time.time()
    print("Loops feitos para a lista com", n, "numeros:", contador)
    #print(lista)
    return depois - agora

for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    tempo = insertSort(lista)
    tempos.append(tempo)

desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo")