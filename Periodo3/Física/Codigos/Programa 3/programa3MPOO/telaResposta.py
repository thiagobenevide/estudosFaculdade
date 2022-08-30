from math import radians, cos,sin,tan
import PySimpleGUI as sg
from matplotlib import pyplot as plt

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

    def telaGrafico(self, x,y):
        