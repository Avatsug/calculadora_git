# Calculadora en Python
## Introducción
Calculadora simple que realiza operaciones básicas como suma, resta, multiplicación, división y potenciación; creada en Python, con commits en cada operación para facilitar y estructurar la creación del código. 
## Funcionamiento
Se puede explicar el funcionamiento de esta calculadora con los siguientes pasos:

1\. **Ejercutar el programa y elegir operación**: se ejecuta el programa y en pantalla aparece un texto donde define el número que representa cada operación; también aparece una entrada de dato donde se tendrá que digitar el número de la operación que se quiere realizar.

2\. **Seleccionar valores/números de la operación**: luego de definir la operación, se tendrá que digitar los valores de esta; aparecerá un texto y una entrada de dato para introducir el primer valor; este proceso se repite para el segundo valor.

3\. **Resultado**: al introducir los dos valores que se piden, se tendrá el resultado de la operación deseada.

4\. **Realizar otra operación**: si se quiere realizar otra operación, se tendrá que ejecutar de nuevo el programa y el proceso será el mismo.

## Partes del código
El por qué de cada parte del código:

1\. **Definición de clases para cada operación**: en el código se definen clases para cada tipo de operación matemática; cada clase tiene un constructor '__init__' que toma dos números como argumentos y guarda esos números en atributos (self.numero_1 y self.numero_2); cada clase también tiene un método 'solucion' que realiza la operación respectiva y devuelve el resultado. 

2\. **Función 'elegirOperacion'**: esta función es la parte principal del programa y maneja la interacción con el usuario; primero, muestra un menú de opciones para las operaciones disponibles: suma, resta, multiplicación, división y potenciación; luego, solicita al usuario que ingrese el número correspondiente a la operación que desea realizar, dependiendo de la elección del usuario, la función solicita los números necesarios para esa operación y crea una instancia de la clase correspondiente (por ejemplo, suma, resta, etc.) con los números proporcionados; por último, se muestra el resultado de la operación con un número específico de decimales, que se define con la variable 'decimalesDeseados'.

## Conclusiones
La creación de este programa impulsó la práctica de conocimientos en Python (funciones y clases) y conocimientos en Git y Git Hub (repositorios y commits), con la excusa de proporcionar soluciones a operaciones matemáticas básicas.
