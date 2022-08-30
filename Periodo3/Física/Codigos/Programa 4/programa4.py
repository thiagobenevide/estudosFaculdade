from math import radians, cos,sin,tan
import PySimpleGUI as sg

def criar_janela_inicial():
    sg.theme('Reddit')
    linha = [
        [sg.Text('0 - Ângulo:'),sg.Input(''),sg.Text('0 - Força:'),sg.Input('')]
    ]

    layout = [
        [sg.Frame('Tarefas', layout=linha,key='container')],
        [sg.Button('Adicionar'),sg.Button('Reiniciar')]

    ]
    return sg.Window('To do List', layout=layout, finalize=True)

janela = criar_janela_inicial()
contador = 0

while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Adicionar':
        contador+=1
        janela.extend_layout(janela['container'], [[sg.Text(f'{contador} - Ângulo:'), sg.Input(''),sg.Text(f'{contador} - Forca:'),sg.Input('')]])
    
    if event == 'Reiniciar':
        contador = 0
        janela.close()
        janela = criar_janela_inicial()

