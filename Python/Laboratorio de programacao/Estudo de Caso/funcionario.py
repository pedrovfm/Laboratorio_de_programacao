import pandas as pd
from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int, sexo=str, matricula=int, setor=str, cargo=str, nivel=int):
        super().__init__(nome, rg, cpf, diaNasc, mesNasc, anoNasc, sexo)
        self.__matricula = matricula
        self.__setor = setor
        self.__cargo = cargo
        self.__nivel = nivel
    
    def cadastrarFuncionario(self):
        funcionario = [[self._Pessoa__nome, self._Pessoa__rg, self._Pessoa__cpf, self._Pessoa__diaNasc, self._Pessoa__mesNasc, self._Pessoa__anoNasc, self._Pessoa__sexo, self.__matricula, self.__setor, self.__cargo, self.__nivel]]
        df = pd.DataFrame(funcionario, columns=['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo', 'Matricula', 'Setor', 'Cargo', 'Nivel'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\Funcionarios.csv')
        except FileNotFoundError:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Funcionarios.csv', header=True, index=False, sep=',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Funcionarios.csv', header=False, index=False, sep=',', mode='a')
    
    def exibirFuncionario(self):
        self.exibir()
        print(f'Matricula: {self.__matricula}\nSetor: {self.__setor}\nCargo: {self.__cargo}\nNivel: {self.__nivel}')

if __name__ == '__main__':
    funcionario = Funcionario('Joao', '12345678', '12345678910', 1, 1, 2000, 'Masculino', 123, 'Atendimento', 'Atendente', 1)
    funcionario.cadastrarFuncionario()
    funcionario.exibirFuncionario()
