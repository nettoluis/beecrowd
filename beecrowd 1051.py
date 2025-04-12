1051
'''Calcular o imposto de renda a ser pago, sabendo que até 2000 reais é isento, acima disso até 3000 é 8%, acima disso até 4500 é 18% e acima disso é 28%'''
salario = float(input())
def calculadoraImpostoRenda(salario):
    aliquotaASerPaga = 0
    if salario <= 2000:
        print('Isento')
    else:
        if salario > 4500:
            aliquotaASerPaga = ((salario - 2000) * 0.08) + ((salario - 3000) * 0.18) + ((salario - 4500) * 0.28) - ((salario - 3000) * 0.08) - ((salario - 4500) * 0.18)
        elif 3000 < salario <= 4500:
            aliquotaASerPaga = ((salario - 2000) * 0.08) + ((salario - 3000) * 0.18) - ((salario - 3000) * 0.08)
        else:
            aliquotaASerPaga = ((salario - 2000) * 0.08)
        print(f"R$ {aliquotaASerPaga:.2f}")
calculadoraImpostoRenda(salario)