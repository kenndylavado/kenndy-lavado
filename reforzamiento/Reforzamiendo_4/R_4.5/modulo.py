def usuario(nombre):
        if len(nombre) < 7 or len(nombre)>12:
            return "El nombre de usuario tiene que tener entre 7 a 12 caracteres."
        if (not nombre.isalnum()):
            return "El nombre de usuario puede contener solo letras y números"
        return True
