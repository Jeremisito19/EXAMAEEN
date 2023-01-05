from paciente import Pacieente
from cedula import Cedula
class Usuario0:
    nombre = str
    apellido = str
    Cedula = Cedula("")
    Pacieente = Pacieente("")
    
    def __init__(self, nombre, apellido, Donante, Cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.Donante = Donante
        self.Cedula = Cedula