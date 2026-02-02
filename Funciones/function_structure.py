# Una función es un bloque de código reutilizable que realiza una tarea específica. 
# Es como una "mini-máquina" que puedes usar muchas veces sin tener que escribir el mismo código repetidamente.

# ANALOGIA
# Imagina un licuadora
# - Le das ingredientes (entrada)
# - Presionas un boton (ejecutas la funcion)
# - Obtienes un batido (salida)

# def : palabra clave para definir un funcion
# saludar: es el nombre que se le pone a la funcion en este caso saludar
# parametros: lo ingredientes que necesita

def saludar():
    print("Hola, como estas")

saludar()

# ======================================================================
# Ejemplo 2
def saludar(nombre):
    print(f"Hola como estas,{nombre}")

saludar("Armando")
saludar("Alexis")
saludar("Freddy")

# =======================================================================
def sumar(a, b):
    resultado = a + b
    return resultado

mi_resultado = sumar(5, 16)
print(f"El resultado de la suma es: {mi_resultado}")

print(sumar(4, 8))

# ========================================================================
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

print(calcular_area_rectangulo(10, 5))
print(calcular_area_rectangulo(7, 6))

# =========================================================================
# Ejemplo para entender con se usa return
def hacer_jugo_malo():
    print("Aqui esta tu fugo de naranja")
    # Aqui te muestra el JUGO pero no te lo da

hacer_jugo_malo()
# Aqui ves el mensaje del jugo pero no puedes llevartelo

# AHORA HAREMOS EL USO DE RETURN
def hacer_jugo_bueno():
    return "Jugo de naranja"
    # Aqui el vendedor te entrega el jugo de naranja

mi_jugo = hacer_jugo_bueno
# Ahora SÍ tienes el jugo en tu mano (en la variable)
print(mi_jugo)  # Puedes beberlo, guardarlo, compartirlo

# =================================================================
def fibonacci_simple(n):
    """
    Devuelve el numero de fibonacci en la posicion n
    n: la posicion que queremos (0,1,2,3,4,...)
    """
    # Para los dos primeros numeros
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    # Para cuaquier numero otro numero; sumaremos los dos anteriores
    # fibonaccci(n) = fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci_simple(n-1) + fibonacci_simple(n-2)
    
print("Posicion 0: ", fibonacci_simple(0))
print("Posicion 1: ", fibonacci_simple(1))
print("Posicion 2: ", fibonacci_simple(2))
print("Posicion 3: ", fibonacci_simple(3))
print("Posicion 4: ", fibonacci_simple(4))
def fibonacci_simple(n):
    """
    Devuelve el numero de fibonacci en la posicion n
    n: la posicion que queremos (0,1,2,3,4,...)
    """
    # Para los dos primeros numeros
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    # Para cuaquier numero otro numero; sumaremos los dos anteriores
    # fibonaccci(n) = fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci_simple(n-1) + fibonacci_simple(n-2)
    
print("Posicion 0: ", fibonacci_simple(0))
print("Posicion 1: ", fibonacci_simple(1))
print("Posicion 2: ", fibonacci_simple(2))
print("Posicion 3: ", fibonacci_simple(3))
print("Posicion 4: ", fibonacci_simple(4))
print("Posicion 5: ", fibonacci_simple(5))
