import random
def desenharMoldura(l = random.randrange(1,20), c = random.randrange(1,20)):
    moldura = []
    print(l, c)
    for i in range(l):
        moldura.append([])
        for j in range(c):
            moldura[i].append('.')
    for m in range(l):
        for n in range(c):
            moldura[0][n] = '-'
            moldura[l-1][n] = '-'
            moldura[m][0] = '|'
            moldura[m][c-1] = '|'
    moldura[0][0] = '+'
    moldura[0][c - 1] = '+'
    moldura[l - 1][0] = '+'
    moldura[l - 1][c - 1] = '+'
    for x in range(l):
        print(moldura[x])

desenharMoldura()
