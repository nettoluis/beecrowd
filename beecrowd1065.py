1065
'''Coletar uma certa quantidade de números inteiros e retornar quantos são pares'''
listaDeNumeros = int(input()), int(input()), int(input()), int(input()), int(input())
listaDeNumerosPares = []
for num in listaDeNumeros:
    if (abs(num) % 2) == 0:
        listaDeNumerosPares.append(num)
    else:
        pass
print(f'{len(listaDeNumerosPares)} valores pares')

