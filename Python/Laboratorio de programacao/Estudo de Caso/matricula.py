import aluno, pandas as pd
Aluno = aluno.Aluno

class Matricula(Aluno):
    def __init__(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int, sexo=str, codigo=int, interesse=str, desconto=float, id=int, mesMatricula=int, anoMatricula=int):
        super().__init__(nome, rg, cpf, diaNasc, mesNasc, anoNasc, sexo, codigo, interesse, desconto)
        self.__id = id
        self.__mesMatricula = mesMatricula
        self.__anoMatricula = anoMatricula
    
    def matricular(self):
        matricula = [[self._Pessoa__nome, self._Pessoa__rg, self._Pessoa__cpf, self._Pessoa__diaNasc, self._Pessoa__mesNasc, self._Pessoa__anoNasc, self._Pessoa__sexo, self._Aluno__codigo, self._Aluno__interesse, self._Aluno__desconto, self.__id, self.__mesMatricula, self.__anoMatricula]]
        df = pd.DataFrame(matricula, columns = ['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo', 'Codigo', 'Interesse', 'Desconto', 'ID', 'Mes de Matricula', 'Ano de Matricula'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\Matriculas.csv')
        except FileNotFoundError:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Matriculas.csv', header = True, index = False, sep = ',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Matriculas.csv', header = False, index = False, sep = ',', mode = 'a')

if __name__ == '__main__':
    matricula = Matricula('Joao', '123456789', '987654321', 1, 1, 2000, 'M', 1, 'Musculacao', 0.1, 1, 1, 2020)
    matricula.matricular()
    matricula.exibirAluno()