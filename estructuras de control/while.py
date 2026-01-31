# Bucle o ciclo
# Ejecuta código de forma repetitiva mientra un condición se cumpla
# Tambien debe dar como resultado True
# While se ejecutara mientras sea verdadero, se repite
number = 0
while 10 > number:
    print("Hola mundo " + str(number))
    number += 2

# Ejemplos 
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
# =====================================================================
password = ""
while password != "1234":
    password = input("Ingresa la contraseña: ")
    
print("¡Contraseña correcta!")
# =====================================================================
suma = 0
numero = 1

while suma < 100:
    suma += numero
    numero += 1
    
print("La suma llegó a:", suma)