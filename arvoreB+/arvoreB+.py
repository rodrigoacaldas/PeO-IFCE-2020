from random import randint

class Noh(object):
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.values = []
        self.leaf = True

    def adiciona(self, key, value):
        if not self.keys:
            self.keys.append(key)
            self.values.append([value])
            return None

        for i, item in enumerate(self.keys):
            if key == item:
                self.values[i].append(value)
                break

            elif key < item:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                self.values = self.values[:i] + [[value]] + self.values[i:]
                break

            elif i + 1 == len(self.keys):
                self.keys.append(key)
                self.values.append([value])

    def split(self):

        left = Noh(self.order)
        right = Noh(self.order)
        mid = self.order // 2

        left.keys = self.keys[:mid]
        left.values = self.values[:mid]

        right.keys = self.keys[mid:]
        right.values = self.values[mid:]

        self.keys = [right.keys[0]]
        self.values = [left, right]
        self.leaf = False

    def is_full(self):
        return len(self.keys) == self.order

    def show(self, counter=0):

        print(counter, str(self.keys))

        if not self.leaf:
            for item in self.values:
                item.show(counter + 1)


class ArvoreBMais(object):

    def __init__(self, order=8):
        self.root = Noh(order)

    def _find(self, node, key):

        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i

        return node.values[i + 1], i + 1

    def _merge(self, parent, child, index):

        parent.values.pop(index)
        pivot = child.keys[0]

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + child.values + parent.values[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += child.values
                break

    def insere(self, key, value):

        parent = None
        child = self.root

        while not child.leaf:
            parent = child
            child, index = self._find(child, key)

        child.adiciona(key, value)

        if child.is_full():
            child.split()

            if parent and not parent.is_full():
                self._merge(parent, child, index)

    def retrieve(self, key):
        child = self.root

        while not child.leaf:
            child, index = self._find(child, key)

        for i, item in enumerate(child.keys):
            if key == item:
                return child.values[i]

        return None

    def show(self):
        self.root.show()


def arvore_bmais_exemplo(ordem, itens):
    print('Inicializando Árvore B+...')
    arvore = ArvoreBMais(order=ordem)

    for i in range(itens):
        arvore.insere(i, i*2)

    print("Árvore B+ com {} itens...".format(itens))
    arvore.show()

    chaveAProcurar1 = randint(0, i)
    chaveAProcurar2 = randint(0, i)
    print('Retornando valores da chave {}'.format(chaveAProcurar1))
    print(arvore.retrieve(chaveAProcurar1))

    print('Retornando valores da chave {}'.format(chaveAProcurar2))
    print(arvore.retrieve(chaveAProcurar2))


if __name__ == '__main__':
    print('\n')
    arvore_bmais_exemplo(4,20)

# In[ ]:
