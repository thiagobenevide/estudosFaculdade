#from __future__ import annotations
class No:
  def __init__(self, info): #Sei Fazer
    self.info = info
    self.prox = None

class Lista:
  def __init__(self):   # Sei criar uma lista
    self.inicio = None

  def adicionar(self, no: No):
    if self.inicio is None:
      self.inicio = no
    else:
      aux = self.inicio
      while aux.prox != None:
        aux = aux.prox
      aux.prox = no

  def adicionar_no_inicio(self, no: No):
    if self.inicio is None:
      self.inicio = no
    else:
      no.prox = self.inicio
      self.inicio = no

  def imprimir_lista(self):
    aux = self.inicio
    texto = ''
    while aux != None:
      texto = texto + str(aux.info) + '->'
      aux = aux.prox
    print("Lista: ", texto)

  def remocao_inicio(self):
    if self.inicio != None:
      aux = self.inicio
      self.inicio = aux.prox
      return aux.info

  def remocao(self):
    if self.inicio != None:
      aux = self.inicio
      if aux.prox == None:
        self.inicio = None
        return aux.info
      while aux.prox.prox != None:
        aux = aux.prox
      temp = aux.prox
      aux.prox = None
      return temp.info


lista = Lista()
lista.imprimir_lista()
no = No(1)
lista.adicionar(no)
lista.imprimir_lista()
lista.remocao()
lista.imprimir_lista()
no2 = No(2)
lista.adicionar(no2)
lista.imprimir_lista()
no3 = No(3)
lista.adicionar(no3)
lista.imprimir_lista()
no4 = No(4)
lista.adicionar_no_inicio(no4)
lista.imprimir_lista()
valorNo4 = lista.remocao_inicio()
lista.imprimir_lista()
no5 = No(valorNo4)
lista.adicionar(no5)
lista.imprimir_lista()
lista.remocao()
lista.imprimir_lista()