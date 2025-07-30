class Paciente:
    def __init__(self, id: str, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.email = email

    def __repr__(self):
        return f"<Paciente {self.nombre} - {self.email}>"