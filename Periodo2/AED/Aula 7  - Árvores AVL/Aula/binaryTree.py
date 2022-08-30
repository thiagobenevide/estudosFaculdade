from xml.dom.minidom import Element


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
            #print("\033Adicionado a esquerda")
        else:
            if dataNode.data <= rootNode.left.data:
                self.insertLeft(rootNode.left, dataNode)
            else:
                self.insertRight(rootNode.left, dataNode)

    def insertRight(self, rootNode, dataNode):
        if rootNode.rigth == None:
            rootNode.rigth = dataNode
            #print(f"\033[1;36mAdicionado a Direita")
        else:
            if dataNode.data > rootNode.rigth.data:
                self.insertRight(rootNode.rigth, dataNode)
            else:
                self.insertLeft(rootNode.rigth, dataNode)
        
    def insert(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
            #print("\033[1;31mRaiz Criada")
        else:
            if data <= self.root.data:
                self.insertLeft(self.root, node)
            else:
                self.insertRight(self.root, node)

    def remove(self, root, element):
        if root == None:
            return None
        else:
            if root.data == element:
                #Remove nos folhas
                if root.left == None and root.rigth == None:
                    root = None
                    return None
                    
                else: #Remove nos que possuem apenas 1 filho
                    if root.left == None or root.rigth == None:
                        assistant = 0
                        TreeNode(assistant)
                        if root.left != None:
                            assistant = root.left
                        else:
                            assistant = root.rigth
                        root = None
                        return assistant
                    else:
                        assistant = TreeNode(root.left)
                        while assistant.rigth != None:
                            assistant = assistant.rigth
                        root.data = assistant.data
                        assistant.data = element
                        root.left = self.remove(root.left, element)
                        return root.data

            else: #Prorcura os valores dos nós
                if element < root.data:
                    root.left = self.remove(root.left, element)
                else:
                    root.rigth = self.remove(root.rigth, element)
                return root

    def show(self, node=None):
        if node == None:
            node = self.root
        print(node.data, end=" ")
        if node.rigth:
            self.show(node.rigth)
        if node.left:
            self.show(node.left)

    def sheets(self, root):
        if root == None:
            return 0
        elif root.left == None and root.rigth == None:
            return 1
        else:
            return self.sheets(root.left) + self.sheets(root.rigth)

    def height(self, root):
        if root == None:
            return -1
        left = self.height(root.left)   
        rigth = self.height(root.rigth) 
        if left > rigth:
            return left + 1
        else:
            return rigth + 1

    def search(self, root, key):
        if root == None:
            return -1
        else:
            if root.data == key:
                return root.data
            else:
                if key < root.data:
                    return self.search(root.left, key)
                else:
                    return self.search(root.rigth, key)


if __name__ == "__main__":
    tree = BinaryTree()

    for i in range(3):
        data = int(input(f"Digite o elemento {i+1}: "))
        tree.insert(data)

    elem = int(input("Digite o número a ser pesquisado: "))

    verfic = tree.search(tree.root, elem)    
    print(verfic)


