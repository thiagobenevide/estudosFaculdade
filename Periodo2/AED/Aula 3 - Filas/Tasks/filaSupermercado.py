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


#Algoritmo de Ordenacao QuickSort
def quicksort(structure, start=0, end=None):
    if end is None:
        end = structure.size()-1
    if start < end:
        pivot = partition(structure, start, end)
        quicksort(structure, start, pivot-1) 
        quicksort(structure, pivot+1, end)

#Funcao auxiliar para o algoritmo de ordenacao quickSort
def partition(structure, start, end):
    pivot = structure[end]
    i = start
    for j in range(start, end):
        if structure[j] <= pivot:
            aux = structure[j]
            structure[j] = structure[i]
            structure[i] = aux 
            i = i + 1

    aux = structure[i]
    structure[i] = structure[end]
    structure[end] = aux    
    return i 

#Separacao entre fila maior que dez e menor que dez
def selecao(queuePeople,queueItens, queueMajorTen,queueMenoDec):
    while queuePeople.size() > 0:
        person = queuePeople.dequeue()
        itens =     queueItens.dequeue()

        if int(itens) > 10:
            queueMajorTen.enqueue(person)
        elif int(itens) <= 10:
            queueMenoDec.enqueue(person)
    
    quicksort(queueMajorTen)
    quicksort(queueMenoDec)
    
    
    print(queueMenoDec.show())
    print(queueMajorTen.show())


#Funcao prinicipal e inicial para realizacao do programa
def main():
    string = input()+" "
    numbers = "0123456789"

    queuePeople = Queue()
    queueItens = Queue()
    queueMajorTen = Queue()
    queueMenoDec = Queue()

    name = ""
    itens = ""
    for char in string:
        if char == " ":
            queuePeople.enqueue(name)
            queueItens.enqueue(itens)
            name = ""
            itens = ""
        elif char in numbers:
            itens = str(itens) + str(char)
        elif char != " " and char != "-":
            name = name + char

    selecao(queuePeople,queueItens,queueMajorTen,queueMenoDec)

    
main()

