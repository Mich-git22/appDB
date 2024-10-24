import tkinter as tk
import requests


# Función para obtener el último registro desde la API
def obtener_ultimo_registro():
    url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            ultimo_registro = data[-1]  # Obtenemos el último registro
            mostrar_registro(ultimo_registro)
        else:
            label_resultado.config(text="No hay datos en la base de datos.")
    else:
        label_resultado.config(text="Error al obtener los datos.")


# Función para mostrar el último registro en la ventana
def mostrar_registro(registro):
    texto = f"ID: {registro['id']}\nNombre: {registro['nombre']}\nApellido: {registro['apellido']}\nCiudad: {registro['ciudad']}\nCalle: {registro['calle']}"
    label_resultado.config(text=texto)


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Último Registro")
ventana.geometry("300x200")

# Etiqueta que mostrará el resultado
label_resultado = tk.Label(ventana, text="", justify="left")
label_resultado.pack(pady=20)

# Botón para actualizar el último registro
boton_actualizar = tk.Button(ventana, text="Obtener Último Registro", command=obtener_ultimo_registro)
boton_actualizar.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()