""" Listas en python es una coleccion o conjunto de datos o valores bajo un unico nombre.
"""

# Definiendo una lista
peliculas = ["batman", "iron-man", "spiderman"]

# Cuando le pasamos la tupla a la funcion list automaticamente se convierte en una lista
cantantes = list(("eminem", "justin bieber", "rihanna"))
years = list(range(2020, 2024))
varios = ["Catellatech", 2022, False, "Cate&Gabi"]

''' 
print(peliculas)
print(cantantes)
print(years)
print(varios) 
'''

#modificando la lista 
cantantes[0] = "drake"
print(cantantes)

# Indices de las listas 
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:3])

# Añadir elementos a la listas 
cantantes.append("coldplay")
print(cantantes)

# Recorrer una lista 
nueva_pelicula = ""

while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una peli: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n****** LISTADO PELICULAS ********")

for movies in peliculas:
    print(f"{peliculas.index(movies)+1}. {movies}")


# Listas Multidimensionales -> es una lista que contiene dentro otras listas 
# Ejemplo lista de contactos

contactos = [
    [
        "Antonio",
        "antonio@antonio.com"
    ],
    [
        "Robert",
        "robert@robert.com"
    ],
    [
        "kendall",
        "kendall@kendall.com"
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: "+ elemento)
        else:
            print("Email: "+ elemento)    
    print("\n")

# print(contactos[1][1])




    

