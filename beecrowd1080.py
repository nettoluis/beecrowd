1080
'''Coletar 100 números inteiros, positivos e distintos, apresentar qual o maior e em que posição ele foi digitado'''
listaNums = []
for i in range(1,101):
    num = int(input())
    listaNums.append(num)
    numMaior = max(listaNums)
print(numMaior)
print((listaNums.index(numMaior)) + 1)
