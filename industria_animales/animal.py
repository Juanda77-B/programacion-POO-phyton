
class Animal:
    def __init__(self, nombre="", edad=0, habitat="", dieta="", tamano="", color=""):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._dieta = dieta
        self._tamano = tamano
        self._color = color

    def asignacion_datos(self, nombre, edad, habitat, dieta, tamano, color):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._dieta = dieta
        self._tamano = tamano
        self._color = color

    def moverse(self):
        print(f"El {self._nombre} se desplaza en su hábitat natural ({self._habitat}).")

    def alimentarse(self):
        print(f"El {self._nombre} se alimenta con una dieta {self._dieta}.")

    def mostrar_info(self):
        print(f"--- Animal: {self._nombre} ---")
        print(f"Edad: {self._edad} años | Hábitat: {self._habitat} | Dieta: {self._dieta}")
        print(f"Tamaño: {self._tamano} | Color: {self._color}")