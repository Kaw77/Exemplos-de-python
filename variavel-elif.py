nome = input('Qual é seu nome? ')
idade = int(input('Qual é sua idade? '))

if nome == 'Carlos':
    print('Olá Carlos! ')
elif idade < 18:
    print('Voce não é Carlos e é menor de idade ')
elif idade > 100:
    print('Diferente de você o Carlos não é imortal! ')
