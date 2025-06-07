from abc import ABC, abstractmethod
import math

# Clase abstracta
class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    def descripcion(self):
        return "Figura geométrica básica"

# Implementaciones concretas
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def descripcion(self):
        return f"Círculo de radio {self.radio}"

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def descripcion(self):
        return f"Rectángulo {self.base}x{self.altura}"

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        # Fórmula de Herón
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def descripcion(self):
        return f"Triángulo de lados {self.lado1}, {self.lado2}, {self.lado3}"

# Función que usa abstracción
def mostrar_info_figuras(figuras):
    for figura in figuras:
        print("\n" + figura.descripcion())
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")

# Uso
figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 4, 5)
]

mostrar_info_figuras(figuras)