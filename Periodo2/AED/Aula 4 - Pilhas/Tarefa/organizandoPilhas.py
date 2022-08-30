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

    def top(self, index=None):
        if self._size > 0:
            if index != None:
                pointer = self.start
                for i in range(index):
                    if pointer:
                        pointer = pointer.next
                if pointer:
                    return pointer.data
        else:
            return self.start
     
    def size(self):
        return self._size


oddStack = Stack()
pairStack = Stack()

string = input() + " "
number = ""

for index in string:
    if index == " ":
        if (int(number)%2) == 0:
            pairStack.push(number)
            number = ""
        elif (int(number)%2) == 1:
            oddStack.push(number)
            number = ""
    else:
        number = number + index

text1 = ""
for index in range(oddStack.size()):
    data  = oddStack.top(index)
    text1 = text1 + data + " "

text2 = ""
for index in range(pairStack.size()):
    data  = pairStack.top(index)
    text2 = text2 + data + " "

print(text2)
print(text1)