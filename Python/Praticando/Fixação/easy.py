# a) Crie uma lista com os números de 1 a 10 e utilize a função len() para imprimir o tamanho da lista.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(nums))

# b) Crie uma string com o nome completo de uma pessoa e utilize a função split() para dividir a string em uma lista com o primeiro nome e o sobrenome.
pedro = 'Pedro Vitor Freitas Melo'
nome = pedro.split(' ')[0]
sobrenome = pedro.split(' ', 1)[1] # .split() retorna uma lista a partir do separador (' ') e do ponto de partida (1)
print(nome)
print(sobrenome)

# c) Crie uma lista com o nome de alguns países e utilize a função sort() para ordenar a lista em ordem alfabética.
paises = ['Brasil', 'Austria', 'Turquia', 'China', 'Zambia', 'Cuba']
paises.sort() # .sort() sempre retorna none
print(paises)

#