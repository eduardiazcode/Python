# Scope
# Algunas personas pueden ir a cualquier habitacion (scope global)
# Otras personas pueden estar solo en su habitacion (scope local)

nombre = "Ana" # Variable global

def saludar():
    mensaje = "Hola" # Variaable local
    print(mensaje, nombre)

saludar()
print(nombre)

# ==============================================================
# Scope local
def mi_funcion():
    x = 10
    print("Dentro de la funcion: ", x) # Al tratar de impirmir dara error, porque solo esta dentro de la funcion

mi_funcion()

# ===============================================================
# Scope global

y = 15

def funcion1():
    print("En funcion de 1: ", y)

def funcion2():
    print("En funcion de 2: ", y)

funcion1()
funcion2()
print(y) # Scope global si se puede imprimir porque esta fuera de la funcion tiene alcance global

# ========================================================================
# Usar un variable global dentro de una funcion
contador = 0

def incrementar():
    global contador
    contador += 1
    print(f"Contador: {contador}")

incrementar()
incrementar()
incrementar()

print(contador)
# Se prefiere evitar hacer uso de variables globales
