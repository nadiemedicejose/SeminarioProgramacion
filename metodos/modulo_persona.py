# Creamos una clase
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.__edad = edad
        
    def __str__(self) -> str:
        return "El nombre es: " + self.__nombre + " y su edad: " + str(self.__edad) + " años"
    