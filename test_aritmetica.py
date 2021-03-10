# Realizar la importacion
# from metodos import modulo_aritmetica as aritmetica
import metodos.modulo_aritmetica as aritmetica

# Utilizar las funciones
sumaResultado = aritmetica.sumar(100, 50)
restaResultado = aritmetica.restar(50, 10)
multiplicacionResultado = aritmetica.multiplicar(10, 10)
divisionResultado = aritmetica.dividir(100, 5)

# Enviamos a impresion los resultados
print('El resultado de la suma es: ', sumaResultado)
print('El resultado de la resta es: ', restaResultado)
print('El resultado de la multiplicacion es: ', multiplicacionResultado)
print('El resultado de la division es: ', divisionResultado)
