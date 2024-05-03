import professor, pandas as pd
Professor = professor.Professor

class Coordenador(Professor):
    def __init__(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int, sexo=str, matricula=int, nivel=int, formacao=str, nivel2=str, disciplina=str, area=str):
        super().__init__(nome, rg, cpf, diaNasc, mesNasc, anoNasc, sexo, matricula, nivel, formacao, nivel2, disciplina)
        self.__area = area
        self.__plusSalario = 0.15
        self.__planoSaude = 125
    
    def cadastrarCoordenador(self):
        self.cadastrarFuncionario()
        self.cadastrarProfessor()
        coordenador = [[self._Pessoa__nome, self._Pessoa__rg, self._Pessoa__cpf, self._Pessoa__diaNasc, self._Pessoa__mesNasc, self._Pessoa__anoNasc, self._Pessoa__sexo, self._Funcionario__matricula, self._Funcionario__setor, self._Funcionario__cargo, self._Funcionario__nivel, self._Professor__formacao, self._Professor__nivel2, self._Professor__disciplina, self.__area, self.__plusSalario]]
        df = pd.DataFrame(coordenador, columns=['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo', 'Matricula', 'Setor', 'Cargo', 'Nivel', 'Formacao', 'Nivel2', 'Disciplina', 'Area', 'Plus Salario'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\Coordenadores.csv')
        except FileNotFoundError:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Coordenadores.csv', header=True, index=False, sep=',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Coordenadores.csv', header=False, index=False, sep=',', mode='a')
    
    def calcularPlusSalario(self):
        if self._Funcionario__nivel == 1:
            self.__salarioBruto = 6500
        elif self._Funcionario__nivel == 2:
            self.__salarioBruto = 8325.50
        elif self._Funcionario__nivel == 3:
            self.__salarioBruto = 12568.43
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
        self.__plusSalario = (self.__salarioLiquido * self.__plusSalario) + self.__salarioLiquido
        return self.__plusSalario
    
    def exibirCoordenador(self):
        super().exibirProfessor()
        print(f'Area: {self.__area}\nPlus Salario: {self.calcularPlusSalario():.2f}')