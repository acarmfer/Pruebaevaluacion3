class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __str__(self):
        return f"Nave: {self.nombre}, Longitud: {self.longitud}, Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}"

# Función para ordenar la lista de naves por nombre de forma ascendente y por longitud de forma descendente
def ordenar_naves(lista_naves):
    return sorted(lista_naves, key=lambda nave: (nave.nombre, -nave.longitud))

# Función para mostrar toda la información de las naves "Cometa Veloz" y "Titán del Cosmos"
def mostrar_naves_especificas(lista_naves):
    for nave in lista_naves:
        if nave.nombre == "Cometa Veloz" or nave.nombre == "Titán del Cosmos":
            print(nave)

# Función para determinar las cinco naves con mayor cantidad de pasajeros
def cinco_naves_mayor_pasajeros(lista_naves):
    return sorted(lista_naves, key=lambda nave: nave.pasajeros, reverse=True)[:5]

# Función para indicar cuál es la nave que requiere la mayor cantidad de tripulación
def nave_mayor_tripulacion(lista_naves):
    return max(lista_naves, key=lambda nave: nave.tripulantes)

# Función para mostrar todas las naves cuyo nombre comience con "GX"
def naves_nombre_inicio_GX(lista_naves):
    return [nave for nave in lista_naves if nave.nombre.startswith("GX")]

# Función para listar todas las naves que pueden llevar seis o más pasajeros
def naves_seis_mas_pasajeros(lista_naves):
    return [nave for nave in lista_naves if nave.pasajeros >= 6]

# Función para mostrar toda la información de la nave más pequeña y la más grande
def nave_mas_pequena_y_grande(lista_naves):
    nave_mas_pequena = min(lista_naves, key=lambda nave: nave.longitud)
    nave_mas_grande = max(lista_naves, key=lambda nave: nave.longitud)
    return nave_mas_pequena, nave_mas_grande

# Lista de naves espaciales
naves = [
    NaveEspacial("Aurora Estelar", 50, 10, 20),
    NaveEspacial("Cometa Veloz", 40, 8, 15),
    NaveEspacial("Titán del Cosmos", 60, 12, 25),
    NaveEspacial("Galaxia X1", 55, 9, 18),
    NaveEspacial("GX-5000", 70, 15, 30),
    NaveEspacial("Nebulosa Brillante", 45, 7, 12),
    NaveEspacial("GX-7000", 65, 14, 28),
    NaveEspacial("Viajero Espacial", 48, 11, 22)
]

# Ordenar la lista de naves
naves_ordenadas = ordenar_naves(naves)
print("Naves ordenadas por nombre (ascendente) y longitud (descendente):")
for nave in naves_ordenadas:
    print(nave)
print()

# Mostrar información de las naves "Cometa Veloz" y "Titán del Cosmos"
print("Información de las naves 'Cometa Veloz' y 'Titán del Cosmos':")
mostrar_naves_especificas(naves)
print()

# Determinar las cinco naves con mayor cantidad de pasajeros
print("Las cinco naves con mayor cantidad de pasajeros:")
cinco_naves = cinco_naves_mayor_pasajeros(naves)
for nave in cinco_naves:
    print(nave)
print()

# Indicar cuál es la nave que requiere la mayor cantidad de tripulación
nave_max_tripulacion = nave_mayor_tripulacion(naves)
print("Nave con mayor cantidad de tripulación:")
print(nave_max_tripulacion)
print()

# Mostrar todas las naves cuyo nombre comienza con "GX"
print("Naves cuyo nombre comienza con 'GX':")
naves_GX = naves_nombre_inicio_GX(naves)
for nave in naves_GX:
    print(nave)
print()

# Listar todas las naves que pueden llevar seis o más pasajeros
print("Naves que pueden llevar seis o más pasajeros:")
naves_seis_pasajeros = naves_seis_mas_pasajeros(naves)
for nave in naves_seis_pasajeros:
    print(nave)
print()

# Mostrar información de la nave más pequeña y la más grande
nave_pequena, nave_grande = nave_mas_pequena_y_grande(naves)
print("Información de la nave más pequeña:")
print(nave_pequena)
print("Información de la nave más grande:")
print(nave_grande)
