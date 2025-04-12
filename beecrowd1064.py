listaDeNums = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
listaDeNumsPositivos = []
for i in range(len(listaDeNums)):
    if listaDeNums[i] > 0:
        listaDeNumsPositivos.append(listaDeNums[i])
print(f'{len(listaDeNumsPositivos)} valores positivos')
print(f'{(sum(listaDeNumsPositivos))/(len(listaDeNumsPositivos)):.1f}')