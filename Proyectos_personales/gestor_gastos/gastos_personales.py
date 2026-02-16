# GESTOR DE GASTOS PERSONALES

import os

runProgram = True
gastos = []

# Funcion para mostrar las opciones del menu
def mostrarMenu():
    print("Seleccione una opcion: ")
    print("")
    print("1. Ingrese el gasto: ")
    print("2. Ver los gastos realizados: ")
    print("3. Calcular el gasto acumulado: ")
    print("4. Eliminar gasto")
    print("5. Salir")

# Funcion para agregar el monto del gasto y el cocepto de este
def agregar_gasto():
    os.system("clear")
    global gastos
    print("==== AGREGAR GASTO ====")
    descripcion = (input("Descripcion del gasto: "))
    monto = float(input("Monto del gasto: S/."))
    
    gasto = { # El diccionario permitira guardar multiples etiquetas, en este caso descripcion y monto
        "descripcion": descripcion,
        "monto": monto
    }
    gastos.append(gasto)
    print(f"✅ Gasto agregado: {descripcion} - S/.{monto}")

    input("\nPresiona ENTER para continuar...") # \n Sirve para pausar el programa un momento hasta que se de enter

def gastos_realizados():
    os.system("clear")
    global gastos
    print("==== GASTOS REALIZADOS ====")

    if len(gastos) == 0:
        print("No hay gastos realizados")
    else:
        for i, gasto in enumerate(gastos, 1):
            print(f"{i}.  {gasto['descripcion']} - S/.{gasto['monto']}")
        print()
    
    input("\nPresiona ENTER para continuar...")

def calcular_total_gastos():
    os.system("clear")
    global gastos
    print("==== TOTAL DE GASTOS ====")
    
    if len(gastos) == 0:
        print("No hay gastos registrados")
        total = 0
    else:
        total = 0
        for gasto in gastos:
            total += gasto['monto']

        print(f"\n💰 Total gastado: S/.{total:.2f}")

    input("\nPresiona ENTER para continuar...")

def borrar_gastos():
    os.system("clear")
    global gastos
    print("==== ELIMINAR GASTOS REALIZADOS ====")

# Si no hay gastos salimos al menu anterior
    if len(gastos) == 0:
            print("No hay gastos para eliminar")
            input("\nPresione ENTER para continuar")
            return
    
# Mostramos los gastos
    for i, gasto in enumerate(gastos, 1):
        print(f"{i}. {gasto['descripcion']} - S/.{gasto['monto']}")

# Pedimos el numero y elminamos
    numero = int(input("Nuumero del gasto a eliminar: "))
    gastos.pop(numero -1)
    print("\n✅ Gasto eliminado")

    input("\nPresione ENTER para continuar...")


def main():
    global runProgram
    print("======================================================")
    print(".: BIENVENIDO A SU CALCULADORA DE GASTOS PERSONALES :.")
    print("======================================================")
    print("\nPresiona Enter para comenzar...")
    input()
    
    while runProgram:
        os.system("clear")
        mostrarMenu()

        try:
            option = int(input("\nSeleccione la opcion que quiera realizar: "))

            match option:

                case 1:
                    agregar_gasto()
                case 2 :
                    gastos_realizados()
                case 3:
                    calcular_total_gastos()
                case 4:
                    borrar_gastos()
                case 5:
                    print("Hasta luego !!!")
                    runProgram = False
                case _:
                    print("❌ No reconozco la opcion, reintente con una opcion valida")
                    input("\nPresione ENTER para continuar...")

        except ValueError:
            print("❌ Por favor ingrese un número")
            input("\nPresiona ENTER para continuar...")


if __name__ == "__main__":
    main()
