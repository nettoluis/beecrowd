1094
'''Coletar a quantidade de experimentos, depois coletar quantas cobaias de cada tipo(Coelho, Ratos e Sapos) foram utilizados e fazer uma análise estatística de qual a porcentagem de uso de cada um'''
qtdExperimentos, coelhos, ratos, sapos = int(input()), 0, 0, 0
for times in range(1, qtdExperimentos + 1):
    quantidade, animal = input().split()
    if animal == 'C':
        coelhos += int(quantidade)
    elif animal == 'R':
        ratos += int(quantidade)
    elif animal == 'S':
        sapos += int(quantidade)
total = coelhos + ratos + sapos
print(f'Total: {total} cobaias\nTotal de coelhos: {coelhos}\nTotal de ratos: {ratos}\nTotal de sapos: {sapos}')
perc_coelhos, perc_ratos, perc_sapos = (coelhos / total) * 100, (ratos / total) * 100, (sapos / total) * 100
print(f'Percentual de coelhos: {perc_coelhos:.2f} %\nPercentual de ratos: {perc_ratos:.2f} %\nPercentual de sapos: {perc_sapos:.2f} %')