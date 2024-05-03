def retornarNumeros(n1, n2):
    nums = [n1, n2]
    if (n1 % 2 == 0) and (n2 % 2 == 0):
        return min(nums)
    elif (n1 % 2 != 0) or (n2 % 2 != 0):
        return max(nums)

print(retornarNumeros(5,2))