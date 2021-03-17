# Clase Padre
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self) -> str:
        return "Nombre: " + self.nombre + "\nEdad: " + str(self.edad) + " años\n"

# Clase Hijo
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    def __str__(self) -> str:
        return super().__str__() + "Sueldo: $" + str(self.sueldo) + "\n"

# Creacion de los ojbetos
persona = Persona("Esteban", 22)

# Enviamos a impresion
print(persona)

# Creamos un objeto, donde utilicemos el concepto de la herencia
empleado = Empleado("Jesus", 20, 15600.93)

# Enviaremos a impresión el objeto
print(empleado)

# Modificar atributos de manera
empleado.nombre = 'Laura'
empleado.edad = 25
empleado.sueldo = 13299.75

# Reimprimimos el objeto
print(empleado)
