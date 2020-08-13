import random


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree(object):
    def insert(self, root, key):

        # Passo 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Passo 2 - Atualizar a altura do no antecessor
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Passo 3 - Pegar o fator de balanceamento
        balance = self.getBalance(root)

        # Passo 4 - Se o nó não estiver balanceado fazer uma das rotações abaixo
        # Caso 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Caso 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Caso 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Caso 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Rotacionar
        y.left = z
        z.right = T2

        # Atualizar alturas
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Retornar a nova raiz
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Rotacionar
        y.right = z
        z.left = T3

        # Atualizar alturas
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Retornar a nova raiz
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    # percurso em ordem pre ordem
    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    #percurso em ordem simétrica
    def inOrder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inOrder(node.left)
        print(node.val, end=' ')
        if node.right:
            self.inOrder(node.right)

    #percuso em pós ordem (primeiro a esquerda depois a direita depois raiz)
    def postOrder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postOrder(node.left)
        if node.right:
            self.postOrder(node.right)
        print("{} ".format(node.val), end='')

    def search(self, value, node=0,count=0):
        if node == 0:
            node = self.root
        if node is None:
            return node
        if node.val == value:
            return count
        if value < node.val:
            return self.search(value, node.left, count+1)
        return self.search(value, node.right, count+1)

def geraLista(tam):
    random.seed(3)
    lista = random.sample(range(1, tam+1), tam)
    return lista

if __name__ == "__main__":
    lista = geraLista(10000)

    myTree = AVL_Tree()
    root = None
    for noh in lista:
        root = myTree.insert(root, noh)

    print("Arvore em ordem pre ordenada")
    myTree.preOrder(root)
    print('')

    print('Arvore em ordem simétrica')
    myTree.inOrder(root)
    print('')

    print('Arvore em ordem pós ordem')
    myTree.postOrder(root)
    print('')


    print(root.val)
    print('Testando a busca')
    lista_procura = [122, 13, 20, 50,999,1000,1001]
    for item in lista_procura:
        procurar = myTree.search(item, root)
        if procurar is None:
            print("{} não foi encontrado".format(item))
        else:
            print("{} foi encontrado em {} interações".format(item, procurar))