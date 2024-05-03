import random

def vericarQuadrado(quadrado):
    condicao = quadrado[0] + quadrado[1] + quadrado[2] == quadrado[3] + quadrado[4] + quadrado[5] == \
quadrado[6] + quadrado[7] + quadrado[8] == quadrado[0] + quadrado[3] + quadrado[6] == \
quadrado[1] + quadrado[4] + quadrado[7] == quadrado[2] + quadrado[5] + quadrado[8] == \
quadrado[0] + quadrado[4] + quadrado[8] == quadrado[2] + quadrado[4] + quadrado[6]
    if condicao == True:
        return quadrado

def quadradosMagicos():
    quadradosMagicos = []
    nums = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]
    while True:
        random.shuffle(nums)
        quadrado = vericarQuadrado(nums)
        if type(quadrado) == list:
            quadradosMagicos.append(quadrado)
        for i in range(len(quadradosMagicos)):
            for j in range(len(quadradosMagicos)):
                if quadradosMagicos[i] == quadradosMagicos[j] and i != j:
                    del quadradosMagicos[j]

quadradosMagicos()

