# ARGS : El asterisco * permite recibir cualquier cantidad de argumentos posicionales en una tupla
# Cuando no sabes cuántos argumentos recibirás. Por convención se usa el nombre args,

def sumar_todo(*numeros):
    print(f"Recibi {numeros}")
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todo(1, 2, 3, 4, 5))
print(sumar_todo(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
print(sumar_todo(5, 4, 3))

def crear_palabras(*palabras):
    return ", ".join(palabras)
# join: es un metodo de los string que une los elementos de una tupla o lista con un string

print(crear_palabras("hola", "mundo", "python"))
print(crear_palabras("amigo", "como", "estas"))

# ==================================================================
# KARGS : El doble asterisco ** permite recibir cualquier cantidad de argumentos por nombre en un diccionario
# Significa keyword arguments (argumentos con palabra clave)

# args empaqueta en una tupla (sin nombre)
def funcion1(*args):
    print(args)

funcion1(1, 2, 3, 4, 5)

# **kargs empaqueta en un diccionario (con nombre)

def funcion2(**kwargs):
    print(kwargs)

funcion2(a=1, b=2, c=3)

def mostrar_datos(**kwargs):
    print(kwargs)
    print(type(kwargs))

mostrar_datos(nombre = "Eduardo", apellido = "Rios", edad = 30)

# =================================================================
def crear_perfil(**datos):
    print("=== PERFIL DE USUARIO ===")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

crear_perfil(nombre = "Eduardo")
crear_perfil(Nombre = "Maria", Edad = 34, Apeliido = "Salazar")
print()

