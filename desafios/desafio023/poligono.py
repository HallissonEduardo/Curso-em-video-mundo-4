from abc import ABC, abstractmethod
import math


class Poligono(ABC):

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):

    def __init__(self, lado: float = 1):

        if lado <= 0:
            raise ValueError("O lado do quadrado deve ser maior que zero.")
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):

    def __init__(self, raio: float = 1):

        if raio <= 0:
            raise ValueError("O raio do círculo deve ser maior que zero.")
        self.raio = raio


    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * (self.raio ** 2)