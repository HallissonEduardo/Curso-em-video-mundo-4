from rich import print, inspect

from poligono import Quadrado



def main():
    quadrado = Quadrado(5)

    print(quadrado.perimetro())  # 20
    print(quadrado.area())
    inspect(quadrado, methods= True)

if __name__ == '__main__':
    main()
