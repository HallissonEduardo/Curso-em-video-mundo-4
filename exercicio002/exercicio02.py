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




