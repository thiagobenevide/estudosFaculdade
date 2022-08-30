import PySimpleGUI as sg
from matplotlib import pyplot as plt

def tela_inicial():
    sg.theme("Black")
    layout_tela_1 = [
        [sg.Text("Posição inicial: ", size=(14, 1)), sg.Input(key="x0", size=(10, 1))],
        [sg.Text("Velocidade inicial: ", size=(14, 1)), sg.Input(key="v0", size=(10, 1))],
        [sg.Text("Acelereção: ", size=(14, 1)), sg.Input(key="a", size=(10, 1))],
        [sg.Text("Tempo: ", size=(14, 1)), sg.Input(key="t", size=(10, 1))],
        [sg.Button("Gráfico da aceleração", key="g1", size=(24, 1))],
        [sg.Button("Gráfico da velocidade", key="g2", size=(24, 1))],
        [sg.Button("Gráfico da posição", key="g3", size=(24, 1))]
    ]
    return sg.Window("Gráficos", layout=layout_tela_1, finalize=True)

#Criando janela
janela = tela_inicial()

#Criando o loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()

    tempo = [0, values["t"]]

#Tratamento da tela inicial -----------------------------------
    if window == janela and event == sg.WIN_CLOSED:
        break

    if window == janela and event == "g1":
        aceleracao = [values["a"], values["a"]]
        
        plt.plot(tempo, aceleracao)
        plt.title("Gráfico da Aceleração",fontsize=16, fontweight='bold')
        plt.xlabel("Valores do Tempo em Segundos (eixo x)", fontsize=9)
        plt.ylabel("Valores da Posição em Metros (eixo y)", fontsize=9)
        plt.plot(tempo, aceleracao, marker='o')
        plt.show()

    elif window == janela and event == "g2":
        v =  int(values["v0"]) + (int(values["a"])*int(values["t"]))
        
        velocidade = [0, v]

        plt.plot(tempo, velocidade)
        plt.title("Gráfico da Velocidade",fontsize=16, fontweight='bold')
        plt.xlabel("Valores do Tempo em Segundos (eixo x)", fontsize=9)
        plt.ylabel("Valores da Posição em Metros (eixo y)", fontsize=9)
        plt.plot(tempo, velocidade, marker='o')
        plt.show()

    elif window == janela and event == "g3":
        x = int(values["x0"]) - (int(values["v0"])*int(values["t"])) + (0.5*int(values["a"])*(int(values["t"])**2))
        
        posicao = [values["x0"], x]

        plt.plot(tempo, posicao)
        plt.title("Gráfico da Posição",fontsize=16, fontweight='bold')
        plt.xlabel("Valores do Tempo em Segundos (eixo x)", fontsize=9)
        plt.ylabel("Valores da Posição em Metros (eixo y)", fontsize=9)
        plt.plot(tempo, posicao, marker='o')
        plt.show()