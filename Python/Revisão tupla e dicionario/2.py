agenda = {}
def incluirNovoNome(nome, *telefones):
    agenda[nome] = list(telefones)

def incluirTelefone(nome, telefone):
    try:
        agenda[nome].append(telefone)
    except:
        incluir = input('Nome não encontrado, deseja incluir? ').lower()
        if incluir == 'sim':
            incluirNovoNome(nome, telefone)

def excluirTelefone(nome, telefone):
    if len(agenda[nome]) == 1:
        del agenda[nome]
    else:
        agenda[nome].remove(telefone)

def excluirNome(nome):
    try:
        del agenda[nome]
    except:
        print(f'{nome} não está na agenda.')

def consultarTelefone(nome):
    return agenda[nome]
