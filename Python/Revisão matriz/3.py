import random
def criarMatriz():
    matriz = []
    l = random.randint(1,10)
    c = random.randint(1,10)
    for i in range(l):
        matriz.append([])
        for j in range(c):
            matriz[i].append(i*j)
    for a in range(l):
        print(matriz[a])
criarMatriz()