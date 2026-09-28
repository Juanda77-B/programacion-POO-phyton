# botella_vidirio.py
from botella import Botella

class BotellaVidrio(Botella):
    def __init__(self, grosor_vidrio="Grueso", color_vidrio="Transparente"):
        super().__init__()
        self.grosor_vidrio = grosor_vidrio
        self.color_vidrio = color_vidrio

    def resistencia_temperatura(self, temperatura_grados):
        print(f"La botella de vidrio {self.color_vidrio} soporta una temperatura de {temperatura_grados}°C.")

    # Polimorfismo: Sobrescribe el método contener_liquidos
    def contener_liquidos(self):
        print(f"Almacenando bebidas frías/calientes en botella de vidrio {self.color_vidrio} sin alterar el sabor.")