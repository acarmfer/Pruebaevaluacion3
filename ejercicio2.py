# Primero vamos a implementar el cálculo del determinante de una matriz cuadrada 3x3 de manera recursiva
def determinante_recursivo(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for i in range(len(matriz)):
            signo = (-1) ** i
            submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
            det += signo * matriz[0][i] * determinante_recursivo(submatriz)
        return det

# Ejemplo de uso
matriz_ejemplo = [
    [2, -3, 1],
    [4, 0, -2],
    [5, 1, 3]
]
print("Determinante (recursivo):", determinante_recursivo(matriz_ejemplo))

#ahora, vamos a implementar el cálculo del determinante de manera iterativa
def determinante_iterativo(matriz):
    det = 0
    for i in range(len(matriz)):
        prod_principal = 1
        prod_secundaria = 1
        for j in range(len(matriz)):
            prod_principal *= matriz[j][(i + j) % len(matriz)]
            prod_secundaria *= matriz[j][(len(matriz) - j + i - 1) % len(matriz)]
        det += prod_principal
        det -= prod_secundaria
    return det

# Ejemplo de uso
matriz_ejemplo = [
    [2, -3, 1],
    [4, 0, -2],
    [5, 1, 3]
]
print("Determinante (iterativo):", determinante_iterativo(matriz_ejemplo))
def determinante_iterativo(matriz):
    det = 0
    for i in range(len(matriz)):
        prod_principal = 1
        prod_secundaria = 1
        for j in range(len(matriz)):
            prod_principal *= matriz[j][(i + j) % len(matriz)]
            prod_secundaria *= matriz[j][(len(matriz) - j + i - 1) % len(matriz)]
        det += prod_principal
        det -= prod_secundaria
    return det

# Ejemplo de uso
matriz_ejemplo = [
    [2, -3, 1],
    [4, 0, -2],
    [5, 1, 3]
]
print("Determinante (iterativo):", determinante_iterativo(matriz_ejemplo))
