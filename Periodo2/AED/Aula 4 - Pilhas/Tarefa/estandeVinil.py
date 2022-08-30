class No:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.start = None
        self._size = 0

    def push(self, item):
        new_node = No(item)
        if self.start == None:
            self.start = new_node
        else:
            pointer = self.start
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = new_node
        self._size = self._size + 1 

    def pop(self):
        if self.start != None:
            pointer = self.start
            while pointer.next.next != None:
                pointer = pointer.next
            data = pointer.data
            pointer.next = None
            return data
        self._size = self._size - 1 

    def top(self, data=None):
        if self._size > 0:
            if data != None:
                pointer = self.start
                for i in range(data):
                    if pointer:
                        pointer = pointer.next
                if pointer:
                    return pointer.data
        else:
            return self.start
     
    def size(self):
        return self._size

bandStack = Stack()

def organizeShelf(stack):
    string = input() + ";"
    numbers = "0123456789"

    year = "("
    band = ""
    band_year = ""
    pointer = 0

    for data in string:
        if data == ";" and pointer in numbers:
            band_year = band + year + ")"
            stack.push(band_year)
            band_year = ""
            band = ""
            year = "("
        elif data == ";" and pointer not in numbers:
            data = ""
        elif data in numbers:
            year = year + data

        else:
            band  = band + data 
        pointer = data
    
    print(stack.top(0))

organizeShelf(bandStack)


