from random import *
#Inicializar intentos, numero random y pedir nombre al usuario
num_intentos=8
num_aleatorio=randint(1,100)
nombre_usuario=input("Introduce tu nombre: ")
print(f"Hola {nombre_usuario} he pensando un número aleatorio entre 1 y 100"
      f"\nTendrás 8 itentos para adivinarlo!\nQUE COMIENCE EL JUEGO!!")
#Generar la lógica del programa
while num_intentos>0:
    num_usuario=int(input("Prueba un número: "))
    if num_usuario==num_aleatorio:
        print(f"Enhorabuena has acertado el numero aleatorio era: {num_aleatorio}")
        break
    if (num_usuario<1) or (num_usuario>100):
        print("Has introducido un numero fuera del rango, prueba otra vez")
        num_intentos-=1
    elif num_usuario>num_aleatorio:
        print(f"{num_usuario} es mayor que el numero aleatorio")
    else :
        print(f"{num_usuario} es menor que el numero aleatorio")
if num_usuario!=num_aleatorio:
    print("Lo siento te has quedado sin intentos")




