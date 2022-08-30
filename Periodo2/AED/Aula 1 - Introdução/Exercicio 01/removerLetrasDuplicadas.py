def analisar(s, tamanho, tamanhoInicial):
    if tamanho == (tamanhoInicial - (tamanhoInicial-1)):
        print(s)
    else:
        selecionada = s[tamanhoInicial-tamanho]
        quantidade = s.count(selecionada)
        if quantidade > 1:
            removerString = s.replace(selecionada, " ")
            auxiliar = removerString[:tamanhoInicial-tamanho]+removerString[tamanhoInicial-tamanho].replace(" ", selecionada)+removerString[tamanhoInicial-tamanho:]
            novaString = auxiliar.replace(" ", "")
            return analisar(novaString, tamanho-1, len(novaString))
        else:
            return analisar(s, tamanho-1, tamanhoInicial)


s = input("")
tamanhoInicial = len(s)
analisar(s, len(s), tamanhoInicial)