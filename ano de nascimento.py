ano_nasc = int(input('Qual o ano de seu nascimento? '))
ano_atual = int(input('Em que ano estamos? '))
idade = ano_atual-ano_nasc
print(f'Você tem {idade} anos de idade. ')
if (idade >= 18):
    print('Você é de maior e já pode tirar a carteira de motorista!')