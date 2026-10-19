from desafio019 import Livro

if __name__ == '__main__':

    l = Livro("10 Coisas que aprendi",
                85)

    l.passar_pagina(12)
    print(l)
    print(l.exibir())


    print("-" * 40)

    l1 = Livro("Clean code",
               456)

    l1.passar_pagina(458)
    print(l1.exibir())