"""
1. Hacer un programa que muestre todos los numeros entre dos numeros que diga el usurio.

"""

num_uno = int(input("Ingresa tu primer numero: "))
num_dos = int(input("Ingresa tu segundo numero: "))

num_dos += 1

if num_uno < num_dos:
    for contador in range(num_uno, num_dos):
        print(contador)
else:
    print("el num 1 debe ser mayor al num 2")
