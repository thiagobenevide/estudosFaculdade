#Tabela hash com endereçamento fechado

"Importe a lista"


class TabelaHash():
    def __init__(self, n):
        self.listas = [Lista() for i in range(n)]
        self.n = n

    def add(self, valor):
        chave = hash(valor)
        posicao = chave % self.n
        self.listas[posicao].adicionar(valor)
    
    def hash(self, valor):
        if type(valor) == str:
            return ord(valor[0])
        else:
            return hash(valor)

    def busca(self, valor):
        chave = self.hash(valor)
        posicao = chave % self.n
        lista = self.listas[posicao]
        aux = lista.inicio
        while(aux != None):
            if aux.info == valor:
                return True
            aux = aux.prox
        return False

    def imprimir_tabela(self):
        pass

    def remove(self):
        pass


if __name__ == '__main__':
    tabela_hash = TabelaHash(5)
    tabela_hash.add(20)
    tabela_hash.add(18)
    tabela_hash.add(25)

    tabela_hash.listas[0].inicio.valor.info