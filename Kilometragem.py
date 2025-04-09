km = int(input('Quantos km foram percorridos '))
dias = int(input('Quantos dias foram percorridos '))
# Preço por dia mais por km
preco = 60 * dias + 0.15 * km

print(f'km = {km} Dias : {dias}')
print(f'Valor a ser pago: {preco}')