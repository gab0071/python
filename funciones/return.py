''' Funciones en python
        * Return
        * Mas sobre parametros opcionales
'''

# Ejemplo 1 
print("\n--- Ejemplo Uno ---")

def saludame(nombre):
    saludo = f"Hola, que tal {nombre}"

    return saludo
print(saludame("catellatech"))    


# Ejemplo 2 
print("\n--- Ejemplo Dos ---")

''' Hacer una calculadora que:
        1. que tenga suma, resta, multiplicacion y division
        2. esta funcion nos va a devolver un resultado

        nota: Hacer que cuando tengamos el parametro basicas en False nos muestre la mul y div nada mas.
              y cuando este en True solo la suma y la resta.
'''


def calculadora(num1,num2, basicas = False):
    suma  = num1 + num2
    resta = num1 - num2
    mult  = num1 * num2
    div   = num1 / num2

    cadena = ""

    if basicas != False:
        cadena += f"Suma: {str(suma)}"
        cadena += f"\n"
        cadena += f"Resta: {str(resta)}"
        cadena += f"\n"
    else:    
        cadena += f"Multiplicacion: {str(mult)}"
        cadena += f"\n"
        cadena += f"Division: {str(div)}"

    return cadena

print(calculadora(25,4))
print(calculadora(2,4, True))


# Ejemplo 3
# Funciones dentro de otra 
print("\n--- Ejemplo Tres ---")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"

    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"

    return texto

def getPersona(nombre, apellido):
    text = f"{getNombre(nombre)}\n{getApellido(apellido)}"

    return text

print(getPersona("hola","chao"))

# Ejemplo 4
# Funciones Lambda o funcion anonima
print("\n--- Ejemplo Cuatro ---")

año = lambda year: f"El año es {year}"

print(año(2022))

