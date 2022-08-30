#from __future__ import annotations
class NoDuplo:
  def __init__(self, info):
    self.info = info
    self.prox = None
    self.ant = None

class ListaDupla:
  def __init__(self):
    self.inicio = None

  def adicionar(self, no: NoDuplo):
    if self.inicio is None:
      self.inicio = no
    else:
      aux = self.inicio
      while aux.prox != None:
        aux = aux.prox
      aux.prox = no
      no.ant = aux

  def adicionar_no_inicio(self, no: NoDuplo):
    if self.inicio is None:
      self.inicio = no
    else:
      aux = self.inicio
      aux.ant = no
      no.prox = aux
      self.inicio = no

  def imprimir_lista(self):
    aux = self.inicio
    texto = ''
    while aux != None:
      texto = texto + str(aux.info) + '->'
      aux = aux.prox
    print("ListaDupla: ", texto)

  def remocao_inicio(self):
    if self.inicio != None:
      aux = self.inicio
      aux.prox.ant = None
      self.inicio = aux.prox
      return aux.info

  def remocao(self):
    if self.inicio != None:
      aux = self.inicio
      if aux.prox == None:
        self.inicio = None
        return aux.info
      while aux.prox != None:
        aux = aux.prox
      aux.ant.prox = None
      return aux.info

lista = ListaDupla()
lista.imprimir_lista()
no = NoDuplo(1)
lista.adicionar(no)
lista.imprimir_lista()
lista.remocao()
lista.imprimir_lista()
no2 = NoDuplo(2)
lista.adicionar(no2)
lista.imprimir_lista()
no3 = NoDuplo(3)
lista.adicionar(no3)
lista.imprimir_lista()
no4 = NoDuplo(4)
lista.adicionar_no_inicio(no4)
lista.imprimir_lista()
valorNo4 = lista.remocao_inicio()
lista.imprimir_lista()
no5 = NoDuplo(valorNo4)
lista.adicionar(no5)
lista.imprimir_lista()
lista.remocao()
lista.imprimir_lista()