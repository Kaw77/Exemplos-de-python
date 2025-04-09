salario = float(input('Qual seu salário? '))
ano_de_admissao = float(input('Qua seu ano de admissão na empresa? '))
ano_atual = float(input('Em que ano estamos? '))
tempo = ano_atual - ano_de_admissao
if (tempo > 5 ):
    bonus = salario * 0.2
else :
    bonus = salario * 0.1
print(f'Você tem {tempo} anos dentro desta empresa. ')
print(f'Seu salário é de {salario}. ')
print(f'Sua bonificação é de {bonus}. ')
print(f'Seu salário final é de {bonus + salario}. ')