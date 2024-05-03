def inverter_string(string):
    string_inversa = []
    for i in range(len(string)-1, -1, -1):
        string_inversa.append(string[i])
    return ''.join(string_inversa)
print(inverter_string('python2023'))
print(inverter_string('0203programacao2023'))
print(inverter_string('luz azul'))
print(inverter_string('arara rara'))
print(inverter_string('anotaram a data da maratona'))
