#from __future__ import annotations
class No:
  def __init__(self, info):
    self.info = info
    self.prox = None

class ListaCircular:
  def __init__(self):
    self.inicio = None

  def adicionar(self, no: No):
    if self.inicio is None:
      no.prox = no
      self.inicio = no
    else:
      aux = self.inicio
      while aux.prox != self.inicio:
        aux = aux.prox
      no.prox = self.inicio
      aux.prox = no

  def adicionar_no_inicio(self, no: No):
    if self.inicio is None:
      self.inicio = no
    else:
      aux = self.inicio
      while aux.prox != self.inicio:
        aux = aux.prox
      no.prox = self.inicio
      self.inicio = no
      aux.prox = self.inicio


  def imprimir_lista(self):
    aux = self.inicio
    texto = ''
    if self.inicio != None:
      texto = str(aux.info) + '->'
      while aux.prox != self.inicio:
        texto = texto + str(aux.prox.info) + '->'
        aux = aux.prox
      texto = texto + str(aux.prox.info)
    print("ListaCircular: ", texto)

  def remocao_inicio(self):
    if self.inicio != None:
      aux = tmp = self.inicio
      while aux.prox != self.inicio:
        aux = aux.prox
      aux.prox = tmp.prox
      self.inicio = tmp.prox
      return aux.info

  def remocao(self):
    if self.inicio != None:
      aux = self.inicio
      while aux.prox.prox != self.inicio:
        aux = aux.prox
      temp = aux.prox
      aux.prox = temp.prox
      return temp.info

lista = ListaCircular()
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