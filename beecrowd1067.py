1067
'''Coletar um número inteiro entre 0 e 1000 e imprimir todos os números impares até ele(inclusive)'''
num = int(input())
for numImpar in range(1,num + 1, 2):
    print(numImpar)