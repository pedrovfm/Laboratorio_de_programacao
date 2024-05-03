import pessoa, pandas as pd
Pessoa = pessoa.Pessoa

class Aluno(Pessoa):
    def __init__(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int, sexo=str, codigo=int, interesse=str, desconto=float):
        super().__init__(nome, rg, cpf, diaNasc, mesNasc, anoNasc, sexo)
        self.__codigo = codigo
        self.__interesse = interesse
        self.__desconto = desconto
    
    def cadastrarAluno(self):
        aluno = [[self._Pessoa__nome, self._Pessoa__rg, self._Pessoa__cpf, self._Pessoa__diaNasc, self._Pessoa__mesNasc, self._Pessoa__anoNasc, self._Pessoa__sexo, self.__codigo, self.__interesse, self.__desconto]]
        df = pd.DataFrame(aluno, columns = ['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo', 'Codigo', 'Interesse', 'Desconto'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\Alunos.csv')
        except FileNotFoundError:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Alunos.csv', header = True, index = False, sep = ',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Alunos.csv', header = False, index = False, sep = ',', mode = 'a')

    def exibirAluno(self):
        self.exibir()
        print(f'Codigo: {self.__codigo}\nInteresse: {self.__interesse}\nDesconto: {self.__desconto}')

if __name__ == '__main__':
    joao = Aluno('Joao', '123456', '123456789', 1, 1, 2000, 'M', 123, 'SI', 0.5)
    pedro = Aluno('Pedro', '123456', '123456789', 2, 5, 2001, 'M', 123, 'CC', 0)
    pedro.cadastrarAluno()
    joao.cadastrarAluno()
    pedro.exibirAluno()
    joao.exibirAluno()
   