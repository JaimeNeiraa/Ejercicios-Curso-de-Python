
from random import randint

# Inicializar intentos, número aleatorio y pedir nombre al usuario
num_intentos = 8
num_aleatorio = randint(1, 100)
nombre_usuario = input("Introduce tu nombre: ")
print(f"Hola {nombre_usuario}, he pensado un número aleatorio entre 1 y 100"
      f"\nTendrás 8 intentos para adivinarlo!\n¡QUE COMIENCE EL JUEGO!")

# Generar la lógica del programa
while num_intentos > 0:
    num_usuario = int(input("Prueba un número: "))

    # Usuario acierta
    if num_usuario == num_aleatorio:
        print(f"¡Enhorabuena! Has acertado. El número aleatorio era: {num_aleatorio}")
        break

    # Usuario introduce número fuera de rango
    elif num_usuario < 1 or num_usuario > 100:
        print("Has introducido un número fuera del rango. Prueba otra vez.")

    # Usuario introduce número mayor que el aleatorio
    elif num_usuario > num_aleatorio:
        print(f"{num_usuario} es mayor que el número aleatorio.")
        if abs(num_usuario - num_aleatorio) <= 5:
            print("Caliente, te estás acercando.")
        else:
            print("Frío, te estás alejando.")

    # Usuario introduce número menor que el aleatorio
    elif num_usuario < num_aleatorio:
        print(f"{num_usuario} es menor que el número aleatorio.")
        if abs(num_usuario - num_aleatorio) <= 5:
            print("Caliente, te estás acercando.")
        else:
            print("Frío, te estás alejando.")

    # Reducir el número de intentos
    num_intentos -= 1
    print(f"Te quedan {num_intentos} intentos.\n")

# Si se acaban los intentos
if num_usuario != num_aleatorio:
    print(f"Lo siento, te has quedado sin intentos. El número aleatorio era: {num_aleatorio}")


