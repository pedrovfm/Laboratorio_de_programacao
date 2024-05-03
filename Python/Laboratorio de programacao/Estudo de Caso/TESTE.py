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
            pd.read_csv('Pessoas.csv')
        except FileNotFoundError:
            df.to_csv('Pessoas.csv', header = True, index = False, sep = ',')
        else:
            df.to_csv('Pessoas.csv', header = False, index = False, sep = ',', mode = 'a')

    def exibir(self):
        print(f'Nome: {self.__nome}\nRG: {self.__rg}\nCPF: {self.__cpf}\nData de Nascimento: {self.__diaNasc}/{self.__mesNasc}/{self.__anoNasc}\nSexo: {self.__sexo}')

class Salario:
    def __init__(self, salarioBruto=float, salarioLiquido=float, inss=float, irrf=float):
        self.__planoSaude = 125

    def calcularSalario(self):
        try:
            # Docente
            if self.__setor.lower() == 'docente':
                # Professor
                if self.__cargo.lower() == 'professor' or self.__cargo.lower() == 'coordenador':
                    if self.__nivel == 1:
                        self.__salarioBruto = 6500
                    elif self.__nivel == 2:
                        self.__salarioBruto = 8325.50
                    elif self.__nivel == 3:
                        self.__salarioBruto = 12568.43
            # Administrativo
            elif self.__setor.lower() == 'administrativo':
                # Coordenador ADM
                if self.__cargo.lower() == 'coordenador adm':
                    if self.__nivel == 1:
                        self.__salarioBruto = 1520.25
                    elif self.__nivel == 2:
                        self.__salarioBruto = 2362.67
                    elif self.__nivel == 3:
                        self.__salarioBruto = 2988.92
                    elif self.__nivel == 4:
                        self.__salarioBruto = 3572.77
                    elif self.__nivel == 5:
                        self.__salarioBruto = 4878.67
            # Atendimento
            elif self.__setor.lower() == 'atendimento':
                # Atendente
                if self.__cargo.lower() == 'atendente':
                    self.__salarioBruto = 1320
            # inss
            if self.__salarioBruto <= 1320:
                self.__inss = 0.075
            elif 1301.01 <= self.__salarioBruto <= 2571.29:
                self.__inss = 0.09
            elif 2571.30 <= self.__salarioBruto <= 3856.94:
                self.__inss = 0.12
            else:
                self.__inss = 0.14
            # irrf
            if self.__salarioBruto <= 2112:
                self.__irrf = 0
            elif 2112.01 <= self.__salarioBruto <= 2826.65:
                self.__irrf = 0.075
            elif 2826.66 <= self.__salarioBruto <= 3751.05:
                self.__irrf = 0.15
            elif 3751.06 <= self.__salarioBruto <= 4664.68:
                self.__irrf = 0.225
            else:
                self.__irrf = 0.275
            self.__salarioLiquido = self.__salarioBruto - (self.__salarioBruto * self.__inss) - (self.__salarioBruto * self.__irrf) - self.__planoSaude
            return self.__salarioLiquido
        except:
            print('Houve um erro, revise os dados informados.')
        
    def cadastrarSalario(self):
        df = pd.DataFrame([[self.calcularSalario()]])
        df.to_csv('FolhaSalarial.csv', header=False, index=False, sep=';', mode='a')


class Funcionario:
    def __init__(self, pessoa, salario):
        self.__pessoa = pessoa
        self.__salario = salario
    
    def cadastrarFuncionario(self):
        funcionario = [[self._Pessoa__nome, self._Pessoa__rg, self._Pessoa__cpf, self._Pessoa__diaNasc, self._Pessoa__mesNasc, self._Pessoa__anoNasc, self._Pessoa__sexo, self.__matricula, self.__setor, self.__cargo, self.__nivel]]
        df = pd.DataFrame(funcionario, columns=['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo', 'Matricula', 'Setor', 'Cargo', 'Nivel'])
        try:
            pd.read_csv('Funcionarios.csv')
        except FileNotFoundError:
            df.to_csv('Funcionarios.csv', header=True, index=False, sep=',')
        else:
            df.to_csv('Funcionarios.csv', header=False, index=False, sep=',', mode='a')
    
    def exibirFuncionario(self):
        self.exibir()
        print(f'Matricula: {self.__matricula}\nSetor: {self.__setor}\nCargo: {self.__cargo}\nNivel: {self.__nivel}')