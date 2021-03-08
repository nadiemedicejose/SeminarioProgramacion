# Creamos una clase
class Aritmetica:
    def __init__(self, operando1, operando2) -> None:
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def multiplicar(self):
        return self.operando1 * self.operando2
    
    def dividir(self):
        return self.operando1 / self.operando2
    
# Crear el objeto
aritmetica = Aritmetica(20, 40)

print("El resultado de la suma es: ", aritmetica.sumar())
print("El resultado de la resta es: ", aritmetica.restar())
print("El resultado de la multiplicacion es: ", aritmetica.multiplicar())
print("El resultado de la division es: ", aritmetica.dividir())