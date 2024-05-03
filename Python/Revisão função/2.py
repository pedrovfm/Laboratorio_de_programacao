def printar_nstack(n):
    for i in range(1, n+1):
        linha = ''
        for j in range(1, i+1):
            linha += f'{str(j)} '
        print(linha)
n = int(input('Informe um número inteiro: '))
printar_nstack(n)
