import random
import math
from abc import ABC, abstractmethod

class Coloreado:
    def como_colorear(self):
        raise NotImplementedError("Debe implementar como_colorear()")

class Figura(ABC):
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def como_colorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado - {super().__str__()}, Lado: {self.lado}"

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo - {super().__str__()}, Radio: {self.radio}"

def main():
    figuras = []
    colores = ["Rojo", "Verde", "Azul", "Amarillo", "Negro"]

    for _ in range(5):
        tipo = random.randint(1, 2)  
        color = random.choice(colores)

        if tipo == 1:
            lado = random.randint(1, 10)
            figura = Cuadrado(color, lado)
        else:
            radio = random.randint(1, 10)
            figura = Circulo(color, radio)

        figuras.append(figura)

    for f in figuras:
        print(f)
        print(f"Área: {f.area():.2f}")
        print(f"Perímetro: {f.perimetro():.2f}")
        if isinstance(f, Coloreado):
            print("Cómo colorear:", f.como_colorear())
        print("#######################################")

if __name__ == "__main__":
    main()
