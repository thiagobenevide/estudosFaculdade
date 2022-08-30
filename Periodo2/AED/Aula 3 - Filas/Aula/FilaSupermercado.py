class Node():
    def __init__(self, data) -> None:
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

    def peek(self):
        if self._size > 0:
            elem = self.first.data
            return elem


    def show(self):
        if self._size > 0:
            text = ""
            pointer = self.first
            while(pointer):
                text = text + str(pointer.data) + (" ")
                pointer = pointer.next
            return text
        else:
            return "Empty Queue"


def quickSort(fila, inicio=0, fim=None):
    if fim is None:
        fim = fila.size()-1
    if inicio < fim:
        p = partition(fila, inicio, fim)
        quickSort(fila, inicio, p-1)
        quickSort(fila, p+1, fim)


def partition(fila, inicio, fim):
    pivot = fila[fim]
    i = inicio
    for j in range(inicio, fim):
        if fila[j] <= pivot:
            aux = fila[j] 
            fila[j] = fila[i]
            fila[i] = aux

    aux = fila[i]
    fila[i] = fila[fim]
    fila[fim] = aux
            

def selecao(filaPessoas, filaItens, filaMaiorDez,filaMenorDez):
    while filaPessoas.size() > 0:
        person = filaPessoas.dequeue()
        itens = filaItens.dequeue()

        if int(itens) > 10:
            filaMaiorDez.enqueue(person)
        elif int(itens) <= 10:
            filaMenorDez.enqueue(person)

    print(filaMenorDez.show())
    print(filaMaiorDez.show())
    

def main():
    string = input()+" "
    numbers = "0123456789"

    filaPessoas = Queue()
    filaItens = Queue()
    filaMaiorDez = Queue()
    filaMenorDez = Queue()

    name = ""
    itens = ""
    for char in string:
        if char == " ":
            filaPessoas.enqueue(name)
            filaItens.enqueue(itens)
            name = ""
            itens = ""
        elif char in numbers:
            itens = str(itens) + str(char)
        elif char != " " and char != "-":
            name = name + char

    selecao(filaPessoas, filaItens,filaMaiorDez,filaMenorDez)
    print(filaMaiorDez.peek())

main()