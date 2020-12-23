class Potencia:
    def __init__(self, activa, reactiva):
        self.Activa = activa
        self.Reactiva = reactiva

    def __add__(self, other):
        return Potencia(self.Activa + other.Activa, self.Reactiva + other.Reactiva)


class Barra:
    def __init__(self, numero, tipo, PotenciaGenerada, PotenciaDesarrollada, Admitancia, BaseKV):
        self.Id = numero
        self.Tipo = tipo

    def PotenciaGenerada(self, activa, reactiva):
        self.Pg = activa
        self.Qg = reactiva


class Linea:
    def __init__(self, barraA, barraB, impedancia, admitancia):
        self.BarraA = barraA
        self.BarraB = barraB
        self.Impedancia = impedancia
        self.Admitancia = admitancia


class SEP:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
