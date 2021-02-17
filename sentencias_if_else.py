'''
# Sentencia If - Else
# Definir una variable tipo Boolean
condicion = True

# Colocamos la estructura condicional If
if condicion:
    print("La condición es Verdadera")
else:
    print("La condición es Falsa")

# Elif
if condicion == True:
    print("La condición es Verdadera, de modo explícito")
elif condicion == False:
    print("La condición es Falsa, de modo explícito")
else:
    print("Condición no reconocida")
'''

# Recibe el valor que te proporcione el usuario
# Coloca un texto, de acuerdo al número que has recibido
numero = int(input("Ingresa un número entre el 1 y el 3"))

# Evaluar el número y de acuerdo al valor, colocaremos un texto
if numero == 1:
    numeroText = "UNO"
elif numero == 2:
    numeroText = "DOS"
elif numero == 3:
    numeroText = "TRES"
else:
    numeroText = "valor fuera de rango"
print(numeroText)