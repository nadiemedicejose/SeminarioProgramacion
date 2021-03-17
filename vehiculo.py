# Clase Padre
class Vehiculo:
    def __init__(self, color, ruedas) -> None:
        self.__color = color
        self.__ruedas = ruedas
        
    def __str__(self) -> str:
        return "Color: " + self.__color + "\nRuedas: " + str(self.__ruedas) + "\n"

# Clase Hijo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad) -> None:
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self) -> str:
        return super().__str__() + "Velocidad: " + str(self.velocidad) + " km/hr\n"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self) -> str:
        return super().__str__() + "Tipo: " + str(self.tipo) + "\n"

# Creamos un objeto, donde utilicemos el concepto de la herencia
coche = Coche("Negro", 4, 180)
bicicleta = Bicicleta("Azul", 2, "Montaña")

# Enviaremos a impresión el objeto
print(coche)
print(bicicleta)
