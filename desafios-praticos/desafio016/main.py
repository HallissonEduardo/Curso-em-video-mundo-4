from desafio016 import Funcionario


if __name__ == "__main__":

    c1 = Funcionario(nome = "Maria",
                     setor = "Administração",
                     cargo = "Diretor")
    print(c1.apresentar())


    c2 = Funcionario(nome = "Hallisson",
                     setor = "TI",
                     cargo = "Desenvolvedor Junior")

    print(c2.apresentar())
