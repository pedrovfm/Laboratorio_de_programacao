criancas_nascidas = int(input('Número de crianças nascidas: '))
sexo_crianca_morta = 'x'
meses_de_vida = 0
mortes = 0
meninos = 0
viveram_ate_2 = 0
while sexo_crianca_morta != 'fim':
    sexo_crianca_morta = input('Sexo da criança morta: ')
    if sexo_crianca_morta == 'fim':
        break
    meses_de_vida = int(input('Meses de vida da criança: '))
    mortes += 1
    if sexo_crianca_morta == 'masculino':
        meninos += 1
    if meses_de_vida <= 24:
        viveram_ate_2 += 1
print('Porcentagem de crianças mortas: %.0f' % ((mortes/criancas_nascidas)*100))
print('Porcentagem de meninos mortos: %.0f' % ((meninos/mortes)*100))
print('Porcentagem de crianças que viveram até 2 anos: %.0f' % ((viveram_ate_2/mortes)*100))