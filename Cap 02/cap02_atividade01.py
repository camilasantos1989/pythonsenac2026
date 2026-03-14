import os
os.system('cls')

#ladoA = float(input('Insira o altura valor: '))
#ladoB = float(input('Insira o comprimento valor: '))
ladoA = int(input('Insira o 1º valor:'))
ladoB = int(input('Insira o 2º valor:'))

#ladoA = int(ladoA)
#ladoB = int(ladoB)
area = int(ladoA)*int(ladoB)
print(type(ladoA), type(ladoB))

soma = ladoA + ladoB
subtracao = ladoA - ladoB
multiplicacao = ladoA * ladoB
divisao = ladoA / ladoB

area = ladoA * ladoB

print('/nResultados: ', f'soma: {soma}', f'subtracao: {subtracao}', f'multiplicacao: {multiplicacao}', f'área do ret~engulo: {area}, cm²')
#print(f'soma: {soma}')
#print(f'subtracao: {subtracao}')
#print(f'multiplicacao: {multiplicacao}')
#print(f'divisao: {divisao}')
#print(f'Área do retângulo: {area}, cm²')