from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):

    def __init__(self, lado=1):
        super().__init__()
        self.lado = lado
    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2





