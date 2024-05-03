vendas = int(input('Vendas em R$: '))
salario = int
if vendas > 20000:
    salario = vendas * 0.01
else:
    salario = vendas * 0.075
print('Salário: R$ {:.2f}'.format(salario))