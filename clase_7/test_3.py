

""" 
    w : abre el archivo para que pueda escribir sobre el.
"""
file = open("c:/Users/kenndy/Desktop/python/clases_uni/clase_7/mi_file/file_2.txt", "w")


file.write( "\nhola como estas\n")
file.write("te veo bien\n")
file.write("adios amigo")

file = open("c:/Users/kenndy/Desktop/python/clases_uni/clase_7/mi_file/file_2.txt", "r")

print("nuestro archivo file_2.txt tiene el siguiente contenido: {}".format(file.read()))
file.close()
