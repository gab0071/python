# Funciones en Python 

# Ejemplo 1 
print("--- Ejemplo Uno ---")

# Definiendo una funcion 
def muestraNombre():
    print("catellaTech")
    print("catherine")
    print("gabriela")
    print("rattio")
    print("\n")
# Invocando la funcion     
muestraNombre()  



# Parametros en fuciones
# Ejemplo 2 
print("--- Ejemplo Dos ---")

def muestraTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre} ✨")

    if edad >= 18:
        print("Eres mayor de edad")

nombre = input("¡Introduce tu nombre!: ")
edad = int(input("¡Introduce tu edad!: "))
muestraTuNombre(nombre, edad)



# Ejemplo 3
print("--- Ejemplo Tres ---") 

def tablaMul(numero):
    print(f"Tabla del numero {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} ❌ {contador} = {operacion}")

    print("\n")
numero = int(input("De que numero quieres la tabla?: "))    
tablaMul(numero)        

# Si queremos mostrar todas las tablas del 1 al 10 
print("---------------------------------------")

for numTabla in range(1,11):
    tablaMul(numTabla)


# Ejemplo 4
print("--- Ejemplo Cuatro ---")    

# Parametros opcionales --> Le podemos pasar o no ese dato

def getEmpleado(nombre, id = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    
    if id != None:
        print(f"Id: {id}")

getEmpleado("catellatech", 1345678)        
getEmpleado("cate")        






