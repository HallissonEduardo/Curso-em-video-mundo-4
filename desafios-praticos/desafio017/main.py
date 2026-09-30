from desafio017 import Produto, produto

if __name__ == '__main__':
    p1 = Produto(nome = "Iphone 11",
                 preco = 2200)

    print(p1.exibir())

    p2 = produto(nome = "Smartphone",
                 preco = 2500)

    print(p2)