import sys
sys.stdout.reconfigure(encoding='utf-8')

from mamifero import Mamifero
from reptil import Reptil
from pez import Pez
from insecto import Insecto
from ave import Ave

print("         SISTEMA DE GESTIoN DE ANIMALES           ")

# 1. Caballo
caballo = Mamifero(velocidad_galope="50 km/h")
caballo.asignacion_datos("Caballo Pura Sangre", 6, "Pradera", "Herbivora", "Grande", "Marron")
caballo.mostrar_info()
caballo.moverse()

print("\n" + "-" * 50 + "\n")

# 2. Cocodrilo
cocodrilo = Reptil(fuerza_mordida="3700 psi")
cocodrilo.asignacion_datos("Cocodrilo de Cienaga", 10, "Rios y Pantanos", "Carnivora", "Grande", "Verde Oscuro")
cocodrilo.mostrar_info()
cocodrilo.moverse()

print("\n" + "-" * 50 + "\n")

# 3. Pez Disco
pez = Pez(tipo_agua="Dulce de Rio Amazonas")
pez.asignacion_datos("Pez Disco", 1, "Rios Neotropicales", "Omnivora", "Pequeño", "Azul y Naranja")
pez.mostrar_info()
pez.moverse()

print("\n" + "-" * 50 + "\n")

# 4. Escarabajo
escarabajo = Insecto(cantidad_patas=6, tiene_cuerno=True)
escarabajo.asignacion_datos("Escarabajo Rinoceronte", 1, "Bosque Tropical", "Herbivora", "Muy Pequeño", "Cafe Brillante")
escarabajo.mostrar_info()
escarabajo.moverse()

print("\n" + "-" * 50 + "\n")

# 5. Pato
pato = Ave(envergadura_alas="85 cm")
pato.asignacion_datos("Pato Real", 2, "Lagos y Humedales", "Omnivora", "Pequeño", "Verde, Blanco y Cafe")
pato.mostrar_info()
pato.moverse()

