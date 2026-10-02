

class Churrasco:

    consumo_padrao: float = 0.400
    preco_kg: float = 82.40

    def __init__(self, titulo, qtd_pessoas, local: str ="Não tem local definido."):
        self.titulo: str = titulo
        self.qtd_pessoas: int = qtd_pessoas
        self._local = local

    def calcular_qtd_carne(self)-> float:
        return self.qtd_pessoas * Churrasco.consumo_padrao

    def calcular_custo_total(self)-> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg


    def calcular_custo_individual(self)-> float:
        return self.calcular_custo_total() / self.qtd_pessoas


    def localizar(self, _local)->str:
        return self._local

    def analisar(self)-> str:
        return (f"Analisando {self.titulo} com {self.qtd_pessoas} pessoas\n"
                f"Quantidade recomendada de carne: {self.calcular_qtd_carne():.1f}/Kg\n"
                f"Cada participante comerá {Churrasco.consumo_padrao:.1f}Kg\n"
                f"Custo por Kg: R${Churrasco.preco_kg:,.2f}\n"
                f"Custo individual: {self.calcular_custo_individual():.2f}\n"
                f"Custo total: R${self.calcular_custo_total():,.2f}\n"
                f"local: {self._local}"
                )



    def __str__(self):
        return f"Esse é `{self.titulo}` com {self.qtd_pessoas} pessoas participando"

# Consumo padrão: 400g por pessoa
# Preço: R$82,40/Kg



