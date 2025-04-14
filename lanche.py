print('Lanchonete')
print('1 - Coxinha R$ 5,00')
print('2 - Pastel R$ 7,00')
print('3 - Café R$ 4,00')
print('4 - Suco R$ 6,00')
print('5 - Sair')

Total = 0
while True:
    op = int(input('O que vai ser hoje ?'))
    if (op == 1):
        Qte = int(input('Qual a quantidade ?'))
        Total = Total + Qte * 5.00
    elif (op == 2):
        Qte = int(input('Qual a quantidade ?'))
        Total = Total + Qte * 7.00
    elif (op == 3):
        Qte = int(input('Qual a quantidade ?'))
        Total = Total + Qte * 4.00
    elif (op == 4):
        Qte = int(input('Qual a quantidade ?'))
        Total = Total + Qte * 6.00
    elif (op == 5):
        break
    else:
        print('Não existe')

print(f'\nTotal do Pedido: R$ {Total}')
