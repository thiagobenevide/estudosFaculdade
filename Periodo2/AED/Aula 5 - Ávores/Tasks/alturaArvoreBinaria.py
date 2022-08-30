class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rigth = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
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
        else:
            if data <= self.root.data:
                self.insertLeft(self.root, node)
            else:
                self.insertRight(self.root, node)

    def show(self, node=None):
        if node == None:
            node = self.root
        print(node.data, end=" ")
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
        

tree = BinaryTree()
number = ""

data = input()+" "
for char in data:
    if char == " ":
        tree.add(int(number))
        number = ""
    else:
        number += char
        
print(int(tree.height(tree.root)))