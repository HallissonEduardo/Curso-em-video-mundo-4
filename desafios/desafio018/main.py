from desafio018 import Churrasco

if __name__ == '__main__':
    c = Churrasco("Churrasco com amigos",
                  10,
                  "Avenida das castanheiras, Proximo ao Mcdonald's"
                  )


    print(c.analisar())

    print("-" * 60)

    c1 = Churrasco("Churrasco da Familia",
                   21
                   )

    print(c1.analisar())