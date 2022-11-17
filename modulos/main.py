"""
Modulos: Funcionalidades ya hechas para utilizar
link: https://docs.python.org/3/py-modindex.html

https://docs.python.org/3/library/datetime.html#module-datetime

"""

# importar modulo
# import mi_modulo
# from mi_modulo import hola_mundo
from mi_modulo import *
# Modulo fechas
import datetime


# print(mi_modulo.hola_mundo("✨catellaTech✨"))

# print(mi_modulo.calculadora(3,5, True))

print(hola_mundo("✨catellaTech✨"))

print(calculadora(3,5, True))


## ---------------------------------------------------------------------------------------------------------
# Modulo fechas

print(datetime.date.today())
 
fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)


fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada ", fecha_personalizada)
print(datetime.datetime.now().timestamp())