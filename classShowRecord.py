class ShowRecord:
    def __init__(self, label):
        self.label = label

    def mostrar_registro(self, registro):
        if registro:
            texto = (f"ID: {registro['id']}\nNombre: {registro['nombre']}\n"
                     f"Apellido: {registro['apellido']}\nCiudad: {registro['ciudad']}\nCalle: {registro['calle']}")
            self.label.config(text=texto)
        else:
            self.label.config(text="No hay datos en la base de datos.")
