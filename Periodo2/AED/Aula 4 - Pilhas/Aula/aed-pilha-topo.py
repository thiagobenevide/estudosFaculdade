class No:
  def __init__(self, valor):
    self.valor = valor
    self.ant = None

class Pilha:
  def __init__(self):
    self.topo = None

  def push(self, i):
    novo_no = No(i)
    novo_no.ant = self.topo
    self.topo = novo_no

  def pop(self):
    if self.topo != None:
      i = self.topo.valor
      self.topo = self.topo.ant
      return i

  def top(self):
    if self.topo != None:
      i = self.pop()
      self.push(i)
      return i
    else:
      return None

def is_balanceado(expressao):
  pilha_parentesis = Pilha()
  for char in expressao:
    if char == '(':
      pilha_parentesis.push(char)
    elif char == ')':
      if pilha_parentesis.top() == None:
        return False
      else:
        pilha_parentesis.pop()
  if pilha_parentesis.top() != None:
    return False
  return True

def pos_fixo(expressao):
  pilha = Pilha()
  operacoes = '+-*/'
  lista = expressao.split(' ')
  for item in lista:
    if item in operacoes:
      num1 = pilha.pop()
      num2 = pilha.pop()
      if item == '+':
        pilha.push(num1+num2)
      if item == '-':
        pilha.push(num1-num2)
      if item == '*':
        pilha.push(num1*num2)
      if item == '/':
        pilha.push(num1/num2)
    else:
      num = int(item)
      pilha.push(num)
  resultado = pilha.pop()
  print(resultado)

def para_binario(num):
  pilha_binario = Pilha()
  while num != 0:
    resto = num % 2
    num = num // 2
    pilha_binario.push(resto)
  str_binario = ''
  while pilha_binario.top() != None:
    str_binario = str_binario + str(pilha_binario.pop())
  print(str_binario)

para_binario(25)