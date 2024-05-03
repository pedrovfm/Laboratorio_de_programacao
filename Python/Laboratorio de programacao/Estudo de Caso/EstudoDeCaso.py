import pandas as pd

class Pessoa:
    def __init__(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int,sexo=str):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__diaNasc = diaNasc
        self.__mesNasc = mesNasc
        self.__anoNasc = anoNasc
        self.__sexo = sexo

    def cadastrar(self):
        pessoa = [[self.__nome, self.__rg, self.__cpf, self.__diaNasc, self.__mesNasc, self.__anoNasc, self.__sexo]]
        df = pd.DataFrame(pessoa, columns = ['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\Pessoas.csv')
        except FileNotFoundError:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Pessoas.csv', header = True, index = False, sep = ',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Pessoas.csv', header = False, index = False, sep = ',', mode = 'a')

    def exibir(self):
        print(f'Nome: {self.__nome}\nRG: {self.__rg}\nCPF: {self.__cpf}\nData de Nascimento: {self.__diaNasc}/{self.__mesNasc}/{self.__anoNasc}\nSexo: {self.__sexo}')

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

class Coordenador(Professor):
    def __init__(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int, sexo=str, matricula=int, nivel=int, formacao=str, nivel2=str, disciplina=str, area=str):
        super().__init__(nome, rg, cpf, diaNasc, mesNasc, anoNasc, sexo, matricula, nivel, formacao, nivel2, disciplina)
        self.__area = area
        self.__plusSalario = 0.15
        self.__planoSaude = 125
    
    def cadastrarCoordenador(self):
        # self.cadastrarFuncionario()
        self.cadastrarProfessor()
        coordenador = [[self._Pessoa__nome, self._Pessoa__rg, self._Pessoa__cpf, self._Pessoa__diaNasc, self._Pessoa__mesNasc, self._Pessoa__anoNasc, self._Pessoa__sexo, self._Funcionario__matricula, self._Funcionario__setor, self._Funcionario__cargo, self._Funcionario__nivel, self._Professor__formacao, self._Professor__nivel2, self._Professor__disciplina, self.__area, self.__plusSalario]]
        df = pd.DataFrame(coordenador, columns=['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo', 'Matricula', 'Setor', 'Cargo', 'Nivel', 'Formacao', 'Nivel2', 'Disciplina', 'Area', 'Plus Salario'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\Coordenadores.csv')
        except FileNotFoundError:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Coordenadores.csv', header=True, index=False, sep=',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Coordenadores.csv', header=False, index=False, sep=',', mode='a')
    
    def calcularPlusSalario(self):
        if self._Funcionario__nivel == 1:
            self.__salarioBruto = 6500
        elif self._Funcionario__nivel == 2:
            self.__salarioBruto = 8325.50
        elif self._Funcionario__nivel == 3:
            self.__salarioBruto = 12568.43
        # inss
        if self.__salarioBruto <= 1320:
            self.__inss = 0.075
        elif 1301.01 <= self.__salarioBruto <= 2571.29:
            self.__inss = 0.09
        elif 2571.30 <= self.__salarioBruto <= 3856.94:
            self.__inss = 0.12
        else:
            self.__inss = 0.14
        # irrf
        if self.__salarioBruto <= 2112:
            self.__irrf = 0
        elif 2112.01 <= self.__salarioBruto <= 2826.65:
            self.__irrf = 0.075
        elif 2826.66 <= self.__salarioBruto <= 3751.05:
            self.__irrf = 0.15
        elif 3751.06 <= self.__salarioBruto <= 4664.68:
            self.__irrf = 0.225
        else:
            self.__irrf = 0.275
        self.__salarioLiquido = self.__salarioBruto - (self.__salarioBruto * self.__inss) - (self.__salarioBruto * self.__irrf) - self.__planoSaude
        self.__plusSalario = (self.__salarioLiquido * self.__plusSalario) + self.__salarioLiquido
        return self.__plusSalario
    
    def exibirCoordenador(self):
        super().exibirProfessor()
        print(f'Area: {self.__area}\nPlus Salario: {self.calcularPlusSalario():.2f}')

class CoordenadorAdm(Funcionario):
    def __init__(self, nome=str, rg=str, cpf=str, diaNasc=int, mesNasc=int, anoNasc=int, sexo=str, matricula=int, nivel=int, area=str):
        super().__init__(nome, rg, cpf, diaNasc, mesNasc, anoNasc, sexo, matricula, 'Administrativo', 'Coordenador adm', nivel)
        self.__area = area
        self.__plusSalario = 0.135
        self.__planoSaude = 125
    
    def cadastrarCoordenadorAdm(self):
        self.cadastrarFuncionario()
        coordenadorAdm = [[self._Pessoa__nome, self._Pessoa__rg, self._Pessoa__cpf, self._Pessoa__diaNasc, self._Pessoa__mesNasc, self._Pessoa__anoNasc, self._Pessoa__sexo, self._Funcionario__matricula, self._Funcionario__setor, self._Funcionario__cargo, self._Funcionario__nivel, self.__area]]
        df = pd.DataFrame(coordenadorAdm, columns=['Nome', 'RG', 'CPF', 'Dia de Nascimento', 'Mes de Nascimento', 'Ano de Nascimento', 'Sexo', 'Matricula', 'Setor', 'Cargo', 'Nivel', 'Area'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\CoordenadoresAdm.csv')
        except FileNotFoundError:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\CoordenadoresAdm.csv', header=True, index=False, sep=',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\CoordenadoresAdm.csv', header=False, index=False, sep=',', mode='a')

    
    def calcularPlusSalario(self):
        if self._Funcionario__nivel == 1:
            self.__salarioBruto = 1520.25
        elif self._Funcionario__nivel == 2:
            self.__salarioBruto = 2362.67
        elif self._Funcionario__nivel == 3:
            self.__salarioBruto = 2988.92
        elif self._Funcionario__nivel == 4:
            self.__salarioBruto = 3572.77
        elif self._Funcionario__nivel == 5:
            self.__salarioBruto = 4878.67
        # inss
        if self.__salarioBruto <= 1320:
            self.__inss = 0.075
        elif 1301.01 <= self.__salarioBruto <= 2571.29:
            self.__inss = 0.09
        elif 2571.30 <= self.__salarioBruto <= 3856.94:
            self.__inss = 0.12
        else:
            self.__inss = 0.14
        # irrf
        if self.__salarioBruto <= 2112:
            self.__irrf = 0
        elif 2112.01 <= self.__salarioBruto <= 2826.65:
            self.__irrf = 0.075
        elif 2826.66 <= self.__salarioBruto <= 3751.05:
            self.__irrf = 0.15
        elif 3751.06 <= self.__salarioBruto <= 4664.68:
            self.__irrf = 0.225
        else:
            self.__irrf = 0.275
        self.__salarioLiquido = self.__salarioBruto - (self.__salarioBruto * self.__inss) - (self.__salarioBruto * self.__irrf) - self.__planoSaude
        self.__plusSalario = (self.__salarioLiquido * self.__plusSalario) + self.__salarioLiquido
        return self.__plusSalario

    def exibirCoordenadorAdm(self):
        self.exibirFuncionario()
        print(f'Area: {self.__area}\nPlus Salario: {self.calcularPlusSalario():.2f}')

class Salario:
    def __init__(self, setor=str, cargo=str, nivel=int):
        self.__planoSaude = 125
        self.__setor = setor
        self.__cargo = cargo
        self.__nivel = nivel

    def calcularSalario(self):
        try:
            # Docente
            if self.__setor.lower() == 'docente':
                # Professor
                if self.__cargo.lower() == 'professor' or self.__cargo.lower() == 'coordenador':
                    if self.__nivel == 1:
                        self.__salarioBruto = 6500
                    elif self.__nivel == 2:
                        self.__salarioBruto = 8325.50
                    elif self.__nivel == 3:
                        self.__salarioBruto = 12568.43
            # Administrativo
            elif self.__setor.lower() == 'administrativo':
                # Coordenador ADM
                if self.__cargo.lower() == 'coordenador adm':
                    if self.__nivel == 1:
                        self.__salarioBruto = 1520.25
                    elif self.__nivel == 2:
                        self.__salarioBruto = 2362.67
                    elif self.__nivel == 3:
                        self.__salarioBruto = 2988.92
                    elif self.__nivel == 4:
                        self.__salarioBruto = 3572.77
                    elif self.__nivel == 5:
                        self.__salarioBruto = 4878.67
            # Atendimento
            elif self.__setor.lower() == 'atendimento':
                # Atendente
                if self.__cargo.lower() == 'atendente':
                    self.__salarioBruto = 1320
            # inss
            if self.__salarioBruto <= 1320:
                self.__inss = 0.075
            elif 1301.01 <= self.__salarioBruto <= 2571.29:
                self.__inss = 0.09
            elif 2571.30 <= self.__salarioBruto <= 3856.94:
                self.__inss = 0.12
            else:
                self.__inss = 0.14
            # irrf
            if self.__salarioBruto <= 2112:
                self.__irrf = 0
            elif 2112.01 <= self.__salarioBruto <= 2826.65:
                self.__irrf = 0.075
            elif 2826.66 <= self.__salarioBruto <= 3751.05:
                self.__irrf = 0.15
            elif 3751.06 <= self.__salarioBruto <= 4664.68:
                self.__irrf = 0.225
            else:
                self.__irrf = 0.275
            self.__salarioLiquido = self.__salarioBruto - (self.__salarioBruto * self.__inss) - (self.__salarioBruto * self.__irrf) - self.__planoSaude
            return self.__salarioLiquido
        except:
            print('Houve um erro, revise os dados informados.')
        
    def cadastrarSalario(self):
        df = pd.DataFrame([[self.calcularSalario()]])
        df.to_csv('Laboratorio de programacao\Estudo de Caso\FolhaSalarial.csv', header=False, index=False, sep=';', mode='a')

class Curso:
    def __init__(self, titulo=str, descricao=str, sala=str):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__valor = 865.23
        self.__sala = sala
    
    def cadastrarCurso(self):
        curso = [[self.__titulo, self.__descricao, self.__valor, self.__sala]]
        df = pd.DataFrame(curso, columns=['Titulo', 'Descricao', 'Valor', 'Sala'])
        try:
            pd.read_csv('Laboratorio de programacao\Estudo de Caso\Cursos.csv')
        except:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Cursos.csv', header=True, index=False, sep=',')
        else:
            df.to_csv('Laboratorio de programacao\Estudo de Caso\Cursos.csv', header=False, index=False, sep=',', mode='a')
    
    def exibirCurso(self):
        print(f'Titulo: {self.__titulo}\nDescricao: {self.__descricao}\nValor: {self.__valor}\nSala: {self.__sala}')
    
    def calcularNumMinAluno(self):
        try:
            folhaSalarial = pd.read_csv('Laboratorio de programacao\Estudo de Caso\FolhaSalarial.csv')
            total = float(folhaSalarial.sum())
            numMinAluno = total / self.__valor
            print(f'Número mínimo de alunos: {int(numMinAluno.__round__(0))}')
        except FileNotFoundError:
            print('Folha salarial não encontrada.')

if __name__ == '__main__':
    ana = Funcionario('Ana', '123456', '123456789', 1, 2, 2000, 'M', 152346, 'Atendimento', 'Atendente', 1)
    ana.cadastrarFuncionario()
    salarioAna = Salario('Atendimento', 'Atendente', 1)
    salarioAna.cadastrarSalario()

    maria = Funcionario('Maria', '123456', '123456789', 5, 3, 1986, 'M', 142653, 'Atendimento', 'Atendente', 1)
    maria.cadastrarFuncionario()
    salarioMaria = Salario('Atendimento', 'Atendente', 1)
    salarioMaria.cadastrarSalario()

    jose = Professor('Jose', '123456', '123456789', 31, 5, 1974, 'M', 126534, 1, 'Graduado', 'Mestrado', 'Programacao')
    jose.cadastrarProfessor()
    salarioJose = Salario('Docente', 'Professor', 1)
    salarioJose.cadastrarSalario()

    joao = Professor('Joao', '123456', '123456789', 23, 12, 1980, 'M', 126543, 2, 'Graduado', 'Douturado', 'Matematica')
    joao.cadastrarProfessor()
    salarioJoao = Salario('Docente', 'Professor', 2)
    salarioJoao.cadastrarSalario()

    nelson = Coordenador('Nelson', '12345678-9', '123.456.789-10', 1, 1, 1978, 'M', 132456, 3, 'Doutorado', 'Doutor', 'Banco de dados', 'TI')
    nelson.cadastrarCoordenador()
    salarioNelson = Salario('Docente', 'Coordenador', 3)
    salarioNelson.cadastrarSalario()

    lucas = CoordenadorAdm('Lucas', '123456789', '123456789-10', 5, 7, 1970, 'M', 162345, 5, 'TI')
    lucas.cadastrarCoordenadorAdm()
    salarioLucas = Salario('Administrativo', 'Coordenador Adm', 5)
    salarioLucas.cadastrarSalario()

    pedro = Aluno('Pedro', '123456789', '123456789-10', 6, 3, 2001, 'M', 123456, 'Sistemas de Informação', 0)
    pedro.cadastrarAluno()
    luana = Aluno('Luana', '123456789', '123456789-10', 12, 6, 2000, 'F', 654321, 'Sistemas de Informação', 0)
    luana.cadastrarAluno()

    matriculaPedro = Matricula('Pedro', '123456789', '123456789-10', 6, 3, 2001, 'M', 123456, 'Sistemas de Informação', 0, 632001, 1, 2023)
    matriculaPedro.matricular()
    matriculaLuana = Matricula('Luana', '123456789', '123456789-10', 12, 6, 2000, 'F', 654321, 'Sistemas de Informação', 0, 1262000, 1, 2023)
    matriculaLuana.matricular()

    curso = Curso('Sistemas de Informação', 'Curso de sistemas de informação', 'A32')
    curso.cadastrarCurso()
    curso.exibirCurso()
    curso.calcularNumMinAluno()