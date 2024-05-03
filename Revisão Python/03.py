salario = int(input('Informe seu salário: '))
salario_final = float

if salario < 200:
    salario_final = salario - (salario * 0.08)
if 200 <= salario < 500:
    salario_final = salario - (salario * 0.085)
if 500 <= salario < 1000:
    salario_final = salario - (salario * 0.09)
if salario >= 1000:
    salario_final = salario - (salario * 0.095)
print('Salário após desconto do INSS: R$%.2f' % salario_final)