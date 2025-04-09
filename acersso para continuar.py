while True:

  nome = input('Qual o seu nome? ')

  if (nome != 'Lenhadorzinho'):

    continue # volta para inicio do laço

  senha = input('Qual a sua senha? ')

  if (senha == 'Instituicao'):

    break # encerra o laço

print('Acesso concedido.')