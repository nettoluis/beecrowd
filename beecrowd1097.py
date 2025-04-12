1097
'''Imprimir uma sequência tripla de I, que cresce de 2 em 2, e uma sequencia ciclica J, de 7,6,5 que cresce a cada fim de ciclo'''
for i in range(1, 10, 2):
    for j in range(6, 3, -1):
        print(f"I={i}  J={j+i}")
