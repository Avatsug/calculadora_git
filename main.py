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
    
# Clase para elevar/potenciar
class potenciacion:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def solucion(self):
        return self.numero_1 ** self.numero_2

# Función para elegir la operación a realizar
def elegirOperacion():
    print("Operaciones: 1. Suma / 2. Resta / 3. Multiplicación / 4. División / 5. Potenciación")
    tipoOperacion = float(input("Ingresa el número de la operación que quieres realizar: "))

    if tipoOperacion==1:
        numero_1 = float(input("Ingresa el primer número a sumar: "))
        numero_2 = float(input("Ingresa el segundo número a sumar: "))
        operacion = suma(numero_1, numero_2)

    elif tipoOperacion==2:
        numero_1 = float(input("Ingresa el primer número a restar: "))
        numero_2 = float(input("Ingresa el segundo número a restar: "))
        operacion = resta(numero_1, numero_2)

    elif tipoOperacion==3:
        numero_1 = float(input("Ingresa el número multiplicando: "))
        numero_2 = float(input("Ingresa el número multiplicador: "))
        operacion = multiplicacion(numero_1, numero_2)

    elif tipoOperacion==4:
        numero_1 = float(input("Ingresa el número dividendo: "))
        numero_2 = float(input("Ingresa el número divisor: "))
        operacion = division(numero_1, numero_2)
        
    elif tipoOperacion==5:
        numero_1 = float(input("Ingresa el número base: "))
        numero_2 = float(input("Ingresa el número exponente: "))
        operacion = potenciacion(numero_1, numero_2)

    else:
        print("Operación inválida")
        return
    
    decimalesDeseados = 2
    resultado = operacion.solucion()
    print(f'El resultado de tu operación es: {resultado: .{decimalesDeseados}f}')
    
# Ejecutar programa
elegirOperacion()