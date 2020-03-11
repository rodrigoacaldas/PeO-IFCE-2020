import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import time

def desenhaGrafico(x, y, xl="Entradas", yl="Saídas", nome="bubblesort"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(nome+'.png')

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def geraListaInvertida(tam):
    lista_inv = []
    for i in range(tam):
        lista_inv.append(tam-i)
    return lista_inv

tamanhos_listas = [1000,10000,30000,60000]
tempos = []
tempos_inv = []

def bublesort(lista):
    agora = time.time()
    loop = 0
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            loop+=1
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]

    depois = time.time()
    tmp = depois-agora
    print("Loops feitos para a lista com", n, "numeros:", loop, "e esse proceso demorou:", tmp, "segundos")

    return tmp

for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    tempo = bublesort(lista)
    tempos.append(tempo)

for tamanho in tamanhos_listas:
    lista = geraListaInvertida(tamanho)
    tempo_inv = bublesort(lista)
    tempos_inv.append(tempo_inv)

desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo", "bubblesortListaAleatoria")
desenhaGrafico(tamanhos_listas, tempos_inv, "Tamanho", "Tempo", "bubblesortListaInvertida")