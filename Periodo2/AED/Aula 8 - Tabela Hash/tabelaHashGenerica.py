class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.start = None
        self._size = 0

    def size(self):
        return self._size

    def addElement(self, element):
        if self.start is None:
            self.start = Node(element)
        else:
            pointer = self.start
            while(pointer.next != None):
                pointer = pointer.next
            pointer.next = Node(element) #type: ignore
        self._size = self._size + 1

    def impressList(self):
        pointer = self.start
        last = self._size
        text = ""
        counter = 1
        if self._size == 1:
            text = str(pointer.data) #type: ignore
        else:
            while pointer != None and counter < last:
                text = text + str(pointer.data) + " "
                pointer = pointer.next
                counter += 1
            text = text + str(pointer.data)
        print(text)

    def __getitem__(self, index):
        pointer = self.start
        for i in range(index):
            if pointer:
                pointer = pointer.next
        if pointer:
            return pointer.data

    def __setitem__(self, index, element):
        pointer = self.start
        for i in range(index):
            if pointer:
                pointer = pointer.next
        if pointer:
            pointer.data = element

class HashTable():
    def __init__(self, number):
        self.lists = [List() for i in range(number)]
        self.number = number
    
    def add(self, value):
        key = self.hash(value)
        position = key % self.number
        self.lists[position].addElement(value)

    def getHash(self, value):
        h = 0
        for char in value:
            h += ord(value)
        return h % self.number

    def search(self, value):
        key = self.hash(value)
        position = key % self.number
        newList = self.lists[position]
        aux = newList.start
        while (aux != None):
            if aux.data == value:
                return True
            aux = aux.next

    def rehashing(self):
        pass

    def loadFactor(self):
        pass

        
    def impressTable(self):
        pass

    def remove(self, value):
        key = self.hash(value)
        position = key % self.number

if __name__ == '__main__':
    hash_table = HashTable(10)
    hash_table.add("Thiago")
    hash_table.add("José")
    hash_table.add("Anderson")

    hash_table.search("Thiago")
