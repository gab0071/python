"""
1. Crear un programa que pida numeros al usuario indefinidamente hasta meter el numero 111

"""

contador = 1

while contador < 100:
    num = int(input("Ingresa un numero: "))

    if num == 111:
        break
    else:
        print(f"Haz introducido el {num}")
