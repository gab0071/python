"""
1. Crear un programa que calcule ¿cuanto es el x porciento de que x numero?
ejemplo : 20% de 150.

"""

num = int(input("Introduce un numero: "))
porcentaje = int(input(f"¿Que porcentaje quieres sacar del {num}?: "))

operacion = (num * (porcentaje/100))

print(f"El {porcentaje}% de {num} es: {operacion} ✨")