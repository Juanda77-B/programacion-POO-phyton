
from animal import Animal

class Mamifero(Animal):
    def __init__(self, velocidad_galope="45 km/h"):
        super().__init__()
        self.velocidad_galope = velocidad_galope

    # Polimorfismo
    def moverse(self):
        print(f"El {self._nombre} trota y galopa velozmente a {self.velocidad_galope} sobre el pasto.")