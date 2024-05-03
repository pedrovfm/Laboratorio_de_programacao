import random

def gerar_numero():
    num = []
    while len(num) < 5:
        str_num = str(num)
        n_random = str(random.randint(0, 9))
        if str_num.find(n_random) == -1:
            num.append(n_random)
    # print('numero gerado: ', num)
    return num
n_gerado = gerar_numero()

def dar_dicas(num, palpite):
    errado = [0, 'Tente novamente! ']
    certo = [0, ' Você está no caminho certo!']
    posicao_diferente = [0, 'Quase lá! ']
    for i in range(0, 5):
        if str(palpite).find(num[i]) == -1:
            errado[0] += 1
        if str(palpite).find(num[i]) == num.index(num[i]):
            certo[0] += 1
        if (str(palpite).find(num[i]) != num.index(num[i])) and (str(palpite).find(num[i]) != -1):
            posicao_diferente[0] += 1
    if errado[0] == 5:
        return print(errado[1])
    else:
        return print(certo[1] * certo[0], posicao_diferente[1] * posicao_diferente[0])

def receber_respostas():
    respostas = []
    respostas.append(input('Qual o número de 5 dígitos? '))
    dar_dicas(n_gerado, respostas[len(respostas)-1])
    while respostas[len(respostas)-1] != 'stop':
        respostas.append(input('Qual o número de 5 dígitos? '))
        dar_dicas(n_gerado, respostas[len(respostas)-1])

receber_respostas()

