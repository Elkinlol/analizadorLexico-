from validaciones.correo import ValidadorCorreo
from validaciones.telefono import ValidadorTelefono
from validaciones.placa import ValidadorPlaca

class DetectorTexto:

    def __init__(self):
        self.validador_correo = ValidadorCorreo()
        self.validador_telefono = ValidadorTelefono()
        self.validador_placa = ValidadorPlaca()

    def analizar(self, texto):

        palabras = texto.split()

        resultados = {
            "correos": [],
            "telefonos": [],
            "placas": []
        }

        for palabra in palabras:

            palabra = palabra.strip(',.;:')

            if self.validador_correo.validar(palabra):
                resultados["correos"].append(palabra)

            if self.validador_telefono.validar(palabra):
                resultados["telefonos"].append(palabra)

            if self.validador_placa.validar(palabra):
                resultados["placas"].append(palabra)

        return resultados