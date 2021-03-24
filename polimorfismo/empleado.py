class Empleado:
  def __init__(self, nombre, sueldo) -> None:
      self.nombre = nombre;
      self.sueldo = sueldo;
      
  def __str__(self) -> str:
      return "\nNombre: " + self.nombre + "\nSueldo: $" + str(self.sueldo);
