class Node():
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.height = 0
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """_Insere novos elementos a árvore AVL_

        Args:
            value (_int_): _elemento a ser inserido_
        """
        element = Node(value)
        if self.root == None:
            self.root = element
        else:
            self.__insert(value, self.root)
    
    def __insert(self, value, node):
        """_Inserir o valor de acordo com o lado esquerdo ou direito_

        Args:
            value (_int_): _Novo valor a ser inserido na árvore AVL_
            node (_Node_): _Nó para ser manipulado_
        """
        if value < node.data:
            if node.left:
                self.__insert(value, node.left)
            else:
                node.left = Node(value, node)
                self.__violationHandler(node.left)
        if value > node.data:
            if node.right:
                self.__insert(value, node.right)
                self.__violationHandler(node.right)
    
    def __violationHandler(self, node):
        """_É verificado os nós da árvore_

        Args:
            node (_Node_): _Nó a direita ou esquerda do método __insert_
        """
        while node:
            node.height = max(self.__height_nodes(node.left), self.__height_nodes(node.right)) + 1
            self.__violationHandlerFix(node)
            node = node.parent
            
    def __violationHandlerFix(self, node):
        pass

    def __height_nodes(self, node):
        """_Mostra a altura do nó para o fator de balanceamento_

        Args:
            node (_Node_): _Nó raiz ou de uma subárvore para ser analisado sua altura_

        Returns:
            _int_: _Retorna a altura do nó que pode ser -1,0,1 ..._
        """
        if not node:
            return -1
        return node.height
    
    def __balanceFactor(self, node):
        """_Mostra o fator principal da árvore avl o fator que gera a necessidade de um balanceamento_

        Args:
            node (_Node_): _Nó analisado para ser feito um balanceamento ou não_

        Returns:
            _int_: _Valor do fator de balanceamento feito de acordo com as alturas_
        """
        if not node:
            return 0
        return self.__height_nodes(node.left)-self.__height_nodes(node.right)

    def __rotateLeft(self,node):
        temporaryNodeRight = node.right
        temporaryNodeLeft = node
        temporaryParent = node.parent

        t = node.right.left
        node.right = t
        
        temporaryNodeRight.parent = temporaryParent
        node.parent = temporaryNodeRight


    def __rotateRight(self, node):
        pass


    def remove():
        pass

    def height():
        pass
