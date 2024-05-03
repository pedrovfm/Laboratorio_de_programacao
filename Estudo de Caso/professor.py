import funcionario
Funcionario = funcionario.Funcionario

class Professor(Funcionario):
    def __init__(self):
        pass

    def cadastrarProfessor(self, formacao=str, nivel=str, disciplina=str):
        Funcionario.cadastrarFuncionario(self, 123456, 'Doscente', 'Professor', 1)
        self.__formacao = formacao
        self.__nivel = nivel
        self.__disciplina = disciplina
    
    def getFormacao(self):
        return self.__formacao
    def getNivel(self):
        return self.__nivel
    def getDisciplina(self):
        return self.__disciplina
    
    def exibirProfessor(self):
        self.exibirFuncionario()
        print(f'Formação: {self.getFormacao()}\nNível: {self.getNivel()}\nDisciplina: {self.getDisciplina()}')

if __name__ == '__main__':
    maria = Professor()
    maria.cadastrarProfessor('Doutorado', 'Doutor', 'Programação')
    maria.exibirProfessor()