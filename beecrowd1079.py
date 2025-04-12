1079
'''Coletar um número inteiro que representará a quantidade de casos testes. Em seguida, coletar três números reais que serão calculados a média ponderada, com pesos 2,3 e 5, respectivamente'''
numCasosTestes = int(input())
for i in range(1, numCasosTestes + 1):
    A, B, C = input().split()
    mediaPonderada = ((2 * float(A)) + (3 * float(B)) + (5 * float(C))) / 10
    print(f'{mediaPonderada:.1f}')