1101
'''Coletar dois números e imprimir a soma de todos os números entre eles -- inclusivo'''
while True:
    line = input().strip()
    parts = line.split()
    if len(parts) < 2:
        break
    M, N = map(int, parts)
    if M <= 0 or N <= 0:
        break
    start = min(M, N)
    end = max(M, N)
    sequence = list(range(start, end + 1))
    sequence_str = ' '.join(map(str, sequence))
    total = sum(sequence)
    print(f'{sequence_str} Sum={total}')


