
def filemanipulacion(dir, mode):
    file = open(dir, mode)
    
    print(file.read())
    file.close()


    return file
#has
#ha
filewrite = "c:/Users/kenndy/Desktop/python/clases_uni/clase_7/mi_file/file_5.txt"


print("lectura del archivo")
filemanipulacion(filewrite, "r")