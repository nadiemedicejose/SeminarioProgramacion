# Creamos una clase
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.__edad = edad
        
    def get__nombre(self):
        return self.__nombre
    
    def set__nombre(self, nombre):
        self.__nombre = nombre
        
    def get__edad(self):
        return self.__edad
    
    def set__edad(self, edad):
        self.__edad = edad
        
# Crear el objeto
persona1 = Persona("Carlos", 19)
print("Nombre inicial: ", persona1.get__nombre())
print("Edad inicial: ", persona1.get__edad())

# Modificar el valor del atributo, utilizando el método Set
persona1.set__nombre("Manuel")
persona1.set__edad(22)

# Enviaremos a impresión
print("Nombre final: ", persona1.get__nombre())
print("Edad final: ", persona1.get__edad())
