from tkinter import *
import math
import random
#
# arvores binárias com gráfico
#


class Noh:  # definição da classe Nó
    def __init__(self, dado=None):
        self.esquerdo = None
        self.direito = None
        self.dado = dado

    def __str__(self):
        return "{", str(dado), "}"

# fim da classe Noh


class ArvoreBinaria: 				# Definição da classe árvore
    def __init__(self):
        self.raiz = None 			# inicializa a raiz

    def criaNoh(self, dado):		# cria um novo noh e o retorna
        return Noh(dado)

    def insere(self, raiz, dado):  # insere um novo dado
        if raiz == None: 			# arvore vazia
            return self.criaNoh(dado)
        else:
            if dado <= raiz.dado:
                raiz.esquerdo = self.insere(raiz.esquerdo, dado)
            else:
                raiz.direito = self.insere(raiz.direito, dado)
        return raiz

    def contaNohs(self, raiz):
        if raiz == None:
            return 0
        return 1 + self.contaNohs(raiz.esquerdo) + self.contaNohs(raiz.direito)

    def calculaProfMaxima(self, raiz):
        if raiz == None:
            return 0
        return 1 + max(self.calculaProfMaxima(raiz.esquerdo), self.calculaProfMaxima(raiz.direito))


class Aplicacao:
    def __init__(self, pai):
        self.arvoreBinaria = None
        self.t1 = Entry(pai)
        self.t1.bind("<Return>", self.constroiArvore)
        self.t1.pack()
        self.b1 = Button(pai)
        self.b1.bind("<Button-1>", self.constroiArvore)
        self.b1["text"] = "ENTRE COM VALOR"
        self.b1.pack()
        self.b2 = Button(pai)
        self.b2["text"] = "Aleatória"
        self.b2.bind("<Button-1>", self.geraAleatoria)
        self.b2.pack()
        self.c1 = Canvas(pai, width=1024, height=650)
        self.c1.pack()

    def constroiArvore(self, *args):
        try:
            valor = int(self.t1.get())
        except Exception:
            return
        print(valor)
        if self.arvoreBinaria == None:
            print("Criando")
            self.arvoreBinaria = ArvoreBinaria()
            self.raiz = self.arvoreBinaria.criaNoh(valor)
        else:
            print("Inserindo")
            self.arvoreBinaria.insere(self.raiz, valor)
        self.desenhaArvore()

    def desenhaArvore(self):
        self.HORIZONTAL = 1024
        self.VERTICAL = 750
        self.tamanho = 30
        self.c1.delete(ALL)
        self.c1.create_rectangle(
            0, 0, self.HORIZONTAL, self.VERTICAL, fill="red")
        self.xmax = self.c1.winfo_width() - 40  # margem de 40
        self.ymax = self.c1.winfo_height()
        self.numero_linhas = self.arvoreBinaria.calculaProfMaxima(self.raiz)
        x1 = int(self.xmax / 2 + 20)
        y1 = int(self.ymax / (self.numero_linhas + 1))
        self.desenhaNoh(self.raiz, x1, y1, x1, y1, 1)

    def desenhaNoh(self, noh, posAX, posAY, posX, posY, linha):
        if noh == None:
            return
        numero_colunas = 2**(linha + 1)
        x1 = int(posX - self.tamanho / 2)
        y1 = int(posY - self.tamanho / 2)
        x2 = int(posX + self.tamanho / 2)
        y2 = int(posY + self.tamanho / 2)
        self.c1.create_line(posAX, posAY, posX, posY, fill="white")
        self.c1.create_oval(x1, y1, x2, y2, fill="white")
        self.c1.create_text(posX, posY, text=str(noh.dado))
        posAX, posAY = posX, posY
        dx = self.xmax / numero_colunas
        dy = self.ymax / (self.numero_linhas + 1)
        posX = posAX + dx
        posY = posAY + dy
        self.desenhaNoh(noh.direito, posAX, posAY, posX, posY, linha + 1)
        posX = posAX - dx
        self.desenhaNoh(noh.esquerdo, posAX, posAY, posX, posY, linha + 1)

    def geraAleatoria(self, *args):
        try:
            valor = int(self.t1.get())
        except Exception:
            return
        self.arvoreBinaria = ArvoreBinaria()
        self.raiz = self.arvoreBinaria.criaNoh(
            random.randint(10 * valor, 100 * valor))
        for i in range(valor - 1):
            self.raiz = self.arvoreBinaria.insere(
                self.raiz, random.randint(10 * valor, 100 * valor))
        self.desenhaArvore()

if __name__ == "__main__":
    root = Tk(None, None, "Desenhando Uma Árvore Binária")
    root.geometry("1024x750")
    ap = Aplicacao(root)
    root.mainloop()

# fim do programa