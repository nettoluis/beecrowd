1072
'''Coletar um valor inteiro N que indicará a quantidade de números inteiros que serão lidos e analisados se estão dentro ou fora do intervalo [10,20]--inclusivo--'''
numCasosTestes,inLista,outLista = int(input()), [], []
for x in range(1,numCasosTestes + 1):
    numx = int(input())
    inLista.append(numx) if 10 <= numx <= 20 else outLista.append(numx)
print(f'{len(inLista)} in\n{len(outLista)} out')
