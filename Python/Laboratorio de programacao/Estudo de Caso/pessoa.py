import pandas as pd

class Pessoa:
    def __init__(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int,sexo=str):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__diaNasc = diaNasc
        self.__mesNasc = mesNasc
        self.__anoNasc = anoNasc
        self.__sexo = sexo

    def cadastrar(self):
        pessoa = [[self.__nome, self.__rg, self.__cpf, self.__diaNasc, self.__mesNasc, self.__anoNasc, self.__sexo]]
        df = pd.DataFrame(pessoa, columns = ['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\Pessoas.csv')
        except FileNotFoundError:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Pessoas.csv', header = True, index = False, sep = ',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Pessoas.csv', header = False, index = False, sep = ',', mode = 'a')

    def exibir(self):
        print(f'Nome: {self.__nome}\nRG: {self.__rg}\nCPF: {self.__cpf}\nData de Nascimento: {self.__diaNasc}/{self.__mesNasc}/{self.__anoNasc}\nSexo: {self.__sexo}')