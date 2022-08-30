import requests
from tkinter import Tk, Label, Button

janela = Tk()
janela.title("Cotação de Moedas")
janela.geometry("400x400")

textoOrientacao = Label(janela, text="Selecione a cotação de moedas para visualizar")
textoOrientacao.grid(column=0, row=0, padx=20, pady=15)

botao = Button(janela, text="Buscar cotações Dolar/Euro/BTC")
botao.grid(column=0, row=1, padx=20, pady=15)

janela.mainloop()