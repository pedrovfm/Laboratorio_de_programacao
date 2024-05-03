import random
def criarMatriz():
    matriz = []
    maior = 0
    iMaior = []
    for i in range(4):
        matriz.append([])
        for j in range(4):
            matriz[i].append(random.randint(-20, 20))
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    for l in range(4):
        for c in range(4):
            if matriz[l][c] == maior:
                iMaior.append([l, c])
    for a in range(4):
        print(matriz[a])
    print(maior, iMaior)
criarMatriz()