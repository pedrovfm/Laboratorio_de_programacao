def compra(valor, **conta):
    contaCartao = {}
    for (k, v) in conta.items():
        contaCartao[k] = v
    contaCartao['saldo'] -= valor
    print(contaCartao)
    return contaCartao
compra(500, saldo=350, transacoes=1, media=300)