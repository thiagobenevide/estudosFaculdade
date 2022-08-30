import PySimpleGUI as sg
import janelaInicial
import calcularDados

janela1, janela2 = janelaInicial.criar_janela_inicial(), None
contador=0

while True:
    window, event, values = sg.read_all_windows()

    # Eventos na janela 1
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == 'Adicionar':
        janelaInicial.calcularForcas(values, contador)
        contador = contador + 2
        janelaInicial.criarLinha(janela1, contador)
        
    if window == janela1 and event == 'Reiniciar':
        contador = 0
        janela1.close()
        janela1 = janelaInicial.criar_janela_inicial()

    if window == janela1 and event == 'Calcular':
        janelaInicial.calcularForcas(values, contador)
        valorResultanteGeral = janelaInicial.calcularResultantes()
        aceleracao = calcularDados.calculoAceleracao(valorResultanteGeral, float(values['massa']))
        
        resultanteX = janelaInicial.getResultanteGeralN(janelaInicial.retornaListaResultanteX())
        resultanteY = janelaInicial.getResultanteGeralN(janelaInicial.retornarListaResultanteY())
        resultanteZ = janelaInicial.getResultanteGeralN(janelaInicial.retornarListaResultanteZ())

        janela1.hide()
        janela2 = janelaInicial.janelaResposta()
        
        janela2["respostaAceleracao"].update(f'A aceleração é igual a {aceleracao:.2f} m/s²')
        janela2["respostaResultanteX"].update(f'A força resultante X geral é {resultanteX:.2f}N')
        janela2["respostaResultanteY"].update(f'A força resultante Y geral é {resultanteY:.2f}N')
        janela2["respostaResultanteZ"].update(f'A força resultante Z geral é {resultanteZ:.2f}N')


    # Eventos na janela 2
    if window == janela2 and event == 'Reiniciar':
        janela2.close()
        janela1.close()
        janela1 = janelaInicial.criar_janela_inicial()

    if window == janela2  and event == sg.WIN_CLOSED:
        janela1.close()
        break