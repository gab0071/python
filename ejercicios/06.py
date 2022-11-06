"""
1. Mostrar todas las tablas de multiplicar del uno al 10
2. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

"""

for numTabla in range(1, 11):
    print("########################")
    print(f"Tabla del numero {numTabla}")
    print("########################")

    for num in range(1, 11):
        print(f"{num} ❌ {numTabla} = {num * numTabla}")
    
    # Salto de linea entre las tablas    
    print("\n")    
