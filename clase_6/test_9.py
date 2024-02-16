import datetime


fecha_1 = datetime.datetime(2023, 4, 13 )
fecha_2 = datetime.datetime(2023, 4, 17 )

if fecha_1 == fecha_2:
    print("nacieron el mismo dia")
elif fecha_1 > fecha_2:
    print("El niño 2 es mayor que el niño 1")
else:
    print("El niño 1 es mayor que el niño 2")