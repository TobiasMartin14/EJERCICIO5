from controladorPlan import ControladorPlan
from planAhorro import PlanAhorro

class Menu:
    __opcion = 0
    def __init__ (self):
        self.__opcion = 0
    def opciones(self, p):
        Y = True
        while (Y == True):
            print ("Opcion 1: Actualizar el valor del vehículo de cada plan")
            print ("Opcion 2: Planes de menor valor")
            print ("Opcion 3: Mostrar monto pagado para licitar")
            print ("Opcion 4: Modificar la cantidad de cuotas para licitar")
            print ("Opcion 5: Salir")

            self.__opcion = int(input("Seleccione una opcion: "))
            if (self.__opcion == 1):
                p.actualizarValor()
            elif (self.__opcion == 2):
                p.mostrarDatosAutos(int(input("Ingrese el valor: ")))
            elif (self.__opcion == 3):
               # p.mostrarMonto()
               p.montoPLicitar()
            elif (self.__opcion == 4):
                p.modificarCantCuotasPagas(int(input("Ingrese el codigo del plan a cambiar la cantidad de cuotas: ")))
            elif(self.__opcion == 5):
                Y = False
            else:
                print("La opcion ingresada no es valida.")