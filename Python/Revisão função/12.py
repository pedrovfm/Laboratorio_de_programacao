import random
def embaralhar(s):
    sList = list(s)
    random.shuffle(sList)
    embaralhada = ''
    for i in range(len(s)):
        embaralhada += sList[i]
    return embaralhada
print(embaralhar('pedro vitor'))