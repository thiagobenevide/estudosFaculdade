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


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rigth = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.elem = 10
    
    def insertLeft(self, rootNode, dataNode):
        if rootNode.left == None:
            rootNode.left = dataNode
        else:
            if dataNode.data <= rootNode.left.data:
                self.insertLeft(rootNode.left, dataNode)
            else:
                self.insertRight(rootNode.left, dataNode)


    def insertRight(self, rootNode, dataNode):
        if rootNode.rigth == None:
            rootNode.rigth = dataNode
        else:
            if dataNode.data > rootNode.rigth.data:
                self.insertRight(rootNode.rigth, dataNode)
            else:
                self.insertLeft(rootNode.rigth, dataNode)
                
        
    def add(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
            self.elem += 1
        else:
            if data <= self.root.data:
                self.insertLeft(self.root, node)
                self.elem += 1
            else:
                self.insertRight(self.root, node)
                self.elem += 1



    def show(self, node=None):
        print(str(node.data) + " ")
        if node.left:
            self.show(node.left)
        if node.rigth:
            self.show(node.rigth)

    def height(self, root):
        if root == None:
            return -1
        left = self.height(root.left)   
        rigth = self.height(root.rigth) 
        if left > rigth:
            return left + 1
        else:
            return rigth + 1

    def get(self, node, stack):
        stack.push(node.data)
        if node.left:
            self.get(node.left, stack)
        if node.rigth:
            self.get(node.rigth, stack)
        

tree1 = BinaryTree()
tree2 = BinaryTree()
stack1 = Stack()
stack2 = Stack()

def show(stack):
    text = ""
    for index in range(stack.size()):
        data = stack.top(index)
        text = text + str(data) + " "
    return text


def addTree(data, tree):
    number = ""
    for char in data:
        if char == " ":
            tree.add(number)
            number = ""
        else:
            number = number + char

def verification(stackTree1, stackTree2):
    if stackTree1 == stackTree2:
        print("true")
    elif stackTree1 != stackTree2:
        print("false")


if __name__ == "__main__":
    data1 = ""
    data2 = ""
    for index in range(2):
        string = input() + " "
        if index == 0:
            data1 = string
        elif index == 1:
            data2 = string

    addTree(data1, tree1)
    addTree(data2, tree2)

    tree1.get(tree1.root, stack1)
    tree2.get(tree2.root, stack2)

    stackTree1 = show(stack1)
    stackTree2 = show(stack2)

    verification(stackTree1, stackTree2)
