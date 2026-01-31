# Sin manejo de errores - el programa crashea (es cuando un programa se cierra o congela)
# Estructura basica para capturar errores
# ============================================================
# numero = int(input("Ingresa un número: "))

try:
    numero = int(input("Ingresa un número: "))
    print(f"El número es: {numero}")
except:
    print("Error: No ingresaste un número válido")
# =============================================================
try:
    number = int(input("Ingrese un numero: "))
    resultado = 10 / number
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Error: El numero ingresado en un decimal intente con un numero entero")
except ZeroDivisionError:
    print("Error: No puede dividirse entre 0")
# ==============================================================
try:
    age = int(input("Tu edad es: "))
except ValueError:
    print("Edad invalida")
else:
    print(f"Tu edad es: {age}")
    if age >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres una persona menor de edad")
finally:
    print(("FIn del programa"))