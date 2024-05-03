from random import choice
import string
senha = ''
tamanho = int(input('De quantos caracteres sua senha precisa? '))
for i in range(tamanho):
    senha += choice(string.printable)
print(senha)