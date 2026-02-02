# Breack rompe (cancela el bucle)
# Continue permmite saltar a la siguiente posicion
# else ejecuta una porcion del codigo cuando termina el ciclo


# Break: Romper/detener el bucle

for i in range(1, 10):
    print(i)
    if i == 5: # cuando llegue el bucle a 5 se detendra el ciclo
        break

while True:
    respuesta = input("¿Quieres salir? (si/no): ")
    if respuesta == "si":
        break
    print("Continuamos...")
    
print("¡Adiós!")

numeros = [1, 5, 8, 12 , 15, 20]

for num in numeros:
    if num > 10:
        print(f"Encontre el numero mayor a 10: {num}")
        break
    print("Revisando: {num}")

# =================================================================================
for i in range (1,10):
    if i == 5: # Se detiene al llegar a 6
        break
    print(i)

# =================================================================================
# Continue: Continue no detiene el bucle, ignora el resto del codigo y salta al siguiente
# salta el resto del codigo en esa iteracion y pasa al siguiente
frutas = ["manzana", "pera", "chirimoya", "platano", "sandia"]

for x in frutas:
    if x == "chirimoya":
        continue
    print("La frutas es: ", x )


for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)
     # Si es par


variables = [5, -3, 8, -1, 12, -7, 20]

suma = 0
for variable in variables:
    if variable % 2 ==0:
        continue
    suma += variable

print(f"La suma de los numeros impares es: {suma}")

frutas = ["manzana", "papaya", "lima"]
verdura = ["espinaca", "repollo", "tomate"]

for mixto in (frutas, verdura):
    if mixto == verdura:
        continue
    print(f"Estas son las ricas frutas: {frutas}")
# ==================================================================================
# ELse : en un bucle se ejecuta SOLO si el bucle terminó normalmente, es decir, SIN usar break.
