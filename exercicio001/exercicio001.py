class Gafanoto:
    def __init__(self):
        self.nome: str = ''
        self.idade: int = 0

    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos"


