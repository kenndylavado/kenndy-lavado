from datetime import datetime, date



fecha = date.today()
print("La fecha de hoy es {}".format(fecha))

tiempo = datetime.now
print(tiempo)


anio= tiempo.year
mes=tiempo.month
dia=tiempo.day

print("Año actual es: {}".format(anio))
print("mes actual es: {}".format(mes))
print("dia actual es: {}".format(dia))


hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print("la hora exacta es {} el minuto es {} y el segundog {}".format(hora,minuto,segundo))