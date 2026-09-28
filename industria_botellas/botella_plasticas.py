# botella_plasticas.py
from botella import Botella

class BotellaPlastica(Botella):
    def __init__(self, tipo_plastico="PET", reutilizable=True):
        super().__init__()
        self.tipo_plastico = tipo_plastico
        self.reutilizable = reutilizable

    # Método específico de botellas plásticas
    def reciclar(self):
        print(f"La botella de plástico tipo {self.tipo_plastico} ha sido enviada al contenedor de reciclaje.")

    # Polimorfismo: Sobrescribe el método mostrar_info
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Plástico: {self.tipo_plastico} | Reutilizable: {self.reutilizable}")
