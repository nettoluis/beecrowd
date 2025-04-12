1073
'''Coletar um número inteiro e imprimir todos os números pares até ele(inclusive), junto com seus quadrados'''
num = int(input())
for numPar in range(2,num + 1, 2):
    print(f'{numPar}^2 = {numPar ** 2}')