def somaImposto(taxa, custo):
    total = custo + (custo * taxa)
    return print(f'Produto de R${custo:.2f} a taxa de {taxa:.0%} passa a custar: R${total:.2f}')
somaImposto(0.15, 100)