import aluno
Aluno = aluno.Aluno

class Matricula(Aluno):
    def __init__(self):
        pass

    def matricular(self, id=int, mesMat=int, anoMat=int):
        Aluno.cadastrarAluno(self, 12345678, 'Sistemas de Informação', 0)
        self.__id = id
        self.__mesMat = mesMat
        self.__anoMat = anoMat

    def getId(self):
        return self.__id
    def getMesMat(self):
        return self.__mesMat
    def getAnoMat(self):
        return self.__anoMat
    
    def exibirMat(self):
        self.exibirAluno()
        print(f'ID: {self.getId()}\nData de Matrícula: {self.getMesMat()}/{self.getAnoMat()}')

if __name__ == '__main__':
    matricula = Matricula()
    matricula.matricular(123456, 3, 2021)
    matricula.exibirMat()
