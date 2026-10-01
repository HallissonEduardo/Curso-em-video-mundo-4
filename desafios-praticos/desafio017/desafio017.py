from dataclasses import dataclass

class Produto:

    def __init__(self, nome, preco):
        self.nome: str = nome
        self.preco: float = preco


    def exibir(self):
        return f"Produto disponivel: {self.nome} valor: R${self.preco:.2f}"

@dataclass
class produto:
    nome: str
    preco: float

    def __str__(self):
        return f"Produto disponivel: {self.nome} valor: R${self.preco:.2f}"


