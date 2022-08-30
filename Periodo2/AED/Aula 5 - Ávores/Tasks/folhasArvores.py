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

    def sheets(self, root):
        if root == None:
            return 0
        elif root.left == None and root.rigth == None:
            return 1
        else:
            return self.sheets(root.left) + self.sheets(root.rigth)

if __name__ == "__main__":
    tree = BinaryTree()

    string = input() + " "
    data = ""
    for char in string:
        if char == " ":
            tree.add(data)
            data = ""
        else:
            data = data + char

    sheets = tree.sheets(tree.root)
    print(sheets)
