1071
'''Coletar dois números que servirão de parâmetro para a soma dos números ímpares entre eles'''
listaImpares, parametroMaior, parametroMenor = [], int(input()), int(input())
for num in range(parametroMenor + 1, parametroMaior,2):
    listaImpares.append(num) if num % 2 != 0 else listaImpares.append(num + 1)
print(sum(listaImpares))
