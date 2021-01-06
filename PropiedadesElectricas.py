class Potencia:
    def __init__(self, activa=0, reactiva=0):
        self.Activa = activa
        self.Reactiva = reactiva

    # Test
    def __add__(self, other):
        return Potencia(self.Activa + other.Activa, self.Reactiva + other.Reactiva)

    #def imprimir(self):
    #    print("Activa %.2f, Reactiva %.2f" % (self.Activa, self.Reactiva))


class Impedancia:
    def __init__(self, resistencia=0, reactancia=0):
        self.Reactancia = reactancia
        self.Resistencia = resistencia


class Admitancia:
    def __init__(self, conductancia=0, susceptancia=0):
        self.Conductancia = conductancia
        self.Susceptancia = susceptancia


class Voltaje:
    def __init__(self, magnitud=1, angulo=0):
        self.Magnitud = magnitud
        self.Angulo = angulo
