''' 
    Ejercicio 2

- Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120.    

'''

lista = []
add = input("Agrega cosas a la lista: ")

# Hecho con el bucle while
while len(lista) < 120:
    add = input("Agrega cosas a la lista: ")
    lista.append(add)
else:
    print("ya no queda espacio en la lista")   


# Hecho con el bucle for 
for list in range(0,120):
    if len(lista) <= 120:
        add = input("Agrega cosas a la lista: ")
        lista.append(add)
    else:
        print("ya no queda espacio en la lista")

lista.sort()
print(lista)