# ¿Cuál es la utilidad del Break?
for letra in "UNIVERSIDAD ESTATAL DE SONORA":
    if letra == "A":
        print(letra)
        break
    
# ¿Cuál es la utilidad del Continue?
# Enviar a impresión por pantalla los números pares
# contenidos dentro de un rango de valores
for i in range(50):
    if i%2 == 0:
        print("Es número PAR!", i)