from aluno import Aluno
from professor import Professor
from funcionario import Funcionario
from rich import  inspect


def main():
    aluno = Aluno(nome="Hallisson",
               idade=17,
               curso="ADS",
               turma="T01")

    aluno.fazer_aniversario()
    print(aluno.fazer_matricula())
    # inspect(aluno)

    print("----------------------------------------------------------")

    educador = Professor(nome="Fabio",
                   idade=37,
                   especialidade="Ciência da computação",
                   nivel="Mestrado")

    educador.fazer_aniversario()
    print(educador.dar_aula())
    # inspect(educador)

    print("----------------------------------------------------------")

    colaborador = Funcionario(nome="Gabriel Fernando",
                     idade=27,
                     cargo="Desenvolvedor junior",
                     setor="TI")

    colaborador.fazer_aniversario()
    print(colaborador.bater_ponto())
    inspect(colaborador, methods=True)


if __name__ == '__main__':
    main()



