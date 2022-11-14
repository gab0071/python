# Funciones y metodos para las listas

cantantes = ["Justin B", "Coldplay", "JBalvin", "Maroon 5"]
numeros = [1, 2, 73, 50, 44, 11]

# Ordenar
print(numeros)  # Lista desordenada
numeros.sort()
print(numeros)  # Lista ordenada


# Añadir elementos
cantantes.append("Rihanna")
cantantes.insert(
    1, "Kygo"
)  # Recibe dos parametros -> .insert(posicion, lo que desees añadir)

print(cantantes)


# Eliminar elementos
cantantes.pop(1)
cantantes.remove("Justin B")

print(cantantes)


# Dar la vuelta a la lista 
numeros.reverse()

print(numeros)


# Buscar dentro de una lista 
print("Rihanna" in cantantes)


# Contar elementos de una lista
print(cantantes) 
print(len(cantantes))


# Cuantas veces aparece un elemento en una lista 
print(numeros.count(73))

# Conseguir el indice 
print(cantantes.index("Coldplay"))


# Unir listas 
cantantes.extend(numeros)
print(cantantes)