def contador(fim, inicio = 0, passo = 1):

    for i in range(inicio, fim+ 1, passo):

        print(f'{i}', end=' ')

    print('\n')

contador(20, 10, 2)

contador(12)
