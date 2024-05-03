import pessoa
Pessoa = pessoa.Pessoa

class Funcionario(Pessoa):
    def __init__(self):
        pass

    def cadastrarFuncionario(self, matricula=int, setor=str, cargo=str, nivel=int):
        Pessoa.cadastrar(self, 'José', '22222222-2', '222222222-22', 10, 1, 1980, 'M')
        self.__matricula = matricula
        self.__setor = setor
        self.__cargo = cargo
        self.__nivel = nivel
    
    def getMatricula(self):
        return self.__matricula
    def getSetor(self):
        return self.__setor
    def getCargo(self):
        return self.__cargo
    def getNivel(self):
        return self.__nivel
    
    def exibirFuncionario(self):
        self.exibir()
        print(f'Matrícula: {self.getMatricula()}\nSetor: {self.getSetor()}\nCargo: {self.getCargo()}\nNível: {self.getNivel()}')

# if __name__ == '__main__':
#     jose = Funcionario()
#     jose.cadastrarFuncionario(123456, 'Segurança', 'Porteiro', 1)
#     jose.exibirFuncionario()