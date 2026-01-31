# Diccionarios
# Sintaxis {"id": 1} {clave: valor}
# Es ordenada
# Se puede hacer modificaciones
# No se puede tener contenido duplicado

usuario = {
    "nombre": "Miguel",
    "apellido": "Fernandez",
    "edad" : 26,
    "colores favoritos" : ['rojo', 'azul', 'verde', 'amarillo'],
    "musicas_favoritas" : {
        "pop" : "Billie Jean",
        "salsa" : "Sol a sol",
        "merengue" : "Mar y Luna"
    }
}

print(usuario["nombre"])
print(usuario["apellido"]) # Para acceder a unos de los items siempre hay que hacerlo entre comillas
print(usuario["edad"])
print(usuario["colores favoritos"])
print(usuario["musicas_favoritas"])

print(len(usuario["colores favoritos"]))
print(len(usuario))

equipos = dict(jugadores = 11, colores_camiseta = ['azul', 'celeste','crema'], region = ['costa', 'sieraa', 'selva'])
print(type(equipos))
print(equipos)