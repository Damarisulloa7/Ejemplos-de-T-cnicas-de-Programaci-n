class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base

class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas):
        super().__init__(nombre, salario_base)
        self.ventas = ventas
    
    def calcular_salario(self):
        return self.salario_base + (self.ventas * 0.1)

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono
    
    def calcular_salario(self):
        return self.salario_base + self.bono

# Función polimórfica
def mostrar_salarios(empleados):
    for emp in empleados:
        print(f"{emp.nombre}: ${emp.calcular_salario():.2f}")

# Uso
empleados = [
    Empleado("Ana", 1500),
    Vendedor("Carlos", 1200, 5000),
    Gerente("María", 3000, 800)
]

mostrar_salarios(empleados)