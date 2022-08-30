import PySimpleGUI as sg
import calcularDados

forcaResultanteX = []
forcaResultanteY = []
forcaResultanteZ = []

def criar_janela_inicial():
    sg.theme('Reddit')
    linha = [
        [sg.Text('0 - Ângulo:'),sg.Input('',size=(15,1), key=0),sg.Text('0 - Força:'),sg.Input('',size=(15,1), key=1), sg.Text('Digite a massa: '), sg.Input('',size=(15,1), key='massa')]
    ]

    layout = [
        [sg.Frame('Tarefas', layout=linha,key='container')],
        [sg.Button('Adicionar'),sg.Button('Reiniciar'), sg.Button('Calcular')]

    ]
    return sg.Window('Programa 4 - Física', layout=layout, finalize=True)

def janelaResposta():
    sg.theme('Reddit')

    layout = [
        [sg.Text('', key="respostaAceleracao")],
        [sg.Text('', key="respostaResultanteX")],
        [sg.Text('', key="respostaResultanteY")],
        [sg.Text('', key="respostaResultanteZ")],
        [sg.Button('Reiniciar')]
    ]

    return sg.Window('Tela Resposta', layout=layout, finalize=True)

def criarLinha(janela, contador):
    janela.extend_layout(janela['container'], [[sg.Text(f'{contador-1} - Ângulo:'), sg.Input('',size=(15,1),key=contador),sg.Text(f'{contador-1} - Forca:'),sg.Input('',size=(15,1), key=contador+1)]])
    
#Retorno de Dados

def retornarForca(values, contador):
    return float(values[contador+1])

def retornarAngulo(values, contador):
    return float(values[contador])

def retornaListaResultanteX():
    return forcaResultanteX

def retornarListaResultanteY():
    return forcaResultanteY

def retornarListaResultanteZ():
    return forcaResultanteZ

def getResultanteGeralN(listaResultanteN):
    return calcularDados.resultanteN(listaResultanteN)


#Funções para chamar calculos

def calcularForcas(values, contador):
    angulo = retornarAngulo(values, contador)
    forca = retornarForca(values, contador)

    forcaX = float(calcularDados.forcaNx(forca, angulo))
    forcaY = float(calcularDados.forcaNy(forca, angulo))
    forcaZ = float(calcularDados.forcaNz(forca, angulo))
    
    forcaResultanteX.append(forcaX)
    forcaResultanteY.append(forcaY)
    forcaResultanteZ.append(forcaZ)

def calcularResultantes():
    resultanteX = float(calcularDados.resultanteN(forcaResultanteX))
    resultanteY = float(calcularDados.resultanteN(forcaResultanteY))

    valorResultanteGeral = calcularDados.resultanteGeral(resultanteX, resultanteY)

    return valorResultanteGeral

