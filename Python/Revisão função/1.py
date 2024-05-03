# https://wiki.python.org.br/ExerciciosFuncoes
def imprimir_n(n):
    for i in range(1, n+1):
        print(f'{str(i)} ' * i)
n = int(input('Insira um número inteiro: '))
imprimir_n(n)