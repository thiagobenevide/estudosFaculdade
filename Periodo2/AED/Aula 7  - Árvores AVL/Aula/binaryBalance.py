class NodeAVL():
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
        self.height = 0


class TreeAVL():
    def __init__(self):
        self.root = None

    def bigger(self, heigth1, heigth2):
        """_Descobre e retorna qual é o maior valor entre duas alturas de subárvores_

        Args:
            heigth1 (_int_): _Altura da primeira subárvore_
            heigth2 (_type_): _Altura da segunda subárvore_

        Returns:
            _int_: _Valor da maior altura_
        """
        if heigth1 > heigth2:
            return heigth1
        else:
            return heigth2

    def heigthNode(self, node):
        """_Retorna a altura do nó_

        Args:
            node (_NodeAVL_): _Um nó qualquer de uma ávore AVL_

        Returns:
            _int_: _Retorna -1 caso o nó não exista, caso exista retorna o valor de uma altura_
        """
        if node == None:
            return -1
        else:
            return node.height

    def balancingFator(self, node):
        """_Retorna o fator de banceamento de um determinado no de acordo com sua altura_

        Args:
            node (_NodeAVL_): _Nó de uma subárvore_

        Returns:
            _int_: _Retorna 0 ou a diferença da altura do no a esqueda menos a altura do nó a direita_
        """
        if node:
            return self.heigthNode(node.left) - self.heigthNode(node.right)
        else:
            return 0

    def leftRotation(self, nodeR):
        """_Rotação simples a esquerda_

        Args:
            nodeR (_NodeAVL_): _Nó que está desbalanceado e precisa ser balanceado com uma rotação a esquerda_

        Returns:
            _NodeAVL_: _Retorna o nó subárvore laterado e balanceado_
        """

        nodeY = nodeR.right
        nodeF = nodeY.right

        nodeR.right = None
        nodeY.left = nodeR

        nodeR.height = (self.bigger(self.heigthNode(nodeR.left), self.heigthNode(nodeR.right)) + 1)
        nodeY.height = (self.bigger(self.heigthNode(nodeY.left), self.heigthNode(nodeY.right)) + 1)

        return nodeY

    def rigthRotation(self, nodeR):
        """_Rotação simples a direita_

        Args:
            nodeR (_NodeAVL_): _Nó que está desbalanceado e precisa ser balanceado com uma rotação a direita_

        Returns:
            _NodeAVL_: _Nó alterado e balanceado com a rotação a direita_
        """
        nodeY = nodeR.left
        nodeF = nodeY.left

        nodeR.left = None
        nodeY.right = nodeR

        nodeR.height = (self.bigger(self.heigthNode(nodeR.left), self.heigthNode(nodeR.right)) + 1)
        nodeY.height = (self.bigger(self.heigthNode(nodeY.left), self.heigthNode(nodeY.right)) + 1)

        return nodeY

    def doubleRotationRigthLeft(self, nodeR):
        """_Rotação dupla, direita e esquerda_

        Args:
            nodeR (_NodeAVL_): _Ná de uma subárvore desbalanceada_

        Returns:
            _NodeAVL_: _Retorna uma rotação a esquerda_
        """
        nodeR.right = self.rigthRotation(nodeR.right)
        return self.leftRotation(nodeR)

    def doubleRotationLeftRigth(self, nodeR):
        """_Rotação dupla, direita e esquerda_

        Args:
            nodeR (_NodeAVL_): _Ná de uma subárvore desbalanceada_
            nodeR.right (_NodeAVL_): _Recebe uma rotação a esquerda_

        Returns:
            _NodeAVL_: _Retorna uma rotação a direita_
        """
        nodeR.left = self.leftRotation(nodeR.left)
        return self.rigthRotation(nodeR)

    def balance(self, root):
        """_Balanceamento da árvore_

        Args:
            root (_NodeAVL_): _Raiz da árvore a ser balanceada_

        Variables:
            balaFator (_int_): _Fator de balanceamento da raiz da subárvore ou raiz geral_

        Returns:
            _NodeAVL_: _Retorna a nova raiz agora balanceada_
        """
        balaFator = self.balancingFator(root)

        # Rotation Left
        if balaFator < -1 and self.balancingFator(root.right) <= 0:
            root = self.leftRotation(root)
        # Rotation Rigth
        elif balaFator > 1 and self.balancingFator(root.left) >= 0:
            root = self.rigthRotation(root)
        # Rotation Left and Rigth
        elif balaFator > 1 and self.balancingFator(root.left) < 0:
            root = self.doubleRotationLeftRigth(root)
        # Rotation Rigth and Left
        elif balaFator < -1 and self.balancingFator(root.right) > 0:
            root = self.doubleRotationRigthLeft(root)

        return root

    def newNode(self, data):
        """
        Cria novo nó com a classe NodeAVL
        :param data: dado do novo nó
        :return: retorna a variável noden
        """
        noden = NodeAVL(data)
        return noden

    def insert(self, data, root, num=1):
        """

        :param data: valor inteiro que deseja inserir
        :param root: raiz da árvore
        :param num: contador de recursões
        :return: retorna a raiz
        """

        if root is None and num == 1:
            node = NodeAVL(data)
            self.root = node
            return
        elif root is None and num != 1:
            return self.newNode(data)
        else:
            if data < root.data:
                root.left = self.insert(data, root.left, num + 1)
            elif data > root.data:
                root.right = self.insert(data, root.right, num + 1)

        root.height = self.bigger(self.heigthNode(root.left), self.heigthNode(root.right)) + 1

        self.root = self.balance(root)


        return root

    def impress(self, root):
        if root:
            self.impress(root.left)
            print(f"Valor -> {root.data}")
            self.impress(root.right)

if __name__ == "__main__":
    treeAVL = TreeAVL()

    string = input() + " "
    number = ""
    for char in string:
        if char == " ":
            num = int(number)
            treeAVL.insert(number, treeAVL.root)
            number = ""
        else:
            number = number + char

        treeAVL.impress(treeAVL.root)


    print(f"Esquerda {treeAVL.root.left.data}")
    print(f"Raiz {treeAVL.root.data}")
    print(f"Direita {treeAVL.root.right.data}")
    print(f"Esquerda de 45 -> {treeAVL.root.right.left.data}")
    print(f"Esquerda de 9 -> {treeAVL.root.left.left.data}")
    print(f"Direita de 9 -> {treeAVL.root.left.right.data}")

