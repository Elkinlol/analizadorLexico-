class ValidadorFecha:

    def validar(self, fecha):

        if len(fecha) != 10:
            return False

        if fecha[2] != '/' or fecha[5] != '/':
            return False

        dia = fecha[0:2]
        mes = fecha[3:5]
        anio = fecha[6:10]

        if not self.solo_numeros(dia):
            return False

        if not self.solo_numeros(mes):
            return False

        if not self.solo_numeros(anio):
            return False

        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        if dia < 1 or dia > 31:
            return False

        if mes < 1 or mes > 12:
            return False

        if anio < 1900 or anio > 2100:
            return False

        return True

    def solo_numeros(self, texto):
        for c in texto:
            if c < '0' or c > '9':
                return False

        return True