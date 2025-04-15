pessoas = []

imc = lambda peso, altura: peso / (altura * altura)

while True:

    nome = input('Nome: ')

    altura = float(input('Altura (m): '))

    peso = int(input('Peso (kg): '))

    x = imc(peso, altura)

    pessoas.append([nome, altura, peso, x])

    res = input('Deseja fazer mais um cadastro? [S/N]')

    if res in 'Nn':

        break

print('Cadastros: ', pessoas)

print('Total de Cadastros: ', len(pessoas))

maior = 0

menor = 99

for cadastro in pessoas:

    if cadastro[3] > maior:

        maior = cadastro[3]

    if cadastro[3] < menor:

        menor = cadastro[3]

print('Maior IMC:',maior)

print('Menor IMC:',menor)
