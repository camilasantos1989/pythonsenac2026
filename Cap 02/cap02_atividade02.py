import os
os.system('cls')
nomeCompleto = input('Informe seu nome completo: ')

# função len retorno a quantidade de caracteres de uma variável
# print('l. Quantidade de caracteres: ', len(nomeCompleto))
print('l. Quantidade de caracteres: ', len(nomeCompleto.replace(' ','')))

# upper transforma um texto em maiusculo
print('2. Nome em maiusculo: ', nomeCompleto.upper())

# lower transforma um texto em minusculo
print('3. Nome minusculo:', nomeCompleto.lower())

# lowcapitalize transforma a primeira letra em maiusculo
print('4. Primeira letra em maiusculo:', nomeCompleto.capitalize())

# Somenteo 1º nome - Camila A Santos
espaco  = nomeCompleto.find(' ')
# print(espaço)
nome = nomeCompleto[0:espaco]

print('5. Somente o primeiro nome: ', nomeCompleto)
sobrenome = nomeCompleto[espaco+11:len(nomeCompleto)]

# sobrenome = nomeCompleto[espaco+1;len(nomecompleto)]
print('6. Somente o sobrenome: ', nomeCompleto[espaco+11:len(nomeCompleto)])

# metodo isalpha para verificar se tem somente letras na palavra
somenteLetras = nomeCompleto.replace(' ','') #temos que tirar os espaços para verificar
print('7. Tem somente letras? ', somenteLetras.isalpha())

# metodo isalnum para verificar se tem somente letras ou numeros na palavra
print('8. É alfanumerico? tem letras ou numeros: ', somenteLetras.isalnum())

# metodo split cria uma lista usando o espaço em branco com quebra
# ['camila', 'alessandra', 'dos santos']
print('9. Quebrar os textos a cada espaço em branco: ', nomeCompleto.split(' '))

# metodo center para centralizar o texto em 80 colunas usando o *
print('10. Centralizar o nome entre *')
print(nomeCompleto.center(80,'*'))
