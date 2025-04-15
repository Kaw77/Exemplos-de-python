item = []

mercado = []

for i in range(3):

  item.append(input('Digite o nome do item:'))

  item.append(int(input('Digite a quantidade:')))

  item.append(float(input('Digite o valor:')))

  mercado.append(item[:])

  item.clear()

print(mercado)


soma = 0
print('Lista de compras:')
print('-' * 20)
print('item |quantidade |valor unitário |total ')
for item in mercado:
    print('{} | {} | {} | {} ' .format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print(f'Soma total: {soma}')
