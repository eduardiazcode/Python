# List (listas o conocidas tambien como arrays)
# Se permite hacer cambios osea son modificables
# Se permite tener duplicados de un item
# Son ordenadas

frutas = ["Manzana", "platano", "pera", "uva"]
print(type(frutas))

numeros = [1, 2, 3, 4, 5]
print(numeros)

varios = [True, "harina", 22, 45.7, -33, 2 + 1j]
print(varios)

# Accediendo a los items de la lista frutas
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

# Accediendo a los items de derecha a izquierda
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])
print(frutas[-4])

# EXTRAYENDO PARTE DE LA LISTA FRUTAS (SLICING - REBANADO)
frutas = ["Manzana", "platano", "pera", "uva"]
# [0]: "Manzana", [1]: "platano", [2]: "pera", [3]: "uva"

# 2. Aplicamos el slicing: frutas[inicio:fin]
# El índice de 'inicio' (1) se incluye.
# El índice de 'fin' (3) NO se incluye (se detiene justo antes).
frutas_2 = frutas[1:4]
# 3. El resultado será una nueva lista con los elementos de los índices 1 y 2.
# Imprime: ['platano', 'pera']
print(frutas_2)

# SUMA DE LISTAS
verduras = ['espinacas', 'cebollas', 'albaca', 'zanahoria']
numbers = [1, 2, 3, 4, 5]
print(verduras + numbers)

# MODIFICACION DE LISTA
ropa = ['pantalon', 'chompa', 'casaca', 'chacole']
print(ropa)
ropa[-1] = 'chaleco'
print(ropa)

ropa[1:4] = ['america', 'asia', 'oceania']
continentes = ropa[1:4]
print(ropa)
print(continentes)

continentes.append(['Lucia', 'Margiori', 'Samson']) 
# append: Sirve para agregar un unico elemento ne este caso es una lista
print(continentes)

colores = ['rojo', 'verde', 'azul', 'morado']
# extend: agrega varios elementos individuales dentro de la lista
colores.extend(['negro', 'blanco', 'turquesa'])
print(colores)

print(len(colores)) # hace un conteo de los elemntos de la lista

fusion = [ropa, colores]
print(fusion)
print(fusion[0])
print(fusion[1])
print(fusion[0][2])
print(fusion[1][5])

marcas_carros = ["Toyota", "Ford", "Nissan", "Chevrolet"]
print(marcas_carros)
del marcas_carros[2] # del se usa para eliminar un item dentro de la lista
print(marcas_carros)