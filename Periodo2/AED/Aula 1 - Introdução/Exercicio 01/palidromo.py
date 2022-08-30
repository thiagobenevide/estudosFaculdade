def inverterPalavra(palavra, tamanho):
    if tamanho == 1:
        return palavra[0]
    else:
        return palavra[tamanho-1] + inverterPalavra(palavra, tamanho-1)

def checarPalindromo(palavraInvertida, validarPalavra):
    if palavraInvertida == validarPalavra:
        return True
    elif palavraInvertida != validarPalavra:
        return False


s = str(input("Digite uma palavra: ")).strip().upper()
validarPalavra = ''.join(filter(str.isalnum, s))
palavraInvertida = inverterPalavra(validarPalavra, len(validarPalavra))

checarPalindromo(palavraInvertida, validarPalavra)






