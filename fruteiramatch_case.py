#Compra de frutas
print('=' * 20)
print('Escolha o que deseja comprar: ')
print('-' * 20)
print('|1 - Maçã|')
print('-' * 20)
print('2 - Laranja')
print('-' * 20)
print('3 - Banana')
print('-' * 20)
produto = int(input('Qual sua escolha? '))
print('=' * 20)
qte = int(input('Quantas unidades? '))
print('=' * 20)
match (produto):
    case 1:
        pagar = qte * 2.3
        print(f'Você comprou {qte} maçãs. Total à pagar: {pagar}' )

    case 2:
        pagar = qte * 3.6
        print(f'Você comprou {qte} laranjas. Total à pagar: {pagar}' )

    case 3:
        pagar = qte * 1.85
        print(f'Você comprou {qte} bananas. Total à pagar: {pagar}' )

    case _:
        print('-' * 20)
        print('Produto inexistente')
        print('-' * 20)
