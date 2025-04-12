qtdNumsAnalisados = int(input())
for x in range(1,qtdNumsAnalisados + 1):
    numx = int(input())
    match numx:
        case _:
            print('EVEN POSITIVE') if numx % 2 == 0 and numx > 0 else print('ODD NEGATIVE') if numx % 2 != 0 and numx < 0 else print('ODD POSITIVE') if numx % 2 != 0 and numx > 0 else print('EVEN NEGATIVE') if numx % 2 == 0 and numx < 0 else print('NULL')