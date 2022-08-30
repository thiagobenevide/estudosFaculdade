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
        

def insertionSort(list):
    for j in range(list.size()):
        key = list[j]
        i = j-1
        while i >= 0 and list[i] >= key:
            list[i+1] = list[i]
            i -= 1
        list[i+1] = key


s = input()

if s[-1] == ' ':
    string = s
else:
    string = s + ' '

list1 = List()
list2 = List()
listStart = List()
listEnd = List()

newString = ""
for key in string:
    if key != " ":
        newString =  newString + key
    else:
        listStart.addElement(newString)
        list1.addElement(newString.upper())
        newString = ""            

def removeDuplicate(listA, listB):
    for i in range(listA.size()):
        if listA[i] not in listB:
            listB.addElement(listA[i])

def addRemove(listA,listB):
    for i in range(listA.size()):
        elemA = listA[i]
        for j in range(listB.size()):
            elemB = listB[j]
            if elemA == elemB.upper():
                pointer = listA[i]
                listA[i] = listB[j]
                listB[j] = pointer

removeDuplicate(list1,list2)
removeDuplicate(listStart, listEnd)
insertionSort(list2)
addRemove(list2, listEnd)
list2.impressList()

