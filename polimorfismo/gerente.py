from empleado import Empleado

class Gerente(Empleado):
  def __init__(self, nombre, sueldo, departamento) -> None:
      super().__init__(nombre, sueldo)
      self.departamento = departamento
      
  def __str__(self) -> str:
      return super().__str__() + "\nDepartamento: " + self.departamento
