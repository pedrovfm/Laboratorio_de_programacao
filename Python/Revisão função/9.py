def numReverso(n):
    reverso = ''
    for i in range(len(n)-1, -1, -1):
        reverso += n[i]
    return reverso
n = input('Informe um número inteiro de qualquer tamanho: ')
print(numReverso(n))