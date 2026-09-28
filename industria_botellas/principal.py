# principal.py
from botella import Botella
from botella_plasticas import BotellaPlastica
from botella_vidirio import BotellaVidrio

# Instancia de la clase base
botella_generica = Botella()
botella_generica.asignacion_material("Aluminio", "600ml", "Cilíndrica", "Liso", "Roscada", "Sin grabado")
botella_generica.mostrar_info()

print("\n" + "-" * 50 + "\n")

# Instancia de BotellaPlastica
botella_agua = BotellaPlastica(tipo_plastico="PET 1", reutilizable=True)
botella_agua.asignacion_material("Plástico", "500ml", "Ergonómica", "Con relieve", "Chupón", "Logo Marca")
botella_agua.mostrar_info()
botella_agua.contener_liquidos()
botella_agua.reciclar()

print("\n" + "-" * 50 + "\n")

# Instancia de BotellaVidrio
botella_vino = BotellaVidrio(grosor_vidrio="Reforzado", color_vidrio="Verde Oscuro")
botella_vino.asignacion_material("Vidrio", "750ml", "Bordelesa", "Elegante", "Corcho", "Grabado de Reserva")
botella_vino.mostrar_info()
botella_vino.contener_liquidos()
botella_vino.resistencia_temperatura(65)

print("\n" + "=" * 50)