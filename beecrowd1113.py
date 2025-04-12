1113
'''Coletar um par de números e indicar se é decrescente ou crescente, quando houver valores iguais, o programa deve parar'''
while True:
    valorUm, valorDois = map(int, input().split())
    print('Crescente') if valorDois > valorUm else print('Decrescente') if valorUm > valorDois else None