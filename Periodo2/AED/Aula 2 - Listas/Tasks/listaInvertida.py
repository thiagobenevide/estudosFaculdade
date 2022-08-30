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
                text = text + str(pointer.data) + ", "
                pointer = pointer.next
                counter += 1
            text = text + str(pointer.data)
        print(f"Lista:[{text}]")

    def __getitem__(self, index):
        pointer = self.start
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("List index out of range")

    def __setitem__(self, index, element):
        pointer = self.start
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of rane")
        if pointer:
            pointer.data = element
        else:
            raise IndexError("List index out of rane")
        


def quicksort(structure, start=0, end=None):
    if end is None:
        end = structure.size()-1
    if start < end:
        pivot = partition(structure, start, end)
        quicksort(structure, start, pivot-1) 
        quicksort(structure, pivot+1, end)


def partition(structure, start, end):
    pivot = structure[end]
    i = start
    for j in range(start, end):
        if structure[j] >= pivot:
            aux = structure[j]
            structure[j] = structure[i]
            structure[i] = aux 
            i = i + 1

    aux = structure[i]
    structure[i] = structure[end]
    structure[end] = aux    
    return i 

listStart = List()

for i in range(2):
    if i == 0:
        string = input() + " "
    else:
        number = int(input())

newString = ""
for key in string:
    if key != " ":
        newString =  newString + key
    else:
        listStart.addElement(newString)
        newString = ""            

quicksort(listStart, number)
listStart.impressList()

