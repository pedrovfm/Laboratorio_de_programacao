# https://www.respondeai.com.br/conteudo/programacao/python/lista-de-exercicios/tuplas-e-dicionarios-2182
def contaVogais(s):
    vogais = {}
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            vogais[s[i]] = 0
            vogais[s[i]] += 1
    return vogais
print(contaVogais('pedro vitor'))
print(contaVogais('aeiou'))
