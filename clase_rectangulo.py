# Clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
        
    def CalcularArea(self):
        return self.base * self.altura
    
# Crear el objeto
rectangulo = Rectangulo(8, 10)

print("El area del rectangulo: ", rectangulo.CalcularArea(), " m2")