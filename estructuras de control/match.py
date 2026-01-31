# Es una estructura de control que te permite comparar varios patrones
# ========================================================
# Forma antigua muy anticuada
dia = 5

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Se termino la semana no existe mas dias")
# ==========================================================
dia = 6

match dia:
    case 1:
        print("Lunes")
    case 2:
        print('Martes')
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case _:
        print("FIn de semana")

# =================================================
option = input("Elige (a/b/c): ")
match option:
    case "a":
        print("Nuevo archivo")
    case "b":
        print("Abrir archivo")
    case "c":
        print("Seleccionaste guardar archivo")
    case _:
        print("Opcion no valida")

# ==================================================
a = 14
b = 6
operacion = input("Escoja que operacion hara (+/-/*//): ")

match operacion:
    case "+":
        resultado =  a + b
    case "-":
        resultado = a - b
    case "*":
        resultado = a * b
    case "/":
        resultado = a / b
    case _:
        print("Operacion invalida")

print(f"Resultado: {resultado}")

# ==================================================
edad = 15

match edad:
    case edad if edad < 0:
        print("Edad no válida")
    case edad if edad < 13:
        print("Eres un niño")
    case edad if edad < 18:
        print("Eres un adolescente")
    case edad if edad < 60:
        print("Eres un adulto")
    case _:
        print("Eres un adulto mayor")

