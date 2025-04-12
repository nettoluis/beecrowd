1066
'''Coletar 5 números inteiros e retornar se são pares ou impares, positivos ou negativos'''
listaDeNumeros = int(input()), int(input()), int(input()), int(input()), int(input())
listaDeNumerosPares, listaDeNumerosImpares, listaDeNumerosPositivos, listaDeNumerosNegativos = [], [], [], []
for num in listaDeNumeros:
    listaDeNumerosPares.append(num) if (num % 2) == 0 else listaDeNumerosImpares.append(num)
    listaDeNumerosPositivos.append(num) if num > 0 else listaDeNumerosNegativos.append(num) if num < 0 else None
print(f'{len(listaDeNumerosPares)} valor(es) par(es)'), print(f'{len(listaDeNumerosImpares)} valor(es) impar(es)'), print(f'{len(listaDeNumerosPositivos)} valor(es) positivo(s)'), print(f'{len(listaDeNumerosNegativos)} valor(es) negativo(s)')
