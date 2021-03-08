# Sintaxis para la creación de una clase
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

persona = Persona("Juan", 20)
print(persona.nombre)
print(persona.edad)

persona2 = Persona("Maria", 18)
print(persona2.nombre)
print(persona2.edad)

print("Dirección en memoria: ", id(persona))
print("Dirección en memoria: ", id(persona2))
