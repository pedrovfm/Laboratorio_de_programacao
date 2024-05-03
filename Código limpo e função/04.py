def converterParaCelsius (f):
    c = (5/9) * (f-32)
    return round(c, 2)
print(converterParaCelsius(100))