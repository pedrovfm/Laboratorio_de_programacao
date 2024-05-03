import pessoa
Pessoa = pessoa.Pessoa

class Aluno(Pessoa):
    def __init__(self):
        pass

    def cadastrarAluno(self, codigo=int, interesse=str, desconto=float):
        Pessoa.cadastrar(self, 'Pedro', '11111111-1', '111111111-11', 6, 3, 2001, 'M')
        self.__codigo = codigo
        self.__interesse = interesse
        self.__desconto = desconto
    
    def getCodigo(self):
        return self.__codigo
    def getInteresse(self):
        return self.__interesse
    def getDesconto(self):
        return self.__desconto
    
    def exibirAluno(self):
        self.exibir()
        print(f'Código: {self.getCodigo()}\nInteresse: {self.getInteresse()}\nDesconto: {self.getDesconto()}')

# if __name__ == '__main__':
#     pedro = Aluno()
#     pedro.cadastrarAluno(12345678, 'Sistemas de Informação', 0)
#     pedro.exibirAluno()