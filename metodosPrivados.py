# Crear una clase y dentro de la clase un método privado
class Persona:
    def __init__(self, nombre, aPaterno, aMaterno) -> None:
        self.nombre = nombre            # Public
        self._aPaterno = aPaterno       # Protected
        self.__aMaterno = aMaterno      # Private
        
    def MetodoPublico(self):
        self.__MetodoPrivado()
        
    def __MetodoPrivado(self):
        print(self.nombre)
        print(self._aPaterno)
        print(self.__aMaterno)
    
    def set__aMaterno(self, aMaterno):
        self.__aMaterno = aMaterno
    
    def get__aMaterno(self):
        return self.__aMaterno
            
# Creación del objeto
persona1 = Persona('Alfonso', 'Cuaron', 'Orozco')

# ¿Qué sucede si llamamos al método privado?
# persona1.__MetodoPrivado()

# ¿Qué debo hacer para acceder a un método privado?
persona1.MetodoPublico()

# ¿Se podrán modificar directamente los atributos?
print('********************************************')
print('Accediendo a los atributos de manera directa')
persona1.nombre = 'Guillermo'
persona1._aPaterno = 'del Toro'
persona1.set__aMaterno('Gomez')
print(persona1.nombre)
print(persona1._aPaterno)
print(persona1.get__aMaterno())