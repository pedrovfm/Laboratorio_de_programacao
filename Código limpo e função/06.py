def e_perfeito(num):
    divisores = 0
    for i in range(1, num, 1):
        if num % i == 0:
            divisores += i
    if divisores == num:
        return 'É perfeito'
    else:
        return 'Não é perfeito'
print(e_perfeito(6))
print(e_perfeito(28))
print(e_perfeito(35))