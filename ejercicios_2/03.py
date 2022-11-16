''' 
    EJERCICIO 3

- Hacer un programa que compruebe si una variable esta vacia.
- Si esta vacia que la rellene con texto en minuscula y mostrarlo en mayuscula

'''

texto = " "

if len(texto.strip()) <= 0:
    texto = "Hola soy un texto en minuscula"
    print(texto.upper())

else:
    print(f"La variable tiene contenido {texto}")    