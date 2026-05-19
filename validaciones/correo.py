class ValidadorCorreo:

    def validar(self, correo):

        estado = 0

        for c in correo:

            if estado == 0:
                if self.es_letra_numero(c):
                    estado = 1
                else:
                    return False

            elif estado == 1:
                if self.es_letra_numero(c) or c in ['.', '_', '-']:
                    estado = 1
                elif c == '@':
                    estado = 2
                else:
                    return False

            elif estado == 2:
                if self.es_letra_numero(c):
                    estado = 3
                else:
                    return False

            elif estado == 3:
                if self.es_letra_numero(c):
                    estado = 3
                elif c == '.':
                    estado = 4
                else:
                    return False

            elif estado == 4:
                if self.es_letra(c):
                    estado = 5
                else:
                    return False

            elif estado == 5:
                if self.es_letra(c):
                    estado = 5
                else:
                    return False

        return estado == 5

    def es_letra(self, c):
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

    def es_numero(self, c):
        return '0' <= c <= '9'

    def es_letra_numero(self, c):
        return self.es_letra(c) or self.es_numero(c)