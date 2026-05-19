class ValidadorPassword:

    def validar(self, password):

        if len(password) < 8:
            return False

        tiene_mayuscula = False
        tiene_minuscula = False
        tiene_numero = False
        tiene_especial = False

        especiales = "!@#$%&*"

        for c in password:

            if 'A' <= c <= 'Z':
                tiene_mayuscula = True

            elif 'a' <= c <= 'z':
                tiene_minuscula = True

            elif '0' <= c <= '9':
                tiene_numero = True

            elif c in especiales:
                tiene_especial = True

        return (
            tiene_mayuscula and
            tiene_minuscula and
            tiene_numero and
            tiene_especial
        )