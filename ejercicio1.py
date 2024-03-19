#Para  implementar la representación de las piedras preciosas
class PiedraPreciosa:
    def __init__(self, tamaño):
        self.tamaño = tamaño

    def __str__(self):
        return f"Piedra de tamaño {self.tamaño}"

    def __lt__(self, otra_piedra):
        return self.tamaño < otra_piedra.tamaño

#se crean las dos columnas donde se apilarán las piedra
class Columna:
    def __init__(self):
        self.piedras = []

    def agregar_piedra(self, piedra):
        self.piedras.append(piedra)

    def quitar_piedra(self):
        if self.piedras:
            return self.piedras.pop()

    def __str__(self):
        return ", ".join(str(piedra) for piedra in self.piedras)

#podemos crear las piedras preciosas y las columnas para el juego
def crear_piedras(num_piedras):
    piedras = [PiedraPreciosa(i) for i in range(num_piedras, 0, -1)]
    return piedras

def crear_piramide(num_piedras):
    piramide = Columna()
    piedras = crear_piedras(num_piedras)
    for piedra in piedras:
        piramide.agregar_piedra(piedra)
    return piramide

def mostrar_estado(piramide_1, piramide_2):
    print("Pirámide 1:", piramide_1)
    print("Pirámide 2:", piramide_2)

#podemos proceder a resolver el puzzle implementando las reglas del juego

def mover_piedra(origen, destino):
    piedra = origen.quitar_piedra()
    if piedra is not None:
        if not destino.piedras or piedra < destino.piedras[-1]:
            destino.agregar_piedra(piedra)
            return True
        else:
            origen.agregar_piedra(piedra)
            print("No se puede colocar una piedra más grande sobre una más pequeña.")
            return False
    else:
        print("No hay piedras para mover.")
        return False

def resolver_puzzle(piramide_origen, piramide_destino, num_piedras):
    if num_piedras % 2 == 0:
        piramides = (piramide_origen, piramide_destino)
    else:
        piramides = (piramide_destino, piramide_origen)

    mostrar_estado(piramide_origen, piramide_destino)
    for i in range(2**num_piedras - 1):
        if i % 2 == 0:
            mover_piedra(piramides[0], piramides[1])
        else:
            mover_piedra(piramides[1], piramides[0])
        mostrar_estado(piramide_origen, piramide_destino)

# Crear las dos pirámides iniciales
piramide_origen = crear_piramide(4)
piramide_destino = Columna()

# Resolver el puzzle
resolver_puzzle(piramide_origen, piramide_destino, 4)
