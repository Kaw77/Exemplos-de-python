while True:

  try:

    x = int(input('Por favor digite um número: '))

    break

  except ValueError:

    print('Oops!  Número inválido.  Tente novamente...')
