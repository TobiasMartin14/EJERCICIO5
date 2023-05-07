
class PlanAhorro ():
    __codigo = None
    __modelo = ''
    __version = ''
    __valor = 0
    cantCuotas = 60
    cantPLicitar = 10


    def __init__(self, codigo,modelo,version,valor):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor

    def actualizarValor (self):
        self.__valor = (self.__valor / self.__cantCuotas) + self.__valor * 0.10

    def __str__(self):
        return f"Código: {self.__codigo}, Modelo: {self.__modelo}, Versión: {self.__version}, Valor: {self.__valor}"

       # return ("Código:", self.__codigo, "Modelo:", self.__modelo, "Versión:", self.__version, "Valor:", self.__valor)

    def setValor(self,nValor):
        self.__valor=nValor
    
    def getValor(self):
        return self.__valor
    
    def getCod(self):
        return self.__codigo
    
    def getMod(self):
        return self.__modelo
    
    def getVer(self):
        return self.__version
    
    @classmethod
    def getCuotasLic(cls):
        return cls.cantPLicitar
    
    @classmethod    
    def getImporteCuota (self):
        return (self.__valor / self.cantCuotas)
    
    @classmethod
    def getCantCuotas(cls):
        return(cls.cantCuotas)

    @classmethod
    def cambiarCuostasPLicitar (cls, nuevacant):
        cls.cantPLicitar = nuevacant