def maiorNota():
    alunos = {}
    while True:
        nome = input('Nome: ')
        if nome == 'oooo':
            for (k, v) in alunos.items():
                if max(alunos.values()) == v:
                    print(k)
                    return k
        nota = float(input(f'Nota de {nome}: '))
        alunos[nome] = nota
maiorNota()