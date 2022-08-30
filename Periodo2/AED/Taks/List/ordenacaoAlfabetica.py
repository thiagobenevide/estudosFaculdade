class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class List:
    def __init__(self):
        self.start = None
        self._size = 0

    def impressList(self):
        pointer = self.start
        text = ""
        while pointer != None:
            text = text + str(pointer.data) + ' '
            pointer = pointer.next
        print(text)

    def addElement(self, elem):
        if self.start is None:
            self.start = Node(elem)
        else:
            pointer = self.start
            while (pointer.next != None):
                pointer = pointer.next
            pointer.next = Node(elem) #type: ignore
        self._size = self._size + 1
    
    def size(self):
        return self._size
        
    def stringDouble(self):
        pass

    def orderAlpha(self):
        pass


s = input()

if s[-1] == ' ':
    string = s
else:
    string = s + ' '

list1 = List()
list2 = List()

newString = ""
for key in string:
    if key != " ":
        newString =  newString + key
    else:
        list1.addElement(newString)
        newString = ""

list1.impressList()
