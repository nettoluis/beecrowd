1095
'''Imprimir uma sequência I que cresce de 3 em 3, começando do 1, e uma sequencia J que diminui de 5 em 5, começando do 60'''
for i,j in zip(range(1,38,3),range(60,-1,-5)):
    print(f'I={i} J={j}')