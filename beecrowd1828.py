1828
'''Coletar um número inteiro que representará a quantidade de disputas e depois retornar a reação do Sheldon caso ele ganhe, perca ou empate com o Raj'''
qtdPartidas, reacoes, comoGanhar = int(input()), ['Bazinga!', 'De novo!', 'Raj trapaceou!'], {
    'tesoura': ['papel', 'lagarto'],
    'papel': ['pedra', 'Spock'],
    'pedra': ['tesoura', 'lagarto'],
    'lagarto': ['Spock', 'papel'],
    'Spock': ['tesoura', 'pedra']
}
for i in range(1, qtdPartidas + 1):
    sheldon, raj = input(). split()
    if raj in comoGanhar[sheldon]:
        print(f'Caso #{i}: {reacoes[0]}')
    elif sheldon in comoGanhar[raj]:
        print(f'Caso #{i}: {reacoes[2]}')
    else:
        print(f'Caso #{i}: {reacoes[1]}')