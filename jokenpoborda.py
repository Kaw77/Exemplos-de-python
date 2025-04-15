import random

# Variáveis globais para contagem de resultados
v1 = 0  # Vitórias do jogador 1
v2 = 0  # Vitórias do jogador 2 (computador)
empate = 0  # Empates

def valida_int(pergunta, min, max):
    while True:
        try:
            x = int(input(pergunta))
            if min <= x <= max:
                return x
            else:
                print(f"Digite um valor entre {min} e {max}!")
        except ValueError:
            print("Digite um número válido!")

def vencedor(jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1:  # pedra
        if jogador2 == 1:  # pedra
            empate += 1
        elif jogador2 == 2:  # papel
            v2 += 1
        elif jogador2 == 3:  # tesoura
            v1 += 1
    elif jogador1 == 2:  # papel
        if jogador2 == 1:  # pedra
            v1 += 1
        elif jogador2 == 2:  # papel
            empate += 1
        elif jogador2 == 3:  # tesoura
            v2 += 1
    elif jogador1 == 3:  # tesoura
        if jogador2 == 1:  # pedra
            v2 += 1
        elif jogador2 == 2:  # papel
            v1 += 1
        elif jogador2 == 3:  # tesoura
            empate += 1
    return [v1, v2, empate]

def mostrar_resultado(j1, j2):
    opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
    print(f"\nJogador: {opcoes[j1]}  ×  Computador: {opcoes[j2]}")

# Função para criar bordas decorativas
def criar_borda(texto, simbolo='═', largura=40):
    borda = simbolo * largura
    texto_centralizado = texto.center(largura, ' ')
    return f"{borda}\n{texto_centralizado}\n{borda}"

# Programa principal
print(criar_borda(" JOKENPO "))
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('0 - Sair\n')

jogadas = []

print(criar_borda(" PROGRAMA PRINCIPAL ", '═', 40))

while True:
    j1 = valida_int('Escolha (1-3) ou 0 para sair: ', 0, 3)
    if j1 == 0:
        break
    
    j2 = random.randint(1, 3)
    jogadas.append((j1, j2))
    mostrar_resultado(j1, j2)
    resultados = vencedor(j1, j2)

# Resultados finais
print("\n" + criar_borda(" RESULTADOS FINAIS ", '═', 40))
print(f"Total de jogadas: {len(jogadas)}")
print(f"Vitórias do Jogador: {v1}")
print(f"Vitórias do Computador: {v2}")
print(f"Empates: {empate}")

# Mostrar histórico de jogadas
print("\n" + criar_borda(" HISTÓRICO DE JOGADAS ", '═', 40))
for i, (j1, j2) in enumerate(jogadas, 1):
    print(f"Rodada {i:2d}: Jogador={j1} vs Computador={j2}")
