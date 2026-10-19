class Gafanoto:
    def __init__(self):
        self.nome: str = ''
        self.idade: int = 0

    def aniversario(self)-> int:
        self.idade += 1
        return self.idade


    def mensagem(self)-> str:
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos"


