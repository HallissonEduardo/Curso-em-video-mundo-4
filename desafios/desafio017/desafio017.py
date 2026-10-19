from dataclasses import dataclass

class Produto:

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco


    def exibir(self)-> str:
        return f"Produto disponivel: {self.nome} valor: R${self.preco:.2f}"


@dataclass
class produto:
    nome: str
    preco: float

    def __str__(self):
        return f"Produto disponivel: {self.nome} valor: R${self.preco:.2f}"


