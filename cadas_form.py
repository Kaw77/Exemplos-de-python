# Sistema de Cadastro com Dicionário
cadastro = {'nome': [],'sexo': [], 'ano': []}


def valida_idade(pergunta):
    while True:
        try:
            idade = int(input(pergunta))
            if idade > 0:
                return idade
            print("Idade deve ser maior que zero!")
        except ValueError:
            print("Digite um número válido!")

def valida_sexo(pergunta):
    while True:
        sexo = input(pergunta).upper()[0]
        if sexo in 'MF':
            return sexo
        print("Erro! Digite apenas M ou F.")


while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N] ')
    if terminar.upper() in  'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para Sim ou N para Não')
        continue

    # Coleta de dados
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo: ')
    ano = input('Digite seu ano: ')

    # Armazenamento
    cadastro = ['nome'].append(nome)
    cadastro = ['sexo'].append(sexo)
    cadastro = ['ano'].append(ano)

    # Pergunta se deseja continuar
    continuar = input("\nDeseja cadastrar outra pessoa? [S/N] ").upper()[0]
    if continuar == 'N':
        break

    # Relatório final
print('\n' + "=" * 40)
print("RELATÓRIO DE CADASTROS".center(40))
print("=" * 40)

print(f"\nTotal de cadastros: {len(cadastro['nomes'])}")
print("\nLista de Cadastrados:")
for i, (nome, sexo, idade) in enumerate(zip(cadastro['nomes'], cadastro['sexos'], cadastro['anos']), 1):
    print(f"{i}. {nome:<30} | Sexo: {sexo} | Idade: {idade} anos")

# Estatísticas
if cadastro['anos']:
    media_idade = sum(cadastro['anos']) / len(cadastro['anos'])
    print(f"\nMédia de idade: {media_idade:.1f} anos")
    print(f"Homens cadastrados: {cadastro['sexos'].count('M')}")
    print(f"Mulheres cadastradas: {cadastro['sexos'].count('F')}")
