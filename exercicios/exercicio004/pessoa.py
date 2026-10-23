
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self) -> int:
        self.idade += 1
        return self.idade