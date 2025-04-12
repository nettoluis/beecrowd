1075
'''Coletar um número base e imprimir todos os números(entre 1 e 10000) que divididos por ele dão resto = 2'''
numBase = int(input())
for numDivisível in range(1,10001):
    if numDivisível % numBase == 2:
        print(numDivisível)