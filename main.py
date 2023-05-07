from planAhorro import PlanAhorro
from controladorPlan import ControladorPlan
from menu import Menu 
import csv

def test ():
    plan = ControladorPlan()
    plan.cargarDatos()
    plan.mostrarDatos()
    menu = Menu()
    menu.opciones(plan)

if __name__ == '__main__':
    test ()