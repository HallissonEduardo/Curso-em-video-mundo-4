class Gafanhoto:

    """
    curso em video
    """

    def __init__(self, nome, idade): # Se eu não atribuir valor ao paremetro nome e idade,

        # eles serão cobrados na criação da classe
        self.nome: str = nome
        self.idade: int = idade

    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos"


class gafanhoto(Gafanhoto):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade}anos"

    def __getstate(self):
        return f"estado nome = {self.nome} \n idade = { self.idade}"



if __name__ == '__main__':
    g1 = Gafanhoto(nome = "Hallisson",
                  idade = 23)
    g1.aniversario()
    print(g1.mensagem())

    print(g1.__doc__)#DOCSTRING
    print(g1.__dict__)
    print(g1.__getstate__())
    print(g1.__class__)
    


    g2 = Gafanhoto(nome = "Brenno",
                  idade= 21
                  )

    g2.nome = "Brenno"
    print(g2.mensagem())
    print(g2.__doc__)# DUNDER ATTRIBUTE




    g3 = Gafanhoto(nome = "Huander",
                  idade = 30
                  )
    g3.nome = "Huander Pires"
    g3.idade = 31 # O VALOR É FLEXIVEL.
    print(g3.mensagem())

    print(g3)




    g1 = gafanhoto(nome = "Cupim",
                  idade = 28
                  )
    g1.aniversario()

    print(g1)

