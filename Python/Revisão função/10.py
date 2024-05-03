import random
def craps():
    while True:
        jogada = random.randrange(2, 12)
        print(jogada)
        if jogada == 7 or jogada == 11:
            print(f'Você venceu!')
            break
        elif jogada == 2 or jogada == 3 or jogada == 12:
            print(f'Você perdeu!')
            break
        else:
            ponto = jogada
            print(f'Seu ponto é {ponto}')
            while jogada != 7 or jogada != ponto:
                jogada = random.randrange(2, 12)
                print(jogada)
                if jogada == 7:
                    print(f'Você perdeu!')
                    break
                elif jogada == ponto:
                    print(f'Você venceu!')
                    break
            break
craps()