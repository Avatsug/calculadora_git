# Curso: Backend Python / Calculadora Git / Gustavo Aparicio
import math 

# Clases para cada operación
# Clase para sumar
class suma:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def solucion(self):
        return self.numero_1 + self.numero_2

# Clase para restar   
class resta:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def solucion(self):
        return self.numero_1 - self.numero_2
    
# Clase para multiplicar
class multiplicacion:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def solucion(self):
        return self.numero_1 * self.numero_2

# Clase para dividir   
class division:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def solucion(self):
        return self.numero_1 // self.numero_2