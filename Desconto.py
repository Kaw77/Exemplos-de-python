preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto (0-100)%: '))
desconto =preco * (percentual / 100)
Valor_final = preco - desconto
print('O preço do produto é {}. Desconto de {}% '.format(preco, percentual))
print(('Valor calculado de desconto: {}. Valor final do produto: {}' . format(desconto, Valor_final)))