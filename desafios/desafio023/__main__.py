
from rich import print, inspect
from poligono import Quadrado, Circulo


def main() -> None:

    q1 = Quadrado(12)

    print(f"Um quadrado de lado {q1.lado} tem perímetro de {q1.perimetro()}mm")
    print(f"Um quadrado de lado {q1.lado} tem área de {q1.area()}mm")
    inspect(q1, methods=True)

    c1 = Circulo()
    print(f"Um círculo de {c1.raio}cm tem perímetro de {c1.perimetro():.2f}cm")
    print(f"Um círculo de {c1.raio}cm tem área de {c1.area():.2f}cm")


if __name__ == '__main__':
    main()