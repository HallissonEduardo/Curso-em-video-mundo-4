from aluno import Aluno
from professor import Professor
from funcionario import Funcionario
from rich import  inspect


def main():
    aluno = Aluno(nome="Hallisson",
               idade=24,
               curso="ADS",
               turma="T01")

    aluno.fazer_aniversario()
    print(aluno.fazer_matricula())
    # inspect(aluno)

    print("----------------------------------------------------------")

    educador = Professor(nome="Rafael",
                   idade=37,
                   especialidade="ADS",
                   nivel="Pós Graduado")

    educador.fazer_aniversario()
    print(educador.dar_aula())
    # inspect(educador)

    print("----------------------------------------------------------")

    colaborador = Funcionario(nome="Thiago",
                     idade=40,
                     cargo="Desenvolvedor",
                     setor="TI")

    colaborador.fazer_aniversario()
    print(colaborador.bater_ponto())
    inspect(colaborador, methods=True)


if __name__ == '__main__':
    main()



