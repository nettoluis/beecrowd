numInteiro = int(input())
for numImpar in range(numInteiro,numInteiro + 12,2):
        print(numImpar) if numImpar % 2 != 0 else print(numImpar + 1)
