lista = list()
lista.append('Python, Java, C, Visual Basic, JavaScript, Assembly, PHP, Objective-C, Go, Delphi, Fortran, Swift, R, Perl e Ruby')

with open('linguagens.txt', 'w') as arquivo:
    arquivo.writelines(lista)
with open('linguagens.txt', 'r') as arquivo:
    print(arquivo.read())
    arquivo.close()