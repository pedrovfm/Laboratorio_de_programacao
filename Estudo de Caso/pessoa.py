class Pessoa:
    def __init__(self):
        pass

    def cadastrar(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int,sexo=str):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__diaNasc = diaNasc
        self.__mesNasc = mesNasc
        self.__anoNasc = anoNasc
        self.__sexo = sexo

    def getNome(self):
        return self.__nome
    def getRg(self):
        return self.__rg
    def getCpf(self):
        return self.__cpf
    def getDiaNasc(self):
        return self.__diaNasc
    def getMesNasc(self):
        return self.__mesNasc
    def getAnoNasc(self):
        return self.__anoNasc
    def getSexo(self):
        return self.__sexo
    
    def exibir(self):
        print(f'Nome: {self.getNome()}\nRG: {self.getRg()}\nCPF: {self.getCpf()}\nData de Nascimento: {self.getDiaNasc()}/{self.getMesNasc()}/{self.getAnoNasc()}\nSexo: {self.getSexo()}')