respostas = []

conhecia = input('Conhecia a vitima? ')
respostas.append('sim') if conhecia == 'sim' else respostas.append('nao')

mora_perto = input('Mora perto da vítima? ')
respostas.append('sim') if mora_perto == 'sim' else respostas.append('nao')

telefonou = input('Telefonou para a vitima? ')
respostas.append('sim') if telefonou == 'sim' else respostas.append('nao')

esteve_local_crime = input('Esteve no local do crime? ')
respostas.append('sim') if esteve_local_crime == 'sim' else respostas.append('nao')

devia = input('Devia para a vitima? ')
respostas.append('sim') if devia == 'sim' else respostas.append('nao')

trabalhou_junto = input('Trabalhou com a vitima? ')
respostas.append('sim') if trabalhou_junto == 'sim' else respostas.append('nao')

if respostas.count('sim') == 2:
    print('Suspeito(a)')
if 3 <= respostas.count('sim') <= 4:
    print('Cúmplice')
if 5 <= respostas.count('sim') <= 6:
    print('Assassino(a)')
else:
    print('Inocente')