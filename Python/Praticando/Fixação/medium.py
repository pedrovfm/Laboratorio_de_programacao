# a) Crie uma lista com os números de 1 a 100 e utilize a função filter() para imprimir somente os números pares.
nums = []
for i in range(1, 101):
    nums.append(i)

def filtro(n):
    if n % 2 == 0:
        return True
    else:
        return False

pares = filter(filtro, nums) # filter() retorna um dado tipo filter
for chave in pares:
    print(chave)

# MEU CODIGO LIMPO
filtrados = []
for j in range(1, 101):
    if j % 2 == 0:
        filtrados.append(j)
for k in range(0, len(filtrados)):
    print(filtrados[k])

# b) Crie uma lista com algumas palavras e utilize a função reduce() para criar uma única string com todas as palavras concatenadas.
palavras = ['pega', 'picApOa', 'noteboOk', 'pedro', 'fluminense']
maiusculo = map(palavras)
for i in range(0, len(maiusculo)):
    print()
print(map(palavras))