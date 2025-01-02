#Pedimos el texto y las letras al usuario
text_usuario=input("Ingresa un texto: ")
letras_usuario=input("Ahora elige tres letras: ")
#Lo pasamos a una lista para poder comprobar
text_usuario=text_usuario.lower()
letras_usuario=letras_usuario.lower()
letras_usuario=list(letras_usuario)
letra1=letras_usuario[0]
letra2=letras_usuario[1]
letra3=letras_usuario[2]
print("Primer Análisis: Veces que aparecen las letras elegidas")
print(f"La  letra {letra1} aparece",text_usuario.count(letra1), "veces")
print(f"La  letra {letra2} aparece",text_usuario.count(letra2), "veces")
print(f"La  letra {letra3} aparece",text_usuario.count(letra3), "veces")
print("---------------------------------------------------------")
#Primer Análisis Completado
print("Segundo Análisis: Cantidad de palabras")
print("La cantidad de palabras del texto introducido es: ",len(text_usuario.split()))
print("---------------------------------------------------------")
#Segundo Análisis completado
primera_letra=text_usuario[0]
ultima_letra=text_usuario[-1]
print("Tercer Análisis: Primera y última letra")
print(f"La primera letra es: {primera_letra}\ny la última letra es : {ultima_letra}")
print("---------------------------------------------------------")
#Tercer Análisis Completado
#Dividir el texto en palabras
palabras=text_usuario.split()
#Invertir el orden de las palabras
palabras_invertidas=palabras[::-1]
#Unir es palabras con un espacio intermedio
text_invertido=" ".join(palabras_invertidas)
print("Curto Análisis: Texto invertido")
print(f"El texto invertido es: \n{text_invertido}")
print("---------------------------------------------------------")
#Cuarto Análisis Completado
print("Quinto Análisis: ¿Aparece la palabra python?")
dic={1:"Aparece la palabra python en el texto",2:"No aparece la palabra python en el texto"}
esta_python=  "python" in text_usuario.split()
if esta_python==True:
    print(dic[1])
else:
    print(dic[2])
