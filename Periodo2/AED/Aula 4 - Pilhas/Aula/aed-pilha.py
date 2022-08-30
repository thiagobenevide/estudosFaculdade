class No:
  def __init__(self, valor):
    self.valor = valor
    self.prox = None

class Pilha:
  def __init__(self):
    self.inicio = None

  def push(self, i):
    novo_no = No(i)
    if self.inicio == None:
      self.inicio = novo_no
    else:
      aux = self.inicio
      while aux.prox != None:
        aux = aux.prox
      aux.prox = novo_no

  def pop(self):
    if self.inicio != None:
      aux = self.inicio
      while aux.prox.prox != None:
        aux = aux.prox
      i = aux.valor
      aux.prox = None
      return i

  def top():
    i = self.pop()
    self.push(i)
    return i