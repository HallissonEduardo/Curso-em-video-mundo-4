class Funcionario:
    def __init__(self, nome: str, setor: str, cargo: str):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentar(self)-> str:
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Curso em video."