1078
'''Coletar um número e imprimir a tabuada dele até o 10'''
numEscolhido = int(input())
for numMultiplicado in range(1,11):
    print(f'{numMultiplicado} x {numEscolhido} = {numMultiplicado * numEscolhido}')