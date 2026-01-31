# cuando la condicion es = (if)True => ejecuta el codigo
# cuando la condicion es = (else) False => ejecuta otra porcion de codigo

age_person = int(input("Ingrese su edad por favor: "))
EDAD = 18

if age_person > 18:
    print("Eres una persona mayor de edad y eres mayor a 18 años")
    if age_person == 50: # Se ejecuta solo si la primeracion opcion es True
        print("Eres una persona de la tercera edad") 
elif age_person == 18: # Si no se cumple la primera condición
    print("Tu edad es de 18 años")
else:
    print("Eres una persona menor de edad")

