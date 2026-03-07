"""
  Cap07 - Atividade 02
  Criar um Classe 

  Objetivos:
  Nesta atividade você vai criar uma objeto de classe, aprendendo sobre os metodos e propriedades e usar metodos especiais. Irá também aprender a consumir esta classe.

  Comandos utilizados:
  Classe, __init__, __str__, Propriedades e Metodos de uma classe
"""
from cap07_atividade02_classe import Recibo
from os import system, name
def limparTela():
    system('cls') if(name == 'nt') else system('clear')
limparTela()

nome = input('Informe a o nome: ')
dados = Recibo(nome)
v = float(input('Informe o valor: '))
d = input('Informe a descrição: ')
dados.descricao(d) #Sem a utilização de decorador
dados.valor = v #Com a utilizção de decorador setter
limparTela()
print(dados)