class Node():
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
            element = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return element

    def show(self):
         if self._size > 0:
            text = ""
            pointer = self.first
            for i in range(self._size):
                text = str(pointer.data) + " " + str(text)
                pointer = pointer.next
            return text

def main():
    string = input()+" "

    queueNormal = Queue()

    data = ""

    for char in string:
        if char == " ":
            queueNormal.enqueue(data)
            data = ""
        else:
            data = str(data) + str(char)
    print(queueNormal.show())
    

main()