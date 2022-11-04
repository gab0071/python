# Condicional If

print("########## EJEMPLO 1 #########")

color = input("Adivina cual es mi color favorito: ")

if color == "negro":
    print("Asi es, mi color favorito es negro ✨")
else:
    print("No este no es mi color favorito! 😒")


# Operadores de comparicion
print("########## EJEMPLO 2 #########")
print("---- Discoteca El Poblado ----")

nombre = input("Cual es tu nombre:")
edad =  int(input("Necesito saber tu edad:"))

if edad >= 18:
    print(f"Bienvenido {nombre}, puedes entrar a la fiesta. 🎉😊")
else:
    print(f"{nombre} no cumples con la mayoria de edad, no puedes entrar. 😢")

##########################################################################
print("########## EJEMPLO 3 #########")

nombre = input("cual es su nombre:")
edad = int(input("cual es su edad?:"))
sobrio = input("sobrio o no?")


if edad >= 18:
    print(f"{nombre} cumples con la edad para conducir.")

    if sobrio != "True":
        print(f"{nombre} quedas arrestado! 😒")
    else:
        print(f"{nombre} puedes continuar con tu viaje. 😎")
else:
    print(f"{nombre} esta multado, eres menor de edad! 🚨")


##########################################################################
print("########## EJEMPLO 4 #########")
print("---- Numero de dia de la semana ----")

dia = int(input("Ingresa el numero del dia de semana: "))

if dia == 1:
    print("es lunes")
elif dia == 2:
    print("el dia es martes")
elif dia == 3:
    print("el dia es miercoles")
elif dia == 4:
    print("el dia es jueves")
elif dia == 5:
    print("el dia es viernes")
else:
    print("es finde ✨🎉")


##########################################################################
''' 
Operadores Logicos en python

and => Y
or  => O
!   => Negacion
not => No

'''
print("########## EJEMPLO 5 #########")
print("---- Comprueba si tienes la edad para trabajar ----")

edad_min = 18
edad_max = 65
edad_oficial = int(input('ingresa tu edad: '))

if edad_oficial >= edad_min and edad_oficial <= edad_max:
    print('Puedes trabajar.')
else:
    print('No tienes edad para trabajar.')


##########################################################################
print("########## EJEMPLO 6 #########")

pais = 'España'

if not (pais == 'Mexico' or pais == 'España' or pais == 'Colombia'):
    print(f'{pais} No habla español')
else:
    print(f'{pais} Si habla español')    


