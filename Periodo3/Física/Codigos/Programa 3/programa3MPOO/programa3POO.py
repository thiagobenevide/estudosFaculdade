from math import radians, cos,sin,tan
import PySimpleGUI as sg
from matplotlib import pyplot as plt

class TelaInicial:
    def telaEntradaDados(self):
        sg.theme("Reddit")
        layoutTelaEntradaDados=[
            [sg.Text("Ângulo: ", size=(15,1)), sg.Input(key="angulo", size=(9,1))],
            [sg.Text("Gravidade: ", size=(15,1)), sg.Input(key="gravidade",size=(9,1))],
            [sg.Text("Velocidade Inicial: ", size=(15,1)), sg.Input(key="v0",size=(9,1))],
            [sg.Text("Divisor: ", size=(15,1)), sg.Input(key="divisor",size=(9,1))],
            [sg.Text("Posição X inicial: ", size=(15,1)), sg.Input(key="x0",size=(9,1))],
            [sg.Text("Posição Y inicial:", size=(15,1)),sg.Input(key="y0",size=(9,1))],
            [sg.Text(size=(5,1)),sg.Button('Calcular',key="calcular", size=(9,1))]
            
        ]
        return sg.Window("App - Entrada", layout=layoutTelaEntradaDados, finalize=True)

class TelaResposta:    
    def telaResposta(self):
        sg.theme("Reddit")
        layoutTelaResposta=[
            [sg.Text("", key="tSubida", size=(60,1))],
            [sg.Text("", key="tVoo", size=(60,1))],
            [sg.Text("", key="alturaMax", size=(60,))],
            [sg.Text("", key="alcanceX", size=(60,1))],
            [sg.Text(size=(20,1)),sg.Button('Visualizar Gráfico',key="grafico", size=(15,1))]
        ]
        return sg.Window("App - Resposta", layout=layoutTelaResposta, finalize=True)

