jogos = {'Wow':2004, 'Diablo':1996, 'The witcher 3: wild hunt':2015, 'Genshin impact':2020, 'Final fantasy':1987, 'Fortnite':2017, 'LOL': 2009, 'Valorant':2019, 'Among us':2018, 'Need for speed':1994}
with open('jogos.txt', 'w') as arquivo:
    for chave, valor in jogos.items():
        arquivo.write('%s : %s\n' % (chave, valor))
with open('jogos.txt', 'r') as arquivo:
    print(arquivo.read())
    arquivo.close()