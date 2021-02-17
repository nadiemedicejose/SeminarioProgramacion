mes = int(input("Ingresa el número de mes [1-12]: "))

if mes == 1:
    mesTexto = "Enero"
elif mes == 2:
    mesTexto = "Febrero"
elif mes == 3:
    mesTexto = "Marzo"
elif mes == 4:
    mesTexto = "Abril"
elif mes == 5:
    mesTexto = "Mayo"
elif mes == 6:
    mesTexto = "Junio"
elif mes == 7:
    mesTexto = "Julio"
elif mes == 8:
    mesTexto = "Agosto"
elif mes == 9:
    mesTexto = "Septiembre"
elif mes == 10:
    mesTexto = "Octubre"
elif mes == 11:
    mesTexto = "Noviembre"
elif mes == 12:
    mesTexto = "Diciembre"
else:
    mesTexto = "mes fuera de rango"

# Para las estaciones
if mes >= 3 and mes <= 5:
    estacion = "Primavera"
elif mes >= 6 and mes <= 8:
    estacion = "Verano"
elif mes >= 9 and mes <= 11:
    estacion = "Otoño"
elif mes == 12 or mes <= 2:
    estacion = "Invierno"
else:
    estacion = "no definido"
print("En", mesTexto, "la estación del año es", estacion)