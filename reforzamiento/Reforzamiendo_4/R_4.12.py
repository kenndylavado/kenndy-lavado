def Buenos_dias (despedida):
            
    def decoradora():
        print("Buenos dias")

        despedida()
        print("hasta luego")
        
    return decoradora()

@Buenos_dias
def saludo():
    nombre = input("ingrese su nombre: ")
    print(f"Soy {nombre}")
