
from animal import Animal

class Reptil(Animal):
    def __init__(self, fuerza_mordida="3700 psi"):
        super().__init__()
        self.fuerza_mordida = fuerza_mordida

    # Polimorfismo
    def moverse(self):
        print(f"El {self._nombre} se arrastra sigilosamente por la orilla y nada en el agua.")