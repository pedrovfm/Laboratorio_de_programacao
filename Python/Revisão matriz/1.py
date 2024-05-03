# https://www.facom.ufu.br/~backes/gbt017/ListaPython04.pdf
import random
def criarMatriz():
    matriz = []
    for i in range(4):
        matriz.append([])
        for j in range(4):
            matriz[i].append(random.randint(0, 20))
    return matriz

def maiorQue10(matriz):
    print(matriz)
    maiorQue10 = 0
    for i in range(4):
        for j in range(4):
            if matriz[i][j] > 10:
                maiorQue10 += 1
    print(maiorQue10)
maiorQue10(criarMatriz())