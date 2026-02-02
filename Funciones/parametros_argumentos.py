# Parametros y argumentos
# Parametros son variables que se definen cuando creamos la funcion (en la definicion)
# Argumentos son los valores que se pasan cuando llamamos a la funcion

def saludar(nombre):
    print(f"Hola {nombre}!")

saludar("Ana")
# Sirve para reutilizar las misma funcion con diferentes valores
# ==================================================================
def sumar(a, b):
    resultado = a + b
    print(f"La suma de {a} + {b} es {resultado}")
    return resultado

sumar(10, 20)

# Python asigna los argumentos a los parámetros por posición: 
# el primer argumento va al primer parámetro, el segundo al segundo, etc.

# ==================================================================
def presentar(nombre, edad, apellido):
    print(f"Hola {nombre} {apellido}, tienes {edad} años")

presentar("Ana", 30, "Garcia")
presentar("Juan", 25, "Perez")
presentar("Pedro", 40, "Gonzalez")

# ==================================================================
def hacer_cafe(tipo="americano", azucar=False, leche=False):
    print(f"Haciendo un cafe de {tipo}")

    if azucar:
        print("Añadiendo azucar")
    if leche:
        print("Añadiendo leche")

hacer_cafe()
hacer_cafe("capuchino", True, True)
hacer_cafe("expresso", True)

# Los parámetros con valores por defecto deben ir DESPUÉS de los parámetros sin valores por defecto.

