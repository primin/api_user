from utils.DateFormat import DateFormat

class Usuario():
    def __init__(self, id_usuario, nombre=None, primer_apellido=None, segundo_apellido=None, cedula_identidad=None, fecha_nacimiento=None) -> None:
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.cedula_identidad = cedula_identidad
        self.fecha_nacimiento = fecha_nacimiento
        
    def to_JSON(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'primer_apellido': self.primer_apellido,
            'segundo_apellido': self.segundo_apellido,
            'cedula_identidad': self.cedula_identidad,
            'fecha_nacimiento': DateFormat.convert_date(self.fecha_nacimiento)
        }