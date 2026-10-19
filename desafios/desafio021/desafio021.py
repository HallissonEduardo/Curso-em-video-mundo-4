from rich.console import Console

console = Console(force_terminal=True)

class Caneta:

    def __init__(self, cor="azul"):

        match cor.lower().strip():
            case "azul":
                self.escolha = "[blue]"

            case "preta" | "preto":
                self.escolha = "[black]"

            case "vermelho" | "vermelha":
                self.escolha = "[red]"

            case "verde":
                self.escolha = "[green]"

            case _:
                self.escolha = "[white]"

        self.cor = cor
        self.tampada = True


    def leia(self, pergunta)-> str:
        if self.tampada:
            console.print("[bold red]Erro: Não da para usar a caneta tampada")
            return ""

        resposta = console.input(f"{self.escolha}{pergunta}[/]")
        return resposta


    def escreva(self, msg)-> None:
        if self.tampada:
            console.print("[bold red]Erro:[/] Não dá para escrever com a caneta tampada!")
        else:
            console.print(f"{self.escolha}{msg}[/]", end="")

    def quebrar_linha(self)-> None:
        console.print()

    def tampar_destampar(self)-> bool:
        self.tampada = not self.tampada
        return self.tampada

