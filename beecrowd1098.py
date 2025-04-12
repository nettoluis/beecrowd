1098
'''Imprimir uma sequência I, que começa em 0 e vai até 2---crescendo de 0,2 em 0,2--, e uma sequência J, que começa com 1,2,3 e vai sendo adicionado o valor de I'''
for i in range(0,22,2):
    for j in range(1,4,1):
        print(f'I={i/10} J={j + i/10}') if float(i/10) != int(i/10) else print(f'I={int(i/10)} J={j + int(i/10)}')