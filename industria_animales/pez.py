
from animal import Animal

class Pez(Animal):
    def __init__(self, tipo_agua="Dulce tropical"):
        super().__init__()
        self.tipo_agua = tipo_agua

    # Polimorfismo
    def moverse(self):
        print(f"El {self._nombre} nada fluidamente usando sus aletas en agua {self.tipo_agua}.")