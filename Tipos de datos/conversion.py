# CONVERSION DE TIPOS DE DATOS
number = 1000
number_string = str(number)
print(type(number))
print(type(number_string))
print(type(str(number)))

var = "5000"
print(type(var))

print(number + int(var))

# Conversion numeros flotantes
variable = 12.25
print(type(variable))
print(variable)
int_number = int(variable)
print(int_number)

# Conversion de str a float
number_float = float(var)
print(type(number_float))
print(number_float)

print(int(var) + number_float) # Si se puede realizar operaciones matematicas con enteros y flotantes