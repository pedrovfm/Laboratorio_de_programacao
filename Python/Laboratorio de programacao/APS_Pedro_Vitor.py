velocidade_atual = int(input("Velocidade atual do veículo: "))
multa = (velocidade_atual - 60) * 14

if velocidade_atual < 0:
    print("Velocidade inválida.")
else:
    if velocidade_atual <= 60:
        print("Siga sua viagem com segurança.")
    if velocidade_atual > 60:
        print("Você recebeu uma multa no valor de R$%.2f" % multa)
