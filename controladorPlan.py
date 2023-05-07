from planAhorro import PlanAhorro
import csv

class ControladorPlan():
    __listaPlanes = []
    def __init__(self):
        self.__listaPlanes = []

    def cargarDatos(self):
        archivo=open("planes.csv")
        reader = csv.reader (archivo, delimiter=";")
            
        for fila in reader:
            cod=int(fila[0])
            mod=str(fila[1])
            ver=str(fila[2])
            val=float(fila[3])
                
            plan = PlanAhorro(cod, mod, ver, val)
            self.__listaPlanes.append(plan)
        print ("El archivo se cargó correctamente")
        archivo.close()

    def mostrarDatos(self): 
        i=0
        while (i < len(self.__listaPlanes)):
            print ("", (self.__listaPlanes[i]))
            i=i+1
    
    def actualizarValor(self):
        for i in range(len(self.__listaPlanes)):
            print ("", (self.__listaPlanes[i]))
            self.__listaPlanes[i].setValor(int(input('Ingrese nuevo valor de vehiculo: ')))
            print ("", (self.__listaPlanes[i]))

    
    def mostrarDatosAutos(self,valor):
        for i in range(len(self.__listaPlanes)):
            if self.__listaPlanes[i].getValor()<valor:
                print ("", (self.__listaPlanes[i]))

    def mostrarMonto(self):
        for i in range(len(self.__listaPlanes)):
            print("Importe del vehiculo con codigo {}: {} \n".format(self.__listaPlanes[i].getCod(), (self.__listaPlanes[i].getCuotasLic() * self.__listaPlanes[i].getImporteCuota())))

    def montoPLicitar (self):
        for i in range (len(self.__listaPlanes)):
            #print("El monto pagado para licitar el vehículo de código {} es: {} " .format((self.__listaPlanes[i].getCod()), (self.__listaPlanes[i].getImporteCuota() * self.__listaPlanes[i].getCuotasLic()) ))
            #print("{}" .format(self.__listaPlanes[i].getCantCuotas()))
            #print("{}" .format(self.__listaPlanes[i].getCuotasLic()))
            cantcuo = self.__listaPlanes[i].getCantCuotas()
            valortot = self.__listaPlanes[i].getValor()
            preciocuo = valortot / cantcuo
            montopagado = preciocuo * self.__listaPlanes[i].getCuotasLic()
            print("El monto pagado para licitar el vehículo de código {} es: {} " .format((self.__listaPlanes[i].getCod()), montopagado) ),

    def modificarCantCuotasPagas(self, codigo):
        indice = 0
        while (self.__listaPlanes[indice].getCod() < codigo):
            indice = indice + 1

        if (indice < len(self.__listaPlanes)):
            self.__listaPlanes[indice].cambiarCuostasPLicitar(int(input("Ingrese la cantidad de cuotas que requiere actualmente para licitar: ")))
        else:
            print("El código ingresado no fue encontrado, vuelva a ingresar un codigo valido.")
        
        print("La cant de cuotas actual para licitar es: ", self.__listaPlanes[indice].getCuotasLic())
