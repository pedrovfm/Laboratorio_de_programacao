custo_fabrica = int(input('Insira o custo de fábrica: '))
distribuidor = 0.28
impostos = 0.45
custo_consumidor = custo_fabrica + (distribuidor * custo_fabrica) + (impostos * custo_fabrica)
print('Custo do consumidor: R$%.2f' % custo_consumidor)
