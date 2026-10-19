from rich import print
from rich.panel import Panel

class ControleRemoto:
    """
        Simulação de Controle Remoto de TV
    """
    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal: int = 1, volume: int = 1):
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False


    def ligar_desligar(self)-> bool:
        self.ligado = not self.ligado
        return self.ligado

    def mudar_canal(self, novo_canal: int)-> int:

        if self.ligado and self.canal_min <= novo_canal <= self.canal_max:
            self.canal_atual =  novo_canal
        return self.canal_atual

    def mudar_volume(self, subir: bool = True)-> int:

        if self.ligado:
            if subir and self.volume_atual < self.volume_max:
                self.volume_atual += 1

            elif not subir and self.volume_atual > self.volume_min:
                self.volume_atual -= 1
        return self.volume_atual

    def mostrar_tv(self)-> None:

        if not self.ligado:
            conteudo = f"[bold red] A TV está desligada[/]"
            painel = Panel(conteudo, title="TV DESLIGADA", expand=False)

        else:

            barra_vol = "-" * self.volume_atual + "|"  * (self.volume_max - self.volume_atual)

            conteudo = (
                f"[bold green]> Assistindo: [/] Canal: {self.canal_atual}\n"
                f"[bold blue]> Volume: {barra_vol}({self.volume_atual})"
            )

            painel = Panel(conteudo, title="TV LIGADA", expand=False)

        print(painel)

