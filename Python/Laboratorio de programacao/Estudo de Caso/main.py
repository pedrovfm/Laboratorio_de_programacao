from pessoa import Pessoa
from funcionario import Funcionario
from professor import Professor
from coordenador import Coordenador
from coordenadorAdm import CoordenadorAdm
from salario import Salario
from curso import Curso

if __name__ == '__main__':
    ana = Funcionario('Ana', '123456', '123456789', 1, 1, 2000, 'M', 123, 'Atendimento', 'Atendente', 1)
    ana.cadastrarFuncionario()
    salarioAna = Salario('Atendimento', 'Atendente', 1)
    salarioAna.cadastrarSalario()

    maria = Funcionario('Maria', '123456', '123456789', 1, 1, 2000, 'M', 123, 'Atendimento', 'Atendente', 1)
    maria.cadastrarFuncionario()
    salarioMaria = Salario('Atendimento', 'Atendente', 1)
    salarioMaria.cadastrarSalario()

    jose = Professor('Jose', '123456', '123456789', 1, 1, 2000, 'M', 123, 1, 'Graduado', 'Mestrado', 'Programacao')
    jose.cadastrarProfessor()
    salarioJose = Salario('Docente', 'Professor', 1)
    salarioJose.cadastrarSalario()

    joao = Professor('Joao', '123456', '123456789', 1, 1, 2000, 'M', 123, 2, 'Graduado', 'Douturado', 'Matematica')
    joao.cadastrarProfessor()
    salarioJoao = Salario('Docente', 'Professor', 2)
    salarioJoao.cadastrarSalario()

    nelson = Coordenador('Nelson', '12345678-9', '123.456.789-10', 1, 1, 2000, 'M', 123456, 3, 'Doutorado', 'Doutor', 'Banco de dados', 'TI')
    nelson.cadastrarCoordenador()
    salarioNelson = Salario('Docente', 'Coordenador', 3)
    salarioNelson.cadastrarSalario()

    lucas = CoordenadorAdm('Lucas', '123456789', '123456789-10', 1, 1, 2000, 'M', 123456, 5, 'TI')
    lucas.cadastrarCoordenadorAdm()
    salarioLucas = Salario('Administrativo', 'Coordenador Adm', 5)
    salarioLucas.cadastrarSalario()

    curso = Curso('Sistemas de Informação', 'Curso de sistemas de informação', 'A32')
    curso.cadastrarCurso()
    curso.exibirCurso()
    curso.calcularNumMinAluno()