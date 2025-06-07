class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0
    
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"Acelerando a {self.velocidad} km/h")
    
    def mostrar_info(self):
        print(f"{self.marca} {self.modelo} ({self.color})")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, puertas):
        super().__init__(marca, modelo, color)
        self.puertas = puertas
    
    def abrir_puertas(self):
        print(f"Abriendo {self.puertas} puertas")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: Coche | Puertas: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada
    
    def hacer_caballito(self):
        print("¡Haciendo caballito!")
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: Motocicleta | Cilindrada: {self.cilindrada}cc")

# Uso
mi_coche = Coche("Toyota", "Corolla", "Rojo", 4)
mi_moto = Moto("Honda", "CBR600", "Negro", 600)

mi_coche.mostrar_info()
mi_coche.acelerar(30)
mi_coche.abrir_puertas()

print("\n")

mi_moto.mostrar_info()
mi_moto.acelerar(50)
mi_moto.hacer_caballito()