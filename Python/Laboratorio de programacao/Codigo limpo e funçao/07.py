def receberReais():
    reais = []
    for i in range(0, 5, 1):
        reais.append(float(input('Digite um número real: ')))
    return reais

def retornarMaior(reais):
    return max(reais)

def retornarMenor(reais):
    return min(reais)

print(retornarMaior(receberReais()))