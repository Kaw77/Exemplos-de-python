def maior3(v1=0, v2=0, v3=0):

  if (v1 and v2 and v3):

    if ((v1 > v2) and (v1 > v3)):

      if (v2 > v3):

        print(f'Ordem crescente: {v3} , {v2} , {v1} ' )

      else:

        print(f'Ordem crescente: {v2} , {v3} , {v1} ' )

    elif ((v2 > v1) and (v2 > v3)):

      if (v1 > v3):

        print(f'Ordem crescente: {v3} , {v1} , {v2} ' )

      else:

        print(f'Ordem crescente: {v1} , {v3} , {v2} ' )

    elif ((v3 > v1) and (v3 > v2)):

      if (v1 > v2):

        print(f'Ordem crescente: {v2} , {v1} , {v3} ' )

      else:

        print(f'Ordem crescente: {v1} , {v2} , {v3} ' )

#Programa Principal

x = int(input('Digite o valor 1: '))

y = int(input('Digite o valor 2: '))

z = int(input('Digite o valor 3: '))

maior3(x, y, z)
