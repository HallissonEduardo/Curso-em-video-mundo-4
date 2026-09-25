class Gafanoto:
    def __init__(self):
        self.nome: str = ''
        self.idade: int = 0

    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos"


if __name__ == '__main__':
    g1 = Gafanoto()
    g1.nome = "Hallisson"
    g1.idade = 23
    g1.aniversario()
    print(g1.mensagem())


    g2 = Gafanoto()
    g2.nome = "Brenno"
    g2.idade = 21
    g2.aniversario()
    print(g2.mensagem())