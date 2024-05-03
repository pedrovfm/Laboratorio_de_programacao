def receberNotas():
    notas = {}
    while True:
        nome = input('Nome: ')
        if nome == '':
            return notas
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        notas[nome] = [nota1, nota2]

def imprimirMedia(nome):
    try:
        notas = receberNotas()[nome]
        n1, n2 = notas
        media = (n1+n2)/2
        print(f'Média de {nome}: {media}')
    except:
        print('Aluno não encontrado.')

def imprimirMaiorMedia():
    medias = receberNotas()
    maior = {}
    for k, v in medias.items():
        medias[k] = (v[0] + v[1]) / 2
        if len(maior) != 1:
            maior[k] = medias[k]
        else:
            nomeMaiorNota = list(maior.keys())
            maiornota = list(maior.values())
            if medias[k] > maiornota[0]:
                del maior[nomeMaiorNota[0]]
                maior[k] = medias[k]
    print(maior)
imprimirMaiorMedia()