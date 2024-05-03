import random
import copy
def criarMatriz4x4():
    matriz = []
    for i in range(4):
        matriz.append([])
        for j in range(4):
            matriz[i].append(random.randint(1, 20))
    return matriz

def triangularInferior(m):
    mTri = copy.deepcopy(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i > j:
                mTri[i][j] = 0
    for a in range(len(m)):
        print(m[a])
    print('\n')
    for b in range(len(mTri)):
        print(mTri[b])
triangularInferior(criarMatriz4x4())