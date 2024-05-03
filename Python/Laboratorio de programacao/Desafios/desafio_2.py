import random

def gerar_resultado():
    caverna = ['serpa_boa', 'serpa_ma']
    resultado = random.choice(caverna)
    return resultado

def jogar_reino_do_serpe():
    escolha = input('Em qual caverna quer entrar? L = caverna esquerda, R = caverna direita ')
    while (escolha == 'L' or escolha == 'R'):
        resultado = gerar_resultado()
        if resultado == 'serpa_ma':
            print('Você foi devorado :(')
            break
        elif resultado == 'serpa_boa':
            print('Você recebeu um tesouro :D')
        escolha = input('Em qual caverna quer entrar? L = caverna esquerda, R = caverna direita ')
jogar_reino_do_serpe()
