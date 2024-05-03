for i in range(50, 301, 1):
    i = str(i) #transformar o num atual em string
    digitos_str = list(i) #armazenar digitos separadamente na lista de string
    digitos_num = []
    for i2 in digitos_str:
        digitos_num.append(int(i2)) #adicionar digitos na lista de inteiros
    if sum(digitos_num) % 2 == 0:
        print(i)