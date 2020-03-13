import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import time

def desenhaGrafico(x, y, xl="Entradas", yl="Saídas",name="radixSort"):
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

tamanhos_listas = [20000,30000,40000,50000,60000]
tempos = []

def radixSort(lista):
   divisao = 1
   mod = 10
   start = True
   while start:
       start = False
       aux = [[], [], [], [], [], [], [], [], [], []]
       for num in lista:
           posicao = num % mod // divisao
           aux[posicao].append(num)
           if not start and posicao > 0:
               start = True

       lista = []
       for listaAux in aux:
           for num in listaAux:
               lista.append(num)

       mod = mod * 10
       divisao = divisao * 10
   return lista



for tamanho in tamanhos_listas:
    lista = geraLista(tamanho)
    print("lista com", tamanho)
    agora = time.time()
    ordenada = radixSort(lista)
    depois = time.time()
    #print(ordenada)
    tempos.append(depois - agora)


desenhaGrafico(tamanhos_listas, tempos, "Tamanho", "Tempo", "radixSortListaAleatoria")
