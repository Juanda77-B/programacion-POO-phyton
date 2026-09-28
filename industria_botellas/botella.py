# botella.py

class Botella:
    def __init__(self, material="", capacidad="", forma="", diseno="", tapa="", grabados=""):
        # Atributos iniciales
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados

    def asignacion_material(self, dato_material, dato_capacidad, dato_forma, dato_diseno, dato_tapa, dato_grabados):
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma
        self.diseno = dato_diseno
        self.tapa = dato_tapa
        self.grabados = dato_grabados
        print(f"La botella es de {self.material}, capacidad {self.capacidad}, forma {self.forma}, tapa {self.tapa}.")

    def contener_liquidos(self):
        print(f"La botella de {self.material} está conteniendo líquido de manera segura.")

    def facilitar_vertido(self):
        print(f"Facilitando el vertido con su diseño {self.diseno}.")

    def cierre_hermetico(self):
        print(f"Cierre hermético con tapa de tipo: {self.tapa}.")

    def mostrar_info(self):
        print(f"--- Datos de Botella ---")
        print(f"Material: {self.material} | Capacidad: {self.capacidad} | Forma: {self.forma} | Tapa: {self.tapa}")