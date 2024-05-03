def converterHora(h, m):
    hInt = int(h)
    if hInt == 0:
        return f'00:{m} A.M. para 24h = 00:{m}'
    elif hInt > 12:
        return f'{hInt}:{m} para 12h = {hInt-12}:{m}'
    else:
        ampm = input('A ou P? (A.M./P.M.) ').lower()
        if hInt == 12 and ampm == 'p':
            return f'{hInt}:{m} P.M. para 24h =  00:{m}'
        else:
            return f'{hInt}:{m} P.M. para 24h = {hInt+12}:{m}' if ampm == 'p' else f'{hInt}:{m} A.M. para 24h = {hInt}:{m}'

def imprimirConversao():
    while True:
        horario = input('Insira o horário:\n(s = parar) ').lower()
        if horario == 's':
            break
        hora = horario.split(':')[0]
        min = horario.split(':')[1]
        print(converterHora(hora, min))
imprimirConversao()