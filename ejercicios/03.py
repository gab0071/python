''' 

1. Hacer los cuadrados de los 60 primeros numeros naturales
2. Hacerlo con el bucle while y for

'''
# For 

for contador in range(1,61):
    cuadrado = contador * contador
    print(f"el cuadrado de {contador} es {cuadrado}")


# While 

contador = 1

while contador <= 60:
    cuadrado = contador ** 2
    print(f"el cuadrado de {contador} es {cuadrado}")
    contador += 1
