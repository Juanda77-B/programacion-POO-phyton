
from animal import Animal

class Ave(Animal):
    def __init__(self, envergadura_alas="80 cm"):
        super().__init__()
        self.envergadura_alas = envergadura_alas

    # Polimorfismo
    def moverse(self):
        print(f"El {self._nombre} vuela con sus alas de {self.envergadura_alas} y acuatiza en el lago.")