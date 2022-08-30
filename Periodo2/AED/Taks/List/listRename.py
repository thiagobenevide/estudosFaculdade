class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListSimple:
    def __init__(self):
        self.start = None
        self._size = 0

    #Adicionar o elemento

    def addElement(self, elem):
        if self.start is None:
            self.start = Node(elem)
        else:
            pointer = self.start
            while (pointer.next != None):
                pointer = pointer.next
            pointer.next = Node(elem) #type: ignore
        self._size = self._size + 1

    #Tamanho

    def size(self):
        return self._size


    def getNode(self, index):
        pointer = self.start
        for key in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    #Pegar Elemento

    def get(self, index):
        pointer = self.getNode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    #Trocar o elemento e pegar

    def set(self, index, elem):
        pointer = self.getNode(index)
        if pointer:
            pointer.data = elem
            return pointer.data
        else:
            raise IndexError("list index out of range")

    #Encontrar indice do elemento

    def index(self, elem):
        pointer = self.start
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError(f"{elem} is not in list")

    #inserir em qualquer posição

    def insertItem(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.start #type: ignore
            self.start = node
        else:
            pointer = self.getNode(index-1)
            node.next = pointer.next #type: ignore
            pointer.next = node         #type: ignore
        self._size =  self._size + 1

    #Função para remover elementos

    def remove(self, elem):
        if self.start == None:
            raise ValueError(f"{elem} is not in list kkkk")
        elif self.start.data == elem:
            self.start = self.start.next
            return True
        else:
            ancestor = self.start
            pointer = self.start.next
            while(pointer):
                    if pointer.data == elem:
                        ancestor.next = pointer.next 
                        pointer.next = None
                        self._size = self._size - 1 
                    ancestor = pointer
                    pointer = pointer.next  #type: ignore
            return True
        raise ValueError(f"{elem} is not in list")

    def impressList(self):
        pointer = self.start
        text = ""
        while pointer != None:
            text = text + str(pointer.data) + ' '
            pointer = pointer.next
        print(text)                            



lista = ListSimple()






