from curses.ascii import isdigit
import PySimpleGUI as sg

def telaEntradaDados():
    sg.theme("Defaut")

    layoutTelaEntradaDados = [
        [sg.Text("Ângulo: ", size=(15,1)), sg.Input(key="angulo", size=(9,1))],
        [sg.Text("Gravidade: ", size=(15,1)), sg.Input(key="gravidade",size=(9,1))],
        [sg.Text("Velocidade Inicial: ", size=(15,1)), sg.Input(key="v0",size=(9,1))],
        [sg.Text("Divisor: ", size=(15,1)), sg.Input(key="divisor",size=(9,1))],
        [sg.Text("Posição X inicial: ", size=(15,1)), sg.Input(key="x0",size=(9,1))],
        [sg.Text("Posição Y inicial:", size=(15,1)),sg.Input(key="y0",size=(9,1))],
        [sg.Text(size=(5,1)),sg.Button('Calcular',key="calcular", size=(9,1))]
    ]
    
    return sg.Window("Projeto", layout=layoutTelaEntradaDados, finalize=True)

def telaErroEntrada():
    sg.theme("Black")

    layoutTelaErroEntrada = [
        [sg.Text("Erro! Vocẽ não digitou números,\nportanto, ou as caixas então vazias \nou a há letras nas caixas.",size=(30,3))],
        [sg.Text(size=(6,1)),sg.Button("Tentar Novamente", key="tentarNovamente", size=(10,2))]
    ]
    
    return sg.Window("Erro!", layout=layoutTelaErroEntrada, finalize=True)

janela1, janela2  = telaEntradaDados(), None

while True:
    window, event, values = sg.read_all_windows()
    
    #Tratamento da tela entrada de dados
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    def continuarPrograma():
        pass

    def erroEntrada(janela2):
        janela1.hide()
        janela2 = telaErroEntrada()
        while True:
            window2, event2, values2 = sg.read_all_windows()
            if window2 == janela2 and event2 == sg.WIN_CLOSED:
                break
            
            if window2 == janela2 and event2 == "tentarNovamente":
                janela2.hide()
                janela1.un_hide()
                return

    
    
    # Verificar se um dado é um número ou um alfanum
    def verificarDado(dado):
        if dado.isdigit():
            return True
        else:
            return False
        
    #Verifica se há erro na entrada de dados ou não
    def verificacaoGeral(entrada):
        if entrada is True:
            continuarPrograma()
        else:
            erroEntrada(janela2)
        
            
    if window == janela1 and event == "calcular":        
        entradaCerta = verificarDado(values["angulo"])
        verificacaoGeral(entradaCerta)
        entradaCerta = verificarDado(values["gravidade"])
        verificacaoGeral(entradaCerta)
        entradaCerta = verificarDado(values["v0"])
        verificacaoGeral(entradaCerta)
        entradaCerta = verificarDado(values["divisor"])
        verificacaoGeral(entradaCerta)
        entradaCerta = verificarDado(values["x0"])
        verificacaoGeral(entradaCerta)
        entradaCerta = verificarDado(values["y0"])
        verificacaoGeral(entradaCerta)
        
    #TELA 2-----------------------------
    