# print 
# Es la función más básica al usar Python

print("Hola mundo")

# Variables:
# Es un contenedor para guardar datos

saludos = "Hola a todos"
print(saludos)

# Un variable jamás debe empezar con un numero

number1 = 30
print(number1)

# Una forma más practica de asignar el mismo valor a diferentes variables
number1 = number2 = number3 = number4 = 50
print(number4)
print(number3)
print(number2)
print(number1)

# Ahora veamos el siguiente caso de asignar valores a dos variables
saludo1, saludo2 = "Hola", "Mundo"
print(saludo1) # saludo1 tomo el valor que esta antes de la coma
print(saludo2) # saludo2 toma el valor despues de la coma

# Ahora si queremos saber el tido de dato que tenemos se hace de la siguiente forma:
numero = 2
print(type(numero)) # es un tipo de variable (int) entero

mensaje = "probando"
print(type(mensaje)) # esun tipo de dato (str) string o cadena de texto

valor = True
print(valor) # es un tipo de dato (bool) booleano estos son verdadero o falso

# import os # importar sistema operativo

# FORMAS DE CREAR VARIABLES
var_name = "snake_case" # lo que esta en comillas son los nombres del tipo de creación de variable
Var_Name = "pascal_case"
var_Name = "camel_case"