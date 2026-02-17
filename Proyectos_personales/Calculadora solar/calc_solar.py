# Calculadora solar 

# Calcular energia de un panel solar
# Ver historial de calculos
# Borrar calculo del historial
# Salir del programa
import os
runProgram = True

# Funcion para mostrar las opciones del menu
def showMenuOption():
    print("CALCULADORA SOLAR - JULIACA")
    print("Seleccione una opcion: ")
    print("")
    print("1. Calcular la energia de un panel solar: ")
    print("2. Ver historial de los calculos solares: ")
    print("3. Borrar un calculos del historial de calculos: ")
    print("4. Salir")

def calcular_energia_solar():
    pass

def historial_calculos():
    pass

def borrar_historial():
    pass


# Funcion principal del programa
def main():
    global runProgram

    print("=" * 50)
    print(".: CALCULADORA DE ENERGIA SOLAR ☀️⚡:. ")
    print(".: REALIZADO EN JULIACA - PERÚ :. ")
    print("=" * 50)
    print("\nHerramienta que calcula la energia generada por un panel solar en Juliaca")
    print("\n☀️    Irradiacia promedio de Juliaca:       5.5-6.5 kWh/m²/día")
    print("💰   Precio promedio electricidad:         S/ 0.60 por kWh")
    print("\n" + "=" * 50)
    input("Presione ENTER para empezar...")

    while runProgram:
        os.system("clear")
        showMenuOption()

        try:
            option = int(input("\nSeleccione la opcion que quiera realizar: "))

            match option:

                case 1:
                    calcular_energia_solar()
                case 2 :
                    historial_calculos()
                case 3:
                    borrar_historial()
                case 4:
                    print("Hasta luego !!!")
                    runProgram = False
                case _:
                    print("❌ No reconozco la opcion, reintente con una opcion valida")
                    input("\nPresione ENTER para continuar...")

        except ValueError:
            print("❌ Por favor ingrese un número")
            input("\nPresiona ENTER para continuar...")



# Punto de entrada del programa
if __name__ == "__main__":
    main()

