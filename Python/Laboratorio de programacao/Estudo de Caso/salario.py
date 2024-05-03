import pandas as pd
class Salario:
    def __init__(self, setor=str, cargo=str, nivel=int):
        self.__planoSaude = 125
        self.__setor = setor
        self.__cargo = cargo
        self.__nivel = nivel

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
        df.to_csv('Laboratorio de programacao\Estudo de Caso\FolhaSalarial.csv', header=False, index=False, sep=';', mode='a')

if __name__ == '__main__':
    salario = Salario('Atendimento', 'Atendente', 1)
    salario.calcularSalario()
    salario.cadastrarSalario()