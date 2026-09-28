
from animal import Animal

class Insecto(Animal):
    def __init__(self, cantidad_patas=6, tiene_cuerno=True):
        super().__init__()
        self.cantidad_patas = cantidad_patas
        self.tiene_cuerno = tiene_cuerno

    # Polimorfismo
    def moverse(self):
        print(f"El {self._nombre} trepa por la corteza de los arboles y vuela trechos cortos.")