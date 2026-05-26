from validaciones.correo import ValidadorCorreo
from validaciones.telefono import ValidadorTelefono
from validaciones.fecha import ValidadorFecha
from validaciones.password import ValidadorPassword
from validaciones.placa import ValidadorPlaca

correo = ValidadorCorreo()
telefono = ValidadorTelefono()
fecha = ValidadorFecha()
password = ValidadorPassword()
placa = ValidadorPlaca()

print(" PRUEBAS POSITIVAS Y NEGATIVAS ")

print(correo.validar("usuario@gmail.com"))
print(correo.validar("usuariogmail.com"))

print(telefono.validar("3001234567"))
print(telefono.validar("12345"))

print(fecha.validar("12/05/2026"))
print(fecha.validar("45/13/2026"))

print(password.validar("Admin123*"))
print(password.validar("abc"))

print(placa.validar("ABC123"))
print(placa.validar("12ABC3"))