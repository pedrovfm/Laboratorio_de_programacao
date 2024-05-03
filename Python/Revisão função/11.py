def dataPorExtenso(data):
    dia = int(data.split('/')[0])
    mes = int(data.split('/')[1])
    ano = int(data.split('/')[2])
    mesPorExtenso = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho',
                     7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    return f'Dia {dia} de {mesPorExtenso[mes]} de {ano}'
print(dataPorExtenso('08/04/2023'))