def encontrarChave(dicionario, value):
    key = []
    for (k, v) in dicionario.items():
        if value == v:
            key.append(k)
    print(key)

identidade = {'nome':'pedro', 'idade':22, 'sexo':'masculino'}
encontrarChave(identidade, 22)