from america import Continente
from horapais import hora
from region import Pais
from paciente import Pacieente
from cedula import Cedula
from migrante import Usuario0




class Cedula1:
    nombre            = str
    apellido          = str
    edad              = int
    tipoDeSangre      = str
    madre             = str
    padre             = str
    fechaDeNacimineto = int 
    donante           = str 
    

    def __init__(self, nombre, apellido, edad, tipoDeSangre, madre, padre, fechaDeNacimiento, donante,):
        self.nombre                = nombre
        self.apellido              = apellido
        self.edad                  = edad
        self.tipoDeSangre          = tipoDeSangre
        self.madre                 = madre
        self.padre                 = padre
        self.fechaDeNacimineto     = fechaDeNacimiento
        self.donante               = donante

    def __str__(self):
        return f'cedula de {self.nombre} {self.apellido}, edad {self.edad}, su tipo de sangre {self.tipoDeSangre}, su madre es {self.madre}, su padre es {self.padre}, fecha de naciomiento {self.fechaDeNacimineto}, dondante {self.donante}'
class Imprimir2(Cedula1):
    ciudad = str

    def __init__(self, nombre, apellido, edad, tipoDeSangre, madre, padre, fechaDeNacimiento, donante, numeroDeCedula, ciudad):
        super().__init__(nombre, apellido, edad, tipoDeSangre, madre, padre, fechaDeNacimiento, donante, numeroDeCedula)
        self.ciudad = ciudad


class usuario:
    nombre               = str
    apellido             = str
    cedula               = int
    tipoDeSangre         = str
    Madre                = str
    Padre                = str

    def __init__(self, nombre, apellido, cedula, tipoDeSangre, Madre, Padre):
        self.nombre                 = nombre
        self.apellido               = apellido
        self.cedula                 = cedula
        self.tipoDeSangre           = tipoDeSangre
        self.Madre                  = Madre
        self.Padre                  = Padre
        
    def imprimir(self):
        print(self.nombre, self.apellido, self.cedula, self.tipoDeSangre, self.Madre, self.Padre)

x = usuario("Susa", "Nahoria", 1709722779, "O+", "Daniela", "Dennis")
x.imprimir()


class  donante(usuario):
    donante = str
    def __init__(self, nombre, apellido, cedula, tipoDeSangre, Madre, Padre, numeroDeCedula, donante):
        super().__init__(nombre, apellido, cedula, tipoDeSangre, Madre, Padre)
        self.donante = donante



class HoraDeRegistro(Continente):
    tipoDeRegistro = str
    nombre          = str
    apellido        = str
    Continente      = Continente("","", "")
    Usuario         = Usuario0("", "","","")
    def __init__(self, nombreC, hora, tipoDeRegistro, nombre, Continente, Usuario):
        super().__init__(nombreC, hora, Pais)
        self.tipoDeReguistro = tipoDeRegistro
        self.nombre          = nombre
        self.Continente      = Continente   
        self.Usuario         = Usuario
        


    


#herencia entre archivos

if __name__ == "__main__":
    #metodo str 
    ejercicio2 = Imprimir2("Dilana","Salazar", 18, "O+", "Mercedes", "Cruz", 2004, "si", 170975134576, "quito")
    print(ejercicio2)
    #herencia entre archivos de 2 objetos +
    ejercicio3 = HoraDeRegistro("Ecuador", "06:00", "Documento de Identidad", "Jeremy Jumbo", Continente("america", hora("19:00"), Pais("Ecuador", "Ambato")))
    print(vars(ejercicio3))
    print(vars(ejercicio3.Continente))
    print(vars(ejercicio3.Continente.hora))
    print(vars(ejercicio3.Continente.Pais))
    
