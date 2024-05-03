filmes = {'Vingadores - ultimato':2019, 'Vingadores - guerra infinita':2018, 'Os vingadores - the avengers':2012, 'Vingadores - era de ultron':2015, 'Pantera negra':2018, 'Capitao america = guerra civil':2016, 'Aquaman':2018, 'Capita marvel':2019}
with open('filmes.txt', 'w') as arquivo:
    for chave, valor in filmes.items():
        arquivo.write('%s : %s\n' % (chave, valor))
with open('filmes.txt', 'r') as arquivo:
    print(arquivo.read())
    arquivo.close()