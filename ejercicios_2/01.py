''' 
    Ejercicio 1 

- Hacer una lista que tenga 8 numeros enteros. ✅
- Recorrer la lista y mostrarla. ✅
- Hacer una funcion que recorra la lista y devuelva un str ✅
- Ordenarla y Mostrarla ✅
- Mostrar su longitud ✅
- Buscar algun elemento (que el usuario pida por teclado) ✅

'''

numeros = [1,6,3,5,2,8,9,7]

print("\n------- Recorrer y Mostrar -------")
for numero in numeros:
    print(numero)


################################################################

print("\n------- Funcion -------")
def mostrarLista(lista):
    resul = ""

    for elemento in lista:
        resul += "Elemento: " + str(elemento)
        resul += "\n"
    
    return resul   

print(mostrarLista(numeros)) 

################################################################

print("\n------- Ordenar la Lista y mostrarla -------")
numeros.sort()
print(numeros)

print("\n------- Mostrar su longitud -------")
print(len(numeros))



################################################################
print("\n------- Introduce el numero -------")

busca = int(input("¿Que numero quieres buscar?: "))
# Comprobar si lo que el user ingresa es un entero 
comprobar = isinstance(busca, int)

while not comprobar or busca <= 0:
    busca = int(input("¿Que numero quieres buscar?: "))
else:
    print(f"Has introducido el numero {busca}")


print(f"\n------- Buscar en la lista el numero {busca} -------")  

search = numeros.index(busca)
print(f"El numero que has introducido existe y esta en el indice: {search}")


              


    