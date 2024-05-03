import professor
Professor = professor.Professor

class Coordenador(Professor):
    def __init__(self):
        pass

    def cadastrarCoordenadorProf(self, area=str, plusSalario=float):
        Professor.cadastrarProfessor(self, 'Doutorado', 'Doutor', 'Cálculo')
        self.__area = area
        self.__plusSalario = plusSalario
    
    def getArea(self):
        return self.__area
    def getPlusSalario(self):
        return self.__plusSalario
    
    def exibirCoordenadorProf(self):
        self.exibirProfessor()
        print(f'Área: {self.getArea()}\nPlus Salário: {self.getPlusSalario()}')

    def calcularPlusSalario(self):
        return self.getSalario() + (self.getPlusSalario() * self.getSalario())

if __name__ == '__main__':
    coordenador = Coordenador()
    coordenador.cadastrarCoordenadorProf('Ciências Exatas', 3500)
    coordenador.exibirCoordenadorProf()

# FUNCIONARIO
# 	- PROFESSOR 
# 		NÍVEL: 1(R$6.500), 2(R$8.325,50) E 3(R$12.568,43)
# 		- COORDENADOR
# 			Salário = NIVEL + 15%
# 	- ADMINISTRATIVO
# 		NÍVEL: A(R$1.520,25), B(R$2.362,67), C(R$2.988,92), D(R$3.572,77), e E(R$4.878,67)
# 		- COORDENADOR ADM.
# 			Salário = NIVEL + 13,5%
# 	- ATENDIMENTO
# 		NÍVEL: A(R$1.520,25), B(R$2.362,67), C(R$2.988,92), D(R$3.572,77), e E(R$4.878,67)
