import funcionario, pandas as pd
Funcionario = funcionario.Funcionario

class Professor(Funcionario):
    def __init__(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int, sexo=str, matricula=int, nivel=int, formacao=str, nivel2=str, disciplina=str):
        super().__init__(nome, rg, cpf, diaNasc, mesNasc, anoNasc, sexo, matricula, 'Docente', 'Professor', nivel)
        self.__formacao = formacao
        self.__nivel2 = nivel2
        self.__disciplina = disciplina
    
    def cadastrarProfessor(self):
        self.cadastrarFuncionario()
        professor = [[self._Pessoa__nome, self._Pessoa__rg, self._Pessoa__cpf, self._Pessoa__diaNasc, self._Pessoa__mesNasc, self._Pessoa__anoNasc, self._Pessoa__sexo, self._Funcionario__matricula, self._Funcionario__setor, self._Funcionario__cargo, self._Funcionario__nivel, self.__formacao, self.__nivel2, self.__disciplina]]
        df = pd.DataFrame(professor, columns=['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo', 'Matricula', 'Setor', 'Cargo', 'Nivel', 'Formacao', 'Nivel2', 'Disciplina'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\Professores.csv')
        except FileNotFoundError:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Professores.csv', header=True, index=False, sep=',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Professores.csv', header=False, index=False, sep=',', mode='a')

    def exibirProfessor(self):
        super().exibirFuncionario()
        print(f'Formacao: {self.__formacao}\nNivel: {self.__nivel2}\nDisciplina: {self.__disciplina}')