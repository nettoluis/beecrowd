1099
'''Coletar um número inteiro que determina qual a quantidade de casos-teste, depois printar a soma dos impares entre dois valores também inteiros'''
numCasosTeste = int(input())
for casosTeste in range(1,numCasosTeste + 1):
    limite1, limite2 = map(int,input().split())
    somaImpares, limiteMaior, limiteMenor = 0, max(limite1,limite2), min(limite1,limite2)
    for numImpar in range(int(limiteMenor) + 1,int(limiteMaior)):
        if numImpar % 2 != 0:
            somaImpares += numImpar
    print(somaImpares)
