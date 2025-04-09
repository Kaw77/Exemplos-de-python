inicial = int(input('Digite um valor inicial:'))

final = int(input('Digite um valor final:'))

qtd_positivo = 0

qtd_par = 0

qtd_impar = 0

soma_positivo = 0

soma_par = 0

soma_impar = 0

 

i = inicial

if (inicial < final):

  while (i <= final):

    if (i > 0):

      qtd_positivo = qtd_positivo + 1

      soma_positivo = soma_positivo + i

    if (i % 2 == 0):

      qtd_par = qtd_par + 1

      soma_par = soma_par + i

    else:

      qtd_impar = qtd_impar + 1

      soma_impar = soma_impar + i

    i = i + 1

  media_positivo = soma_positivo / qtd_positivo

  media_par = soma_par / qtd_par

  media_impar = soma_impar / qtd_impar

  print(f'Quantidade de valores positivos: {qtd_positivo}')

  print(f'Média de valores positivos: {media_positivo}')

  print(f'Quantidade de valores pares: {qtd_par}')

  print(f'Média de valores pares: {media_par}')

  print(f'Quantidade de valores impares: {qtd_impar}')

  print(f'Média de valores impares: {media_impar}')

 

else:

  print('Você digitou um valor inicial maior ou igual ao final. Encerrando o programa...')