import professor, pandas as pd
Professor = professor.Professor

class Curso(Professor):
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
    curso = Curso('Python', 'Curso de Python', 'A32')
    curso.cadastrarCurso()
    curso.calcularNumMinAluno()
