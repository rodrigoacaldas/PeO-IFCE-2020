import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import time

def desenhaGrafico(x, y, xl="Entradas", yl="Saídas",name="coutingSort"):
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

tamanhos_listas = [30000,40000,50000,60000,70000]
tempos = []

def coutingSort(lista):
    contando = {}
    for n in lista:
        if n not in contando:
            contando[n] = 0
        contando[n] += 1
    ordenada = []
    for n, contado in sorted(contando.items()):
        for i in range(contado):
            ordenada.append(n)
    return ordenada

for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    print("lista com", tamanho)
    agora = time.time()
    ordenada = coutingSort(lista)
    depois = time.time()
    tempos.append(depois - agora)


desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo", "coutingSortListaAleatoria")
