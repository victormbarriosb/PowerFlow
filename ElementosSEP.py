from ElementosGeometricos import *
from PropiedadesElectricas import *


class Barra:
    def __init__(self, numero, tipo, basekv=0, potenciagenerada=Potencia(), potenciadesarrollada=Potencia(),
                 admitancia=Admitancia(), ubicacion=Punto(), voltaje=Voltaje()):
        self.Voltaje = voltaje
        self.Ubicacion = ubicacion
        self.admitancia = admitancia
        self.baseKV = basekv
        self.potenciaDesarrollada = potenciadesarrollada
        self.potenciaGenerada = potenciagenerada
        self.Id = numero
        self.Tipo = tipo


class Linea:
    def __init__(self, barraa, barrab, impedancia=Impedancia(), admitancia=Admitancia()):
        self.BarraA = barraa
        self.BarraB = barrab
        self.Impedancia = impedancia
        self.Admitancia = admitancia


class SEP:

    Nodos = []
    Lineas = []

    def __init__(self):
        pass

    def AgregarNodo(self, barra):
        self.Nodos.append(barra)

    def AgregarLinea(self, linea):
        self.Lineas.append(linea)
