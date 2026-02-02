
def operaciones_matematicas(number1, number2):
    suma = number1 + number2
    resta= number1 - number2
    multiplicacion = number1 * number2
    division = number1 / number2
    return suma, resta, multiplicacion, division


adicion, sustraccion, producto, segmentacion = operaciones_matematicas(14, 12)
print(f"Suma: {adicion}")
print(f"Resta: {sustraccion}")
print(f"Multiplicacion: {producto}")
print(f"Divison: {segmentacion}")