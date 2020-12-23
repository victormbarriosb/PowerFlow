# Victor Barrios 12/23/2020
from ElementosSEP import *

# Creando Barra
A = Barra(1, 1, 230, potenciadesarrollada=Potencia(0.5, 0.3099))
B = Barra(2, 3, 230, potenciadesarrollada=Potencia(1.7, 1.0535))
C = Barra(3, 3, 230, potenciadesarrollada=Potencia(2, 1.2394))

L1 = Linea(A, B, Impedancia(0, 1))
L2 = Linea(A, C, Impedancia(0, 1))
L3 = Linea(B, C, Impedancia(0, 1))

SistemaElectrico = SEP()

SistemaElectrico.AgregarNodo(A)
SistemaElectrico.AgregarNodo(B)
SistemaElectrico.AgregarNodo(C)

SistemaElectrico.AgregarLinea(L1)
SistemaElectrico.AgregarLinea(L2)
SistemaElectrico.AgregarLinea(L3)
