"""
1. Mostrar todos los numeros impares y pares entre dos numeros que ingrese el usuario

"""

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 < num2:
    for numero in range(num1, (num2 + 1)):
        if numero % 2 == 1:
            print(f"{numero} es impar")
        else:
            print(f"{numero} es par")
else:
    print("el primer numero debe ser menor al segundo")
