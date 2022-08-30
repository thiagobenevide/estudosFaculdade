from math import radians, cos,sin,tan
import PySimpleGUI as sg
from matplotlib import pyplot as plt
from telaResposta import TelaResposta
from telaInicial import TelaInicial

if __name__ == "main":
    telaInicial = TelaInicial()
    telaResposta = TelaResposta()
    
    janela1 = telaInicial.telaEntradaDados()
    janela2 = telaResposta.telaResposta()
    
    while True:
        window, values, event = sg.read_all_windows()
                        
        if window == janela1 and event == sg.WIN_CLOSED:
            break
        
        if window == janela2 and event == sg.WIN_CLOSED:
            break

        if window == janela1 and event == "calcular":
                  
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
            
            
        
        plt.style.use('ggplot')
        plt.title('Gráfico',fontsize=16, fontweight='bold')
        plt.xlabel('x', fontsize=9)
        plt.ylabel(f'y', fontsize=9)
        plt.plot(listaPontosX, listaPontosY, marker='o')
        plt.show()
        
        
        

