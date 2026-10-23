from aluno import Aluno
from professor import Professor
from funcionario import Funcionario
from rich import  inspect

if __name__ == '__main__':
    a1 = Aluno(nome="Hallisson",
                  idade=17,
                  curso="ADS",
                  turma="T01")

    a1.fazer_aniversario()
    print(a1.fazer_matricula())
    #inspect(a1)

    print("----------------------------------------------------------")

    p1 = Professor(nome="Fabio",
                    idade=37,
                    especialidade="Ciência da computação",
                    nivel="Mestrado")

    p1.fazer_aniversario()
    print(p1.dar_aula())
    #inspect(p1)

    print("----------------------------------------------------------")


    f1 = Funcionario(nome="Gabriel Fernando",
                     idade=27,
                     cargo="Desenvolvedor junior",
                     setor="TI")
    f1.fazer_aniversario()
    print(f1.bater_ponto())
    inspect(f1, methods=True)