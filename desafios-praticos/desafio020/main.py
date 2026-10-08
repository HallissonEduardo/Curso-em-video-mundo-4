from desafio020 import Jogos


if __name__ == '__main__':
    P1 = Jogos("Hallisson",
               "Red")
    P1.add_favorito("Rimworld")
    P1.add_favorito("Castlevania")
    P1.add_favorito("Zelda")
    print(P1.status())