# ==========================================
# MANEJO DE CADENAS DE TEXTO (STRINGS)
# ==========================================

name = "Eduardo"
print(name)  # Resultado: Eduardo

last_name = "Diaz"

# Concatenación simple (No guarda el resultado en la variable)
print(name + " " + last_name)  # Resultado: Eduardo Diaz

# f-strings: La mejor forma de mezclar variables y texto
print(f"{name} {last_name}")  # Resultado: Eduardo Diaz

# Operador de asignación compuesta: Concatena y actualiza el valor
name += " Mollocondo" # Tambien es conocido como acumulador
print(name)  # Resultado: Eduardo Mollocondo


# ==========================================
# OPERACIONES MATEMÁTICAS BÁSICAS
# ==========================================

number1 = 10
number2 = 20

result = number1 + number2   # Suma: 10 + 20
print(f"Suma: {result}")      # Resultado: 30

result = number1 - number2   # Resta: 10 - 20
print(f"Resta: {result}")     # Resultado: -10

result = number1 * number2   # Multiplicación: 10 * 20
print(f"Multiplicación: {result}") # Resultado: 200

result = number1 / number2   # División: 10 / 20 (Siempre devuelve decimal)
print(f"División: {result}")   # Resultado: 0.5

result = number1 % number2   # Módulo: Residuo de la división 10 / 20
print(f"Módulo: {result}")     # Resultado: 10
# Si tienes una operacion A % B:
#   Si A < B, el resultado siempre serra A

result = number1 ** 2        # Potencia: 10 elevado al cuadrado
print(f"Potencia: {result}")   # Resultado: 100

result = 10 // 3             # División Entera: Descarta los decimales
print(f"División Entera: {result}") # Resultado: 3


# ==========================================
# OPERADORES DE ASIGNACIÓN (ACTUALIZAR VALORES)
# ==========================================

number1 = 10

# Incremento: Suma y guarda el nuevo valor
number1 += 3    # Es como: number1 = 10 + 3
print(f"Incremento: {number1}")  # Resultado: 13

# Decremento: Resta y guarda el nuevo valor
number1 -= 3    # Es como: number1 = 13 - 3
print(f"Decremento: {number1}")  # Resultado: 10

# Multiplicación acumulativa
number1 *= 3    # Es como: number1 = 10 * 3
print(f"Multiplicación: {number1}") # Resultado: 30

# División acumulativa
number1 /= 2    # Es como: number1 = 30 / 2
print(f"División: {number1}") # Resultado: 15.0

# Potencia acumulativa
number1 **= 2   # Es como: number1 = 15.0 * 15.0
print(f"Potencia: {number1}") # Resultado: 225.0

# Módulo acumulativo
number1 %= 10   # Es como: number1 = 225.0 % 10 (el residuo)
print(f"Residuo: {number1}")  # Resultado: 5.0

# ==========================================
# OPERADORES DE COMPARACIÓN (ACTUALIZAR VALORES)
# ==========================================
a = 5
b = 7

# Igualdad (==): ¿Es a igual a b?
print(a == b)  # Resultado: False

# Diferente (!=): ¿Es a distinto de b?
print(a != b)  # Resultado: True

# Mayor que (>): ¿Es a mayor que b?
print(a > b)   # Resultado: Falso

# Menor que (<): ¿Es a menor que b?
print(a < b)   # Resultado: Verdadero

# Mayor o igual que (>=): ¿Es a mayor o igual que b?
print(a >= 15) # Resultado: Falso porque es menor que 15

# Menor o igual que (<=): ¿Es a menor o igual que b?
print(b <= 5)  # Resultado: False

# ==========================================
# EJEMPLO PRÁCTICO CON STRINGS
# ==========================================

usuario_registrado = "eduardo123"
usuario_intento = "Eduardo123"

# Comparar si los textos son iguales (Python distingue mayúsculas)
es_valido = usuario_registrado == usuario_intento
print(f"¿El usuario es correcto?: {es_valido}") # Resultado: False

# ========================================
# 4. EL OPERADOR AMPERSAND (&)
# ==========================================

# --- USO A: Lógico (con Booleanos) ---
# Evalúa si AMBAS condiciones son verdaderas
es_mayor_de_edad = True
tiene_dni = True

puede_votar = es_mayor_de_edad & tiene_dni 
print(f"¿Puede votar?: {puede_votar}") # Resultado: True

# Ejemplo con comparaciones directas
resultado_logico = (5 > 3) & (10 < 20) 
print(f"¿Ambas son ciertas?: {resultado_logico}") # Resultado: True

# ==========================================
# 4. OPERADORES LÓGICOS (AND / OR)
# ==========================================

# --- AND (& / and) ---
# Ambos deben ser ciertos
print((5 > 3) & (10 < 20)) # True

# --- OR (| / or) ---
# Al menos UNO debe ser cierto
tengo_efectivo = False
tengo_tarjeta = True

# Si tengo efectivo O tengo tarjeta, puedo comprar
puedo_comprar = tengo_efectivo or tengo_tarjeta
print(f"¿Puedo comprar?: {puedo_comprar}") # Resultado: True (porque uno es verdadero)

# Ejemplo con comparaciones
resultado_or = (10 > 50) or (5 == 5)
print(f"¿Alguna es cierta?: {resultado_or}") # Resultado: True