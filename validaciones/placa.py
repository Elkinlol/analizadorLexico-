class ValidadorPlaca:

    def validar(self, placa):

        if len(placa) != 6:
            return False

        letras = placa[0:3]
        numeros = placa[3:6]

        for c in letras:
            if not ('A' <= c <= 'Z'):
                return False

        for c in numeros:
            if not ('0' <= c <= '9'):
                return False

        return True