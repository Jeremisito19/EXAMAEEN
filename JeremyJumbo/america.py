from horapais import hora
from region import Pais

class Continente(hora):
    nombreC     = str
    hora        = hora("")
    Pais        = Pais("","")

    def __init__(self, nombreC, hora, Pais):
        self.nombreC     = nombreC
        self.hora        = hora
        self.Pais        = Pais
