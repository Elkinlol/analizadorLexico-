class ValidadorTelefono:

    def validar(self, numero):

        if len(numero) != 10:
            return False

        if numero[0] != '3':
            return False

        for c in numero:
            if c < '0' or c > '9':
                return False

        return True