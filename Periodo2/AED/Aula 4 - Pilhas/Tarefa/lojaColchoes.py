class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
    
class Stack():
    def __init__(self):
        self.topStack = None
        self._size = 0
    
    def size(self):
        return self._size

    def push(self, item):
        if item != None:
            new_node = Node(item)
            new_node.previous = self.topStack
            self.topStack = new_node
            self._size = self._size + 1

    def pop(self):
        if self.topStack != None:
            data = self.topStack.data
            self.topStack = self.topStack.previous
            self._size = self._size - 1
            return data        

    def top(self, data=None):
        if self._size >= 0:
            if data != None:
                pointer = self.topStack
                for index in range(data):
                    if pointer:
                        pointer = pointer.previous
                if pointer:
                    return pointer.data
            else:
                item = self.pop()
                self.push(item)
                return item
        
mattressStack = Stack()
cartStack = Stack()
armazemStack = Stack()


def inputData(mattressStack, cartStack, armazemStack):
    cart = 0
    mattresses = 0

    for index in range(2):
        s = input()
        if index == 0:
            cart = int(s)
        elif index == 1:
            mattresses = int(s)

    for index in range(mattresses):
        mattressStack.push(mattresses-index)

    for index in range(cart):
        cartStack.push(cart-index)
    
    armazem(cart, mattresses, mattressStack, cartStack, armazemStack) 

def armazem(cart, mattresses, mattressStack, cartStack, armazemStack):
    if mattresses < cart:
        for index in range(mattresses):
            data = mattressStack.pop()
            cartStack.push(data)
        for index in range(mattresses):
            data2 = cartStack.pop()
            armazemStack.push(data2)
    elif mattresses % cart == 0:
        counter = mattresses
        while counter > 0:
            for index in range(cart):
                data = mattressStack.pop()
                cartStack.push(data)
            for index in range(cart):
                data2 = cartStack.pop()
                armazemStack.push(data2)
            counter = counter - cart
    elif mattresses % cart == 1:
        counter = mattresses
        while counter > 0:
            for index in range(cart):
                data = mattressStack.pop()
                cartStack.push(data)
            for index in range(cart):
                data2 = cartStack.pop()
                armazemStack.push(data2)
            counter = counter - cart
            cart = counter

    show(armazemStack)



def show(stack):
    text = ""
    for index in range(stack.size()):
        data = stack.top(index)
        text = text + str(data) + "\n"
    print(text)

inputData(mattressStack, cartStack, armazemStack)
