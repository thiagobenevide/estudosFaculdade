import PySimpleGUI as sg
from matplotlib import pyplot as plt

def tela_app():
    sg.theme("Black")
    layout_tela_vm = [
            [sg.Text("Tempo 1: ", size=(8, 1)), sg.Input(key="t1", size=(15, 1)), sg.Text("Posição 1: ", size=(9, 1)), sg.Input(key="p1", size=(15, 1))],

            [sg.Text("Tempo 2: ", size=(8, 1)), sg.Input(key="t2", size=(15, 1)), sg.Text("Posição 2: ", size=(9, 1)), sg.Input(key="p2", size=(15, 1))],

            [sg.Text("Tempo 3: ", size=(8, 1)), sg.Input(key="t3", size=(15, 1)), sg.Text("Posição 3: ", size=(9, 1)), sg.Input(key="p3", size=(15, 1))],

            [sg.Text("Unidade de Medida: "), sg.Radio("m/s", "radio", default=True, key="verificar"), sg.Radio("km/h", "radio")],

            [sg.Text("")], #Apenas para dar um espaçamento entre os botoes e as caixas de texto

            [sg.Text("", size=(16, 2)), sg.Button("Calcular", key = "calcular", size=(10, 2))]
	]
    return sg.Window("App - Valores", layout = layout_tela_vm, finalize=True)

def tela_resposta():
    sg.theme("Black")
    layout_tela_resposta = [
        [sg.Text("", key="resposta_vm")],
        [sg.Text("", key="resposta_vem")],
        [sg.Text("")],
        [sg.Button("Visualizar Gráfico", key = "grafico", size=(10, 2)), sg.Text("", size=(10, 2)), sg.Button("Voltar", key = "voltar", size=(10, 2))]
    ]
    return sg.Window("App - Resposta", layout = layout_tela_resposta, finalize=True)
    
#Criar Janelas
janela1, janela2, janela3= tela_app(), None, None

#Criar o loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    erro_na_entrada = False
    
#Tratamento da tela inicial --------------------------------------
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == "calcular":
        janela1.hide()
        janela2 = tela_resposta()

        p1 = float(values["p1"])
        p2 = float(values["p2"])
        p3 = float(values["p3"])
        t1 = float(values["t1"])
        t2 = float(values["t2"])
        t3 = float(values["t3"])
        
        janela2 = tela_resposta()

        #print(p1,p2,p3,t1,t2,t3)
        if t3-t1 == 0:
            break

        velocidade_media = (p3 - p1)/(t3 - t1)

        velocidade_escalar_media = abs(p1 + p2 + p3)/(t3 - t1)

        if values["verificar"] == True:
            resposta = "m/s"
        else:
            velocidade_escalar_media = velocidade_escalar_media*3.6
            velocidade_media = velocidade_media *3.6
            resposta = "km/h"

        janela2["resposta_vm"].update(f"A velocidade média atingida foi de {velocidade_media:.2f} {str(resposta)}")
        janela2["resposta_vem"].update(f"A velocidade escalar média atingida foi de {velocidade_escalar_media:.2f} {resposta}")
        
#Tratamento da tela de resposta ----------------------------------

    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela2 and event == "voltar":
        janela2.hide()
        janela1.un_hide()
    
    if window == janela2 and event == "grafico":
        tempo = [t1, t2, t3]
        posicao = [p1, p2, p3]
        plt.style.use('ggplot')
        plt.title('Gráfico do Tempo e Posição',fontsize=16, fontweight='bold')
        plt.xlabel('Tempo (segundos)', fontsize=9)
        plt.ylabel(f'Posição (metros)', fontsize=9)
        plt.plot(tempo, posicao, marker='o')
        plt.show()
    
