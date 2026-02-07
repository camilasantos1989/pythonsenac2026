"""
Cap03 - Atividade 01
Verificar Número Par e Impar

Objetivos:
Exercício - Estrutura de Decisão (if/eslse)
para verificar se o número é par ou impar

Comandos utilizados:
If, operador % (retorna o resto da divisão entre operandos)

"""

import os
os.system('cls')

"""
numero = int(input('Informe um número inteiro: '))
resto = int(numero % 2)

if(resto == 0):
    print(f'O número {numero} é: PAR')
else:
    print(f'O número {numero} é: IMPAR')
print()
print('---------------------')
print('*********************')
print('Final do Algoritmo!!!')

"""

"""
 Cap03 - Atividade 02
  Conversor de Medidas

  Objetivos:
  Nesta atividade você vai converter um número em centimetros para Polegada, Pé ou Jarda. 
  Será necessário usar o comando if / elif / else.

  Comandos utilizados:
  If / elif / else, formatação de números com posição de substituição {:.4f}
"""

medidaCm = float(input('Digite a medida em cemtímetros: '))
print('1 Polegada\n2 - Pé\n3 - Jarda')
menu = input('Opção: ')
if(menu == '1'):
    unidade = 'Polegada'
    resConversao = medidaCm/2.54
#else:
#    if(menu == '2'):
#        #unidade = 'Polegada'
#        resConversao = medidaCm/2.54
elif (menu == '2'):
    unidade = 'Pé'
    resConversao = medidaCm/30.48
elif (menu == '3'):
    unidade = 'Jarda'
    resConversao = medidaCm/91.44
else:
    #unidade = 'Inválida'
    #resConversao = 0
#print(f'{medidaCm} cm em {unidade} corresponde a: {resConversao: .4f}')

    print('Opção Inválida')
print(f'{medidaCm} cm em {unidade} corresponde a: {resConversao: .4f}' if ('unidade' in globals()) else '')
print('----------------')
print('unidade' in globals())
print(globals())