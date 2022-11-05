# Bucles For
print("########## EJEMPLO 1 #########")

contador = 0
resultado = 0

for contador in range(0,7):
    print(f"el contador va por {str(contador)}")

    # Suma 
    resultado += contador
print(f"El resultado es: {resultado}") 


##########################################################################
print("########## EJEMPLO 2 #########")
print("---- Tabla de Multiplicar ----")

num_usuario = int(input("¿De que numero quieres ver la tabla?🤓: "))

if num_usuario < 1:
    num_usuario = 1

print(f"-- tabla de multiplicar del {num_usuario} --")

for num_tabla in range(1, 11):
    print(f"{num_usuario} ❌ {num_tabla} = {num_usuario * num_tabla}")
else:
    print("✨ Tabla finalizada ✨")


##########################################################################
# Blucles While
print("########## EJEMPLO 1 #########")

contador = 1

while contador <= 50:
    print(f"Estoy en el numero {contador}")
    contador += 1

# ##########################################################################

contador = 1
muestrame = str(0)

while contador <= 50:
    muestrame += " ," + str(contador)
    contador += 1
print(muestrame)


#########################################################################
print("########## EJEMPLO 2 #########")
print("---- Tabla de Multiplicar con el bucle While ----")

num_usuario = int(input("¿De que numero quieres ver la tabla?🤓: "))
contador = 1

if num_usuario < 1:
    num_usuario = 1
print(f"-- tabla de multiplicar del {num_usuario} --")

while contador <= 10:
    print(f"{num_usuario} ❌ {contador} = {num_usuario * contador}")
    contador += 1
else:
    print("✨ Tabla finalizada ✨")
