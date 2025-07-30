class Especialidad:
    def __init__(self, id: str, nombre: str):
        self.id = id
        self.nombre = nombre

    def __repr__(self):
        return f"<Especialidad {self.nombre}>"