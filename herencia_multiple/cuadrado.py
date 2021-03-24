# Importación de superclases
from figuraGeometrica import FiguraGeometrica
from color import Color

# Creamos la subclase
class Cuadrado(FiguraGeometrica, Color):
  def __init__(self, lado, color):
    FiguraGeometrica.__init__(self, lado, lado)
    Color.__init__(self, color)
    
  def area(self):
    return self.ancho * self.alto
    