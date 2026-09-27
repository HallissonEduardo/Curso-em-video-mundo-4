from exercicio02 import Gafanhoto, gafanhoto




if __name__ == '__main__':
    g1 = Gafanhoto(nome="Hallisson",
                   idade=23)
    g1.aniversario()
    print(g1.mensagem())

    # print(g1.__doc__)#DOCSTRING
    # print(g1.__dict__)
    # print(g1.__getstate__())
    print(g1.__class__)

    g2 = Gafanhoto(nome="Brenno",
                   idade=21
                   )

    g2.nome = "Brenno"
    print(g2.mensagem())
    print(g2.__doc__)  # DUNDER ATTRIBUTE

    g3 = Gafanhoto(nome="Huander",
                   idade=30
                   )
    g3.nome = "Huander Pires"
    g3.idade = 31
    print(g3.mensagem())

    print(g3)

    g1 = gafanhoto(nome="Cupim",
                   idade=28
                   )
    g1.aniversario()

    print(g1)
