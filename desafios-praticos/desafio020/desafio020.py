class Jogos:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favorito(self, game ):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)


    def status(self)->str:
        mensagem = (f"Nome verdadeiro: {self.nome} \nNick name: {self.nick}\n"
                    f"-----Jogos favoritos------\n")
        for i, fav in enumerate(self.favoritos, start=1):
            mensagem += f"Favorito {i}: {fav}\n"

        return mensagem
