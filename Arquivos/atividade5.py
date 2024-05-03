seriados = {'Stranger things':2016, 'Lupin':2021, 'Uma advogada extraordinaria':2022, 'Bridgerton':2020, 'Manifest':2018, 'Arcane':2021, 'O gambito da rainha':2020, 'Anne with an e':2017}
with open('seriados.txt', 'w') as arquivo:
    for chave, valor in seriados.items():
        arquivo.write('%s : %s\n' % (chave, valor))
with open('seriados.txt', 'r') as arquivo:
    print(arquivo.read())
    arquivo.close()