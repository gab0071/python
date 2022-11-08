''' Variables Locales y Globales
        Locales: Es aquella que se define dentro de la funcion y no puede ser usada fuera.
        Globales: Son las que se declaran fuera de la funcion y pueden ser usadas dentro y fuera de las funciones.
'''

frase = "Es mejor Crypto que FIAT"

print(frase)

def probando():
    frase = "Hola mundo"
    print("Dentro de la funcion: ")
    print(frase)

    year = 2022
    print(year)

    global website 
    website = "catellatech.com"
    print(f"In: {website}")

    return str(year)

print(probando())
print(f"Out: {website}")
    