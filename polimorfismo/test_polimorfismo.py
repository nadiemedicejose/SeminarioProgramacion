from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(tipo_padre):
  print(tipo_padre)
  
empleado = Empleado('Steve Jobs', 18000)
imprimir_detalles(empleado)

empleado2 = Gerente('Mark Zuckerberg', 15000, "Sistemas")
imprimir_detalles(empleado2);
