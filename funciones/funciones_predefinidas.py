''' Funciones predefinidas en python '''

nombre = "catellaTech"

# Funciones generales 
print(type(nombre))

# Detectar el tipado 
comprobar = isinstance(nombre, str)

if comprobar:
    print("Esa variable es str")
else:
    print("No es str")  


# Limpiar espacios de un str 

frase = "   HOLA QUE TAL    "

print(frase)
print(frase.strip())


# Eliminar variables 
year = 2022
print(year)

del year
# print(year)


# Comprobar variable vacia 
text = "    ff  "

if len(text) <= 0:
    print("la variable esta vacia")
else:
    print("la variable tiene contenido: ", len(text))



# Encontrar Caracteres 
frase = "la vida es bella"
print(frase.find("vida"))


# Reemplazar palabras en un string 
new_frase = frase.replace("vida", "casa")
print(new_frase)


# Mayusculas y Minusculas 
print(nombre)
print(nombre.lower())
print(nombre.upper())

