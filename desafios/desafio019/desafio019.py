class Livro:

    def __init__(self, titulo: str, paginas: int):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual: int = 1

    def __str__(self):
        return f"Voce esta lendo o livro: {self.titulo}"

    def passar_pagina(self, qtd: int = 1)-> int:
        nova_pagina = self.pagina_atual + qtd

        if nova_pagina <= self.total_paginas:
            self.pagina_atual = nova_pagina
        else:
            self.pagina_atual = self.total_paginas
        return self.pagina_atual

    def fim_do_livro(self)-> bool:
        return self.pagina_atual >= self.total_paginas


    def exibir(self)-> str:
        return (f"Voce abriu o livro {self.titulo} que tem \n"
                f"{self.total_paginas} paginas. Voce esta na pagina {self.pagina_atual}")


