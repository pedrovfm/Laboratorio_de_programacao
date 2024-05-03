# https://wiki.python.org.br/ExerciciosArquivos
with open('IPs.txt', 'w') as arquivo:
    arquivo.write('200.135.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n \
85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256')
with open('IPs.txt', 'r') as arquivo:
    arquivo.read()
    arquivo.close()
with open('IPs.txt', 'w') as arquivo:
    arquivo.write('[Endereços válidos:]\n200.135.80.9\n192.168.1.1\n8.35.67.74\n1.2.3.4 \n\
[Endereços inválidos:]\n257.32.4.5\n85.345.1.2\n9.8.234.5\n192.168.0.256')