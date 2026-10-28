from aluno import Aluno
from professor import Professor
from funcionario import Funcionario
from rich import  inspect



def main():
    print("Classe Aluno\n")

    estudante = Aluno(nome="Hallisson",
               idade=24,
               curso="ADS",
               turma="T01")

    estudante.fazer_aniversario()
    print(estudante.fazer_matricula())
    print(estudante.estudar())

    print("----------------------------------------------")
    print("Classe Professor\n")

    colaborador_educador = Professor(nome="Wesley",
                   idade=37,
                   especialidade="ADS",
                   nivel="Superior")

    colaborador_educador.fazer_aniversario()
    print(colaborador_educador.dar_aula())
    print(colaborador_educador.estudar())

    print("----------------------------------------------------------")
    print("Classe funcionario\n")

    colaborador = Funcionario(nome="Gabriel Fernando",
                     idade=27,
                     cargo="Desenvolvedor junior",
                     setor="TI")

    colaborador.fazer_aniversario()
    print(colaborador.bater_ponto())
    print(colaborador.estudar())
    inspect(colaborador, methods=True)

if __name__ == '__main__':
    main()