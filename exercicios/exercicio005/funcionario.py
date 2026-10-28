from pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self)-> str:
        return f"O {self.nome} bateu o ponto!!"

    def estudar(self)-> str:
        return f" {self.nome} Acabou de iniciar seus estudos para o concurso."