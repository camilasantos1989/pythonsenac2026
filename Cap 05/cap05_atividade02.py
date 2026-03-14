from os import system, name
system('cls') if(name=='nt') else system('clear')
#biblioteca random



import random

opcoes = ["Pedra", "Papel", "Tesoura"]

while opcoes.upper()=='S':
   opcoes=('Pedra', 'Papel', 'Tesoura')
   print("Escolha a sua jogada: ")
   for i, elemento in enumerate(opcoes):
      print(f'{i+1} - {elemento}')
jogador = int(input())-1
cpuM = random.randint(0,2)
jM = "Parabéns!!! Você venceu :)"
eM = "Deu empate, só perdeu tempo /:"
cpuM = "Deu RED. A CPU venceu :("
resultado =(
            #  0  1  2
              (eM, jM, cpuM)#0
              (cpuM, eM, jM)#1
              (jM, cpuM, eM)#2
            )
print(f'Você escolheu {opcoes[jogador]}')
print(f'A CPU escolheu {opcoes[cpuM]}')
print(resultado[cpuM][jogador])
opcao = input('Digite S para continuar ou qualquer tecla para finalizar. ')


