1114
'''Ler senhas digitadas e imprimir Senha Invalida quando ela for diferente de 2002 e Acesso Permitido quando for'''
while True:
    try:
        senhaDigitada = int(input())
    except ValueError:
        print('Senha Invalida')
        continue
    if senhaDigitada != 2002:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')