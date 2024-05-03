PALAVRAS_DICAS = {'cabeca':'parte do corpo onde se encontra o cerebro',
'cadeira':'objeto ao qual uma pessoa senta',
'vazio':'ausência de algo',
'india':'segundo pais mais populoso do mundo',
'lixo':'o que não serve mais',
'casa':'lugar onde as familias residem',
'condominio':'conjunto de prédios agrupados',
'mar':'vasta extensão de água salgada'}

PALAVRAS = list(PALAVRAS_DICAS.keys())
DICAS = list(PALAVRAS_DICAS.values())
tabuleiro = []

def preencher_tabuleiro():
    for i in range(9):
        linha = []
        tabuleiro.append(linha)
        for j in range(10):
            linha.append('')
preencher_tabuleiro()



