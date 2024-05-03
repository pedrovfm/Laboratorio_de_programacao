def valorPagamento(prestacao, atraso):
    comJuros = prestacao + (prestacao * 0.03) + (atraso * 0.001)
    if atraso == 0:
        print(f'R${prestacao: .2f}')
        return prestacao
    else:
        print(f'R${comJuros:.2f}')
        return comJuros

def pagarPrestacao():
    pago = 0
    while True:
        prestacao = input('Valor da prestação: (s = parar) ')
        if prestacao == 's':
            print(f'Total pago: R${pago:.2f}')
            break
        atraso = input('Dias em atraso: (s = parar) ')
        if atraso == 's':
            print(f'Total pago: R${pago:.2f}')
            break
        pago += valorPagamento(float(prestacao), int(atraso))
pagarPrestacao()