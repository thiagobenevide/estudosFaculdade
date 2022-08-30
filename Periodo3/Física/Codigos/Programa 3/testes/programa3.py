import PySimpleGUI as sg

def telaEntradaDados():
    sg.theme("Default")
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
    sg.theme("Default")
    layoutTelaResposta=[
        [sg.Text("Resposta1", key="tMaximo", size=(40,1))],
        [sg.Text("Resposta2", key="tVoo", size=(40,1))],
        [sg.Text("Resposta3", key="hMax", size=(40,1))],
        [sg.Text("Resposta4", key="alcance", size=(40,1))],
    ]
    return sg.Window("App - Resposta", layout=layoutTelaResposta, finalize=True)

def telaRespostaFormula():
    sg.theme("Default")
    layoutTelaRespostaFormula=[
        [sg.Text("Resposta1", key="tMaximoFor", size=(40,1))],
        [sg.Text("Resposta2", key="tVooFor", size=(40,1))],
        [sg.Text("Resposta3", key="hMaxFor", size=(40,1))],
        [sg.Text("Resposta4", key="alcanceFor", size=(40,1))],
    ]
    return sg.Window("App - Resposta Formula", layout=layoutTelaRespostaFormula, finalize=True)

    
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
        janela3 = telaRespostaFormula()
        