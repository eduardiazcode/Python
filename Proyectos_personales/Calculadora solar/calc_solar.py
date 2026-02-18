# Calculadora solar 

# Calcular energia de un panel solar
# Ver historial de calculos
# Borrar calculo del historial
# Salir del programa
import os
runProgram = True
calculos_list = []

# ===========================================
# FUNCIONES DEL MENÚ
# ===========================================

# Funcion para mostrar las opciones del menu
def showMenuOption():
    print("CALCULADORA SOLAR - JULIACA")
    print("Seleccione una opcion: ")
    print("")
    print("1. Calcular la energia de un panel solar")
    print("2. Ver historial de los calculos")
    print("3. Borrar un calculo del historial: ")
    print("4. Salir")

def mostrar_historial():
    global calculos_list

    if len(calculos_list) ==0:
        print("\n⚠️ No hay calculos en el historial aun")
        print(" Use la opcion 1 para generar su primer cálculo")
        return
    
    print("*" * 60)
    print("HISTORIAL DE CÁLCULOS")
    print("*" * 60)

    for i, calc in enumerate(calculos_list): # Recorre cada diccionario de la lista
        # enumerate: permite a;adir un contador automático
        print(f"\n📊 Cálculo #{i + 1}")
        print(f"Fecha: {calc['fecha']}")
        print(f"Area del panel: {calc['area']}")
        print(f"Irradiancia: {calc['irradiancia']} kWh/m²/día")
        print(f"Rendimiento: {calc['rendimientio'] * 100}%")
        print(f"Energia generada: {calc['energia']} kW/día")
        print(f"Ahorro mensual: S/. {calc['ahorro']}")
        print(f"Ahorro anual: S/. {calc['ahorro'] * 12}")
        print("*" * 60)

# ==================================================
# FUNCIONES DE CALCULO
# ==================================================

# Funcion del calculo de energia generada por un panel solar
def calcular_energia_solar(area, irradiancia, rendimiento):
    # Formula: E = AREA * IRRADIANCIA * RENDIMIENTO
    # Retorna: energia en kwh/dia

    energia = area * irradiancia * rendimiento
    return round(energia,2) # round es funcion que redondee un numero decimal con 2 decimales

# Funcion del calculo de ahoror economico mensual
def calcular_ahorro(energia_kwh, precio_kwh):
    ahorro_diario = energia_kwh * precio_kwh
    ahorro_mensual = ahorro_diario * 30
    return round(ahorro_mensual, 2)

# FUncion que solicita calculos y realiza el calculo solar
def crear_calculo():
    os.system("clear")
    global calculos_list

    

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
                    mostrar_historial()
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

