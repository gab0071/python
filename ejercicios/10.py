"""
1. Crear un programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos han aprobado y cuantos no.

"""

contador = 1
aprobados = 0
reprobados = 0

num_alumnos = int(input("Cuantos alumnos tienes?: "))

while contador <= num_alumnos:
    nota = int(input(f"Que nota quieres colocarle al 'alumno {contador}'?: "))

    if nota >= 5:
        aprobados += 1
    else:
        reprobados += 1        
    contador += 1

print(f"Alumnos aprobados {aprobados} ✔")
print(f"Alumnos reprobados {reprobados} ❌")
