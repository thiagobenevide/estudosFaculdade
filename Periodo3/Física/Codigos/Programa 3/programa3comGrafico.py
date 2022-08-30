
from math import radians, cos,sin,tan
import PySimpleGUI as sg
from matplotlib import pyplot as plt

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
        [sg.Text(size=(20,1)),sg.Button('Visualizar Gráfico',key="grafico", size=(15,1))]
    ]
    return sg.Window("App - Resposta", layout=layoutTelaResposta, finalize=True)

    
janela1, janela2 = telaEntradaDados(), None

while True:
    window, event, values = sg.read_all_windows()
    
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    
    if window == janela2 and event == sg.WIN_CLOSED:
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
        
        #Parte1 - Valores Iniciais
        vTetaY = v0*sin(angulo)
        vTetaX = v0*cos(angulo)

        #Parte2 - Tempo
        tSubida = vTetaY/gravidade
        tVoo = 2*tSubida

        #Parte3 - Altura    
        alturaMax = (y0 + (vTetaY*tSubida)) - ((gravidade*(tSubida**2))/2)
    
        #Parte4 - Alcance
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
            
            #Parte 5 - Formula e varificação ponto a ponto
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
        plt.ylabel('y', fontsize=9)
        plt.plot(listaPontosX, listaPontosY, marker='o')
        plt.show()
        
        
        