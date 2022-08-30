class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
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

    #Metodo de pegar elemento de acordo com index
    def __getitem__(self, index):
        if self._size > 0:
            pointer = self.first
            for item in range(index):
                if pointer:
                    pointer = pointer.next
            if pointer:
                return pointer.data

    #Metodo de trocar elemento com index
    def __setitem__(self, index, element):
        if self._size > 0:
            pointer = self.first
            for i in range(index):
                if pointer:
                    pointer = pointer.next
            if pointer:
                pointer.data = element

    #Metodo de mostrar fila
    def show(self):
        if self._size > 0:
            text = ""
            pointer = self.first
            while(pointer):
                text = text + str(pointer.data) + (" ")
                pointer = pointer.next
            return text


def main():
    string = input()
    queuePri = Queue()
    data = ""
    count = 0

    for char in string:
        if char == ";":
            queuePri.enqueue(data)
            data = ""
        else:
            data = str(data) + str(char)

    for index in range(queuePri.size()-1):
        data1 = int(queuePri[0])
        data2 = int(queuePri[1])
        if data1 > data2:
            queuePri.dequeue()
        elif data1 < data2:
            pointer = queuePri[0]
            queuePri[0] = queuePri[1]
            queuePri[1] = pointer
            count += 1
            queuePri.dequeue()

    print(count)


main()

