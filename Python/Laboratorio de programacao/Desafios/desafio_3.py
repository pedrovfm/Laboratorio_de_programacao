import random

tabuleiro = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

def exibir_game():
    print(*tabuleiro, sep='\n')

def marcar_usuario():
    parar = True
    i = 0
    j = 0
    while parar == True:
        exibir_game()
        jogada = input('Onde você quer jogar? ')
        if str(tabuleiro[i]).find(jogada) != -1:
            tabuleiro[i] = 'x'
        i += 1
        j += 1
        if j == 9:
            j = 0
marcar_usuario()
