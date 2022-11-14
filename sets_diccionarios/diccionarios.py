""" 
Diccionarios -> Es un tipo de dato que almacena un conjunto de datos.
En formato clave -> valor.
Es  parecido a un array asociativo o a un objeto JSON.

"""

persona = {"Nombre": "Ana", "Apellido": "Perez", "Email": "ana@ana.com"}

print(type(persona))
print(persona)


# Diccionarios dentros de listas 

contactos = [
    {
        "nombre": "Antonio",
        "email": "antonio@antonio.com"
    },
    {
        "nombre": "Robert",
        "email": "robert@robert.com"
    },
    {
        "nombre": "kendall",
        "email": "kendall@kendall.com"
    }
]

print(contactos[0]["nombre"])

print("\n ✨ LISTADO DE CONTACTOS ✨ ")
print("-------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("--------------------------------------------------")