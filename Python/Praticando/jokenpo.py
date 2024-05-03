from random import choice
opcoes = ['pedra', 'papel', 'tesoura']
marcador = True
placar_j = 0
placar_c = 0

while marcador:
    print(f'-------------------------------------\n\
PLACAR: {placar_j} x {placar_c}')
    jogada = input(f'-------------------------------------\n\
Pedra, papel ou tesoura? (s = parar)\n\
-------------------------------------\n').lower()
    computador = choice(opcoes)
    if jogada == 's':
        marcador = False
        print(f'-------------------------------------\n\
PLACAR: {placar_j} x {placar_c}')
        if placar_j == placar_c:
            print('EMPATE!')
        elif placar_j > placar_c:
            print('VITÓRIA!')
        else:
            print('DERROTA!')
    elif jogada == computador:
        print(f'x {computador}\n')
        continue
    elif jogada == 'pedra':
        if computador == 'papel':
            print(f'x {computador}\n')
            placar_c += 1
        else:
            print(f'x {computador}\n')
            placar_j += 1
    elif jogada == 'papel':
        if computador == 'tesoura':
            print(f'x {computador}\n')
            placar_c += 1
        else:
            print(f'x {computador}\n')
            placar_j += 1
    elif jogada == 'tesoura':
        if computador == 'pedra':
            print(f'x {computador}\n')
            placar_c += 1
        else:
            print(f'x {computador}\n')
            placar_j += 1