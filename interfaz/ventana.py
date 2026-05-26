import tkinter as tk
from tkinter import messagebox

from validaciones.correo import ValidadorCorreo
from validaciones.telefono import ValidadorTelefono
from validaciones.fecha import ValidadorFecha
from validaciones.password import ValidadorPassword
from validaciones.placa import ValidadorPlaca
from analizador.detector_texto import DetectorTexto


def iniciar_app():

    ventana = tk.Tk()
    ventana.title("Validador de Patrones")
    ventana.geometry("700x700")
    correo_validator = ValidadorCorreo()
    telefono_validator = ValidadorTelefono()
    fecha_validator = ValidadorFecha()
    password_validator = ValidadorPassword()
    placa_validator = ValidadorPlaca()
    detector = DetectorTexto()

    titulo = tk.Label(
        ventana,
        text="Sistema de Validación de Patrones",
        font=("Arial", 18)
    )
    titulo.pack(pady=10)

    # CORREO
    tk.Label(ventana, text="Correo:").pack()
    entrada_correo = tk.Entry(ventana, width=40)
    entrada_correo.pack()

    # TELEFONO
    tk.Label(ventana, text="Teléfono:").pack()
    entrada_telefono = tk.Entry(ventana, width=40)
    entrada_telefono.pack()

    # FECHA
    tk.Label(ventana, text="Fecha DD/MM/AAAA:").pack()
    entrada_fecha = tk.Entry(ventana, width=40)
    entrada_fecha.pack()

    # PASSWORD
    tk.Label(ventana, text="Contraseña:").pack()
    entrada_password = tk.Entry(ventana, width=40, show="*")
    entrada_password.pack()

    # PLACA
    tk.Label(ventana, text="Placa:").pack()
    entrada_placa = tk.Entry(ventana, width=40)
    entrada_placa.pack()

    resultado = tk.Label(ventana, text="", fg="blue")
    resultado.pack(pady=10)

    def validar_datos():

        mensaje = ""

        correo = entrada_correo.get()
        telefono = entrada_telefono.get()
        fecha = entrada_fecha.get()
        password = entrada_password.get()
        placa = entrada_placa.get()

        mensaje += f"Correo: {'Válido' if correo_validator.validar(correo) else 'Inválido'}\n"

        mensaje += f"Teléfono: {'Válido' if telefono_validator.validar(telefono) else 'Inválido'}\n"

        mensaje += f"Fecha: {'Válida' if fecha_validator.validar(fecha) else 'Inválida'}\n"

        mensaje += f"Contraseña: {'Válida' if password_validator.validar(password) else 'Inválida'}\n"

        mensaje += f"Placa: {'Válida' if placa_validator.validar(placa) else 'Inválida'}\n"

        resultado.config(text=mensaje)

    boton_validar = tk.Button(
        ventana,
        text="Validar",
        command=validar_datos
    )

    boton_validar.pack(pady=10)

    # ANALIZADOR DE TEXTO

    tk.Label(
        ventana,
        text="Analizador de Texto",
        font=("Arial", 14)
    ).pack(pady=10)

    texto = tk.Text(ventana, height=10, width=70)
    texto.pack()
    
    def analizar_texto():

        contenido = texto.get("1.0", tk.END)

        resultados = detector.analizar(contenido)

        mensaje = "RESULTADOS\n\n"

        mensaje += "Correos encontrados:\n"
        for correo in resultados["correos"]:
            mensaje += f"- {correo}\n"

        mensaje += "\nTeléfonos encontrados:\n"
        for telefono in resultados["telefonos"]:
            mensaje += f"- {telefono}\n"

        mensaje += "\nPlacas encontradas:\n"
        for placa in resultados["placas"]:
            mensaje += f"- {placa}\n"

        messagebox.showinfo("Resultados", mensaje)

    boton_analizar = tk.Button(
        ventana,
        text="Analizar Texto",
        command=analizar_texto
    )

    boton_analizar.pack(pady=10)

    ventana.mainloop()