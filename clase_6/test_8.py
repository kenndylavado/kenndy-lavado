from datetime import datetime


str_date = "2/6/2023"


"""
    d = dia
    m = mes
    Y = año
"""
conversion = datetime.strptime(str_date,"%m/%d/%Y")
print("la fecha formteada es {}".format(conversion))


conversion_letras = datetime.strftime(conversion, "%d %b del %Y")
print("la fecha literal es: {}".format(conversion_letras))