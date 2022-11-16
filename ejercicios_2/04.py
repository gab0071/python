''' 
    EJERCICIO 4

- Crear un script que tenga cuatro variables:
    - una lista
    - una string
    - un entero 
    - un booleano

- Imprimir un mensaje con el tipo de dato de cada variable
- Usar funciones

'''

lista = ["Hola mundo"]
string = "Hola mundo"
intiger = 444
boolean = True

def tipoDato(elemento):
    return (type(elemento))

print(tipoDato(lista))
print(tipoDato(string))
print(tipoDato(intiger))
print(tipoDato(boolean))