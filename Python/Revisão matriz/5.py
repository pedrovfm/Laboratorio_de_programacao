import random
def criarMatriz4x4():
    matriz = []
    for i in range(4):
        matriz.append([])
        for j in range(4):
            matriz[i].append(random.randint(-20, 20))
    return matriz

def compararMatrizes(m1, m2):
    resultado = []
    for i in range(4):
        resultado.append([])
        for j in range(4):
            resultado[i].append(max(m1[i][j], m2[i][j]))
    print(m1, '\n', m2, '\n')
    for a in range(4):
        print(resultado[a])
compararMatrizes(criarMatriz4x4(), criarMatriz4x4())