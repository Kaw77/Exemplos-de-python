#Compra de frutas
print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha? '))
qte = int(input('Quantas unidades? '))
if (produto == 1):
    pagar = qte * 2.3
    print(f'Você comprou {qte} maçãs. Total à pagar: {pagar}' )
else :
    if (produto == 2):
        pagar = qte * 3.6
        print(f'Você comprou {qte} laranjas. Total à pagar: {pagar}' )
    else:
      if (produto == 3):
        pagar = qte * 1.85
        print(f'Você comprou {qte} bananas. Total à pagar: {pagar}' )
      else:
        print('Produto inexistente')
