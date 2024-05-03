compras = ['arroz, feijao, acucar, carne moida, macarrao, cafe, leite, sal, temperos prontos, farinha, refrigerante e agua']
with open('compras.txt', 'w') as arquivo:
    arquivo.writelines(compras)
with open('compras.txt', 'r') as arquivo:
    print(arquivo.readlines())
    arquivo.close()
