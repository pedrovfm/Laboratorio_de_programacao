tempo = int(input('Quantas horas a viagem levou? '))
velocidade = int(input('Qual a velocidade média durante a viagem? '))
distancia = tempo * velocidade
combustivel = distancia/12

print('Velocidade média: %.0fKm/h' % velocidade)
print('Tempo gasto: %.0fh' % tempo)
print('Distância percorrida: %.0fKm' % distancia)
print('Combustível gasto: %.0fL' % combustivel)
