from math import radians, cos,sin,tan


#Calcular todas as resultantes X
def forcaNx(entradaForca, entradaAngulo):
    forca = float(entradaForca*cos(radians(float(entradaAngulo))))
    return forca

def forcaNy(entradaForca, entradaAngulo):
    forca = float(entradaForca*sin(radians(float(entradaAngulo))))
    return forca

def forcaNz(entradaForca, entradaAngulo):
    forca = float(entradaForca*tan(radians(float(entradaAngulo))))
    return forca

#Calcular todas as resultantes Y
def resultanteN(todasForcaN):
    fResultanteAux = 0
    for forca in range(len(todasForcaN)):
        fResultanteAux = fResultanteAux+todasForcaN[forca]
    return fResultanteAux

#Calcular Resultante Geral
def resultanteGeral(resultanteX, resultanteY):
    forcaResultante = (resultanteX)+(resultanteY)
    return forcaResultante

#Calculo da Força Resultante
def calculoAceleracao(forcaResultante, massa):
    acelecaoCorpo = forcaResultante/massa
    return acelecaoCorpo


