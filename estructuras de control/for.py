# Bucle o ciclo for
# Genera codigo repetitivo similar a While

for i in range (6): # crea una secuencia de numeros 1,2,3,4,5,6
    print(i)
# PRIMERA VUELTA
# Empieza en 0 y termina en 5, el 6 NO SE INCLUYE
# i = 0 tomar el primer numero de la secuencia
# print (i=0) Imprime 0

# SEGUNDA VUELTA
# i = 1  toma el segundo numero
# print (i=1) Imprime 1

# TERCERA VUELTA
# i = 2 toma el tercer numero
# print (i=2) Imprime 2
# Se detendra cuando llegue al 5, el bucle ha terminado

for x in range (3):
    print("Hola mundo")

# =========================================
suma = 0
for numero in range(1, 11):
    suma += numero

print("La suma es:", suma)

nombres = ["Andres", "Victor", "Carlos"]
for nombre in nombres:
    print("Hola", nombre)

abecedario = ["A","B","C","D","E","F"]
for y in abecedario:
    print(y)

for number in range(2, 77, 5):
    print(number)

numero = input("Ingrese un numero: ")
for n in range(1, int(numero), 4):
    print(n)

programacion = ["Java", "C++", "hTML", "CSS", "Python"]
for lenguaje in programacion:
    if lenguaje == "Python":
        print("El mejor lenguaje es " + lenguaje)