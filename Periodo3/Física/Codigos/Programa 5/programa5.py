from cmath import pi
from math import radians, cos,sin,tan
from turtle import color
import PySimpleGUI as sg
from matplotlib import pyplot as plt
from vpython import *

def telaEntradaDados():
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

def telaResposta():
    sg.theme("Reddit")
    layoutTelaResposta=[
        [sg.Text("", key="tSubida", size=(60,1))],
        [sg.Text("", key="tVoo", size=(60,1))],
        [sg.Text("", key="alturaMax", size=(60,))],
        [sg.Text("", key="alcanceX", size=(60,1))],
        [sg.Button('Visualizar Gráfico',key="grafico", size=(15,1)),  sg.Button('Visualizar simulação',key="simulacao", size=(15,1))]
    ]
    return sg.Window("App - Resposta", layout=layoutTelaResposta, finalize=True)

    
janela1, janela2, janela3 = telaEntradaDados(), None, None

while True:
    window, event, values = sg.read_all_windows()
    
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    
    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela3 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == "calcular":

        janela1.hide()
        janela2 = telaResposta()
        
        #Entrada de Dados
        gravidade = float(values["gravidade"])
        v0 = int(values["v0"])
        x0 = int(values["x0"])
        y0 = int(values["y0"])
        divisor = int(values["divisor"])
        angulo = radians(float(values["angulo"]))
        
        #Parte1    
        vTetaY = v0*sin(angulo)
        vTetaX = v0*cos(angulo)

        #Parte2
        tSubida = vTetaY/gravidade
        tVoo = 2*tSubida

        #Parte3    
        alturaMax = (y0 + (vTetaY*tSubida)) - ((gravidade*(tSubida**2))/2)
    
        #Parte4
        alcanceR = x0 + (vTetaX*tVoo)

        janela2["tSubida"].update(f"O tempo para alcançar a altura máxima é {tSubida:.2f} segundos")
        janela2["tVoo"].update(f"O tempo total de voo é {tVoo:.2f} segundos")
        janela2["alturaMax"].update(f"A altura máxima é {alturaMax:.2f} metros")
        janela2["alcanceX"].update(f"O alcance R é {alcanceR:.2f} metros")
        
    listaPontosY = [y0]
    listaPontosX = [x0]
    
    
    if window == janela2 and event == "grafico":
        parcela = alcanceR/divisor
        contadorParcela = parcela
        
        for contador in range(divisor):
            pontoy = ((tan(angulo))*contadorParcela) - (((gravidade*(contadorParcela**2))/(2*((v0*cos(angulo))**2))))
            
            pontoy = pontoy+y0
            pontox = contadorParcela+x0
            
            listaPontosY.append(pontoy)
            listaPontosX.append(pontox)
            
            contadorParcela = contadorParcela + parcela
            
            
        
        print(listaPontosY)
        print(listaPontosX)
            
        plt.style.use('ggplot')
        plt.title('Gráfico',fontsize=16, fontweight='bold')
        plt.xlabel('x', fontsize=9)
        plt.ylabel(f'y', fontsize=9)
        plt.plot(listaPontosX, listaPontosY, marker='o')
        plt.show()
        
    if window == janela2 and event == "simulacao":

        #antes de rodar ir no terminal e colocar  pip3 install vpython --upgrade

        #OBJETOS

        bola = sphere(pos=vec(0,1,0), radius=1, color=color.red, make_trail = True)
        solo = box(pos=vec(0,0,0),  size=vec(2*alcanceR,0.5,5), color=color.white)

        #CONDIÇÕES INICIAIS

        theta = angulo*(pi/180)
        g = vec(0,-gravidade, 0)
        bola.v = vec(v0*cos(angulo), v0*sin(angulo), 0)
        t = 0
        dt = 0.001

        #LEGENDA
        legendaAlcance = label(pos=vec(0,15,0), text="Alcance")

        #EQUAÇÕES

        while bola.pos.y >= 1:
            rate(500)
            bola.v = bola.v + g*dt
            bola.pos = bola.pos + bola.v*dt
            t = t+dt

            legendaAlcance.text = "Alcance = {:0.2f}".format(bola.pos.x)