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
        text = "Lista: ["
        counter = 1
        if self._size == 1:
            text = str(pointer.data) #type: ignore
        else:
            while pointer != None and counter < last:
                text = text + str(pointer.data)
                pointer = pointer.next
                counter += 1
            text = text + str(pointer.data) + "]" #type: ignore
        print(text)

    def get(self, index):
        pointer = self.start
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data


s = input()
id = int(input())

list1 = List()
list2 = List()

for i in s:
    list1.addElement(i)

caracter = list1.get(5)
print(caracter)

list1.impressList()
