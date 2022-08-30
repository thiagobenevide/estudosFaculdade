# Primeira pessoa será a primeira
# Ultimo a chegar será o último a sair

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0


    def size(self):
        return self._size
    
    def enqueue(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node #type: ignore
            self.last = node

        if self.first is None:
            self.first = node
        
        self._size = self._size + 1
    
    def dequeue(self):
        if self.first is not None:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem

        raise IndexError("The stark is empty")

    def seeElement(self):
        if self._size > 0:
            elem = self.data.next #type: ignore
            return elem
        else:
            raise IndexError("The queue is empty")

    def display(self):
        if self._size > 0:
            text = ""
            pointer = self.first
            while(pointer):
                text = text + str(pointer.data) + (" ")
                pointer = pointer.next
            return text
        else:
            return "Empty Queue"

fila = Queue()

for i in range(4):
    s = input(f"Digite o elemento {i}: ")
    fila.enqueue(s)

for j in range(fila.size()):
    print(fila.dequeue())





