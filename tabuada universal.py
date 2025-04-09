numero = int(input("Digite um número: "))
limite = int(input("Até qual multiplicador? "))

print(f"\nTabuada do {numero} até {limite}:")
i = 1
while i <= limite:
    print(f"{numero} x {i} = {numero * i}")
    i += 1