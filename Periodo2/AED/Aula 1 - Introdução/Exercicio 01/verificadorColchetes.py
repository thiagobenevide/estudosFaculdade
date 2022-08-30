colcheteEsquerdo = []
colcheteDireito = []

def percorrerString(string, tamanho, tamanhoInicial):
    if tamanho == 0:
        return 
    else:
        caractere = string[tamanhoInicial-tamanho]
        if caractere == "[":
            colcheteEsquerdo.append(caractere)
            return percorrerString(string, tamanho-1, tamanhoInicial)
        elif caractere == "]":
            colcheteDireito.append(caractere)
            return percorrerString(string, tamanho-1, tamanhoInicial)
        else:
            return percorrerString(string, tamanho-1, tamanhoInicial)
            


def verificacao(colcheteEsquerdo, colcheteDireito):
    if len(colcheteEsquerdo) + len(colcheteDireito) == 0:
        print("Nao possui parenteses")
    elif len(colcheteEsquerdo) == len(colcheteDireito):
        return 1
    elif len(colcheteEsquerdo) != len(colcheteDireito):
        return 0


string = input("")
tamanhoInicial = len(string)

percorrerString(string, len(string), tamanhoInicial)
print(verificacao(colcheteEsquerdo, colcheteDireito))

