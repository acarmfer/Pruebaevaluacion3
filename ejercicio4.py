class Termino:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente

    def __str__(self):
        if self.exponente == 0:
            return str(self.coeficiente)
        elif self.exponente == 1:
            return f"{self.coeficiente}x"
        else:
            return f"{self.coeficiente}x^{self.exponente}"

class Polinomio:
    def __init__(self, terminos):
        self.terminos = terminos

    def __str__(self):
        polinomio_str = ""
        for i, termino in enumerate(self.terminos):
            if i == 0:
                polinomio_str += str(termino)
            else:
                if termino.coeficiente >= 0:
                    polinomio_str += f" + {termino}"
                else:
                    polinomio_str += f" - {abs(termino.coeficiente)}x^{termino.exponente}"
        return polinomio_str

    def restar(self, otro_polinomio):
        resultado_terminos = []
        for termino in self.terminos:
            resultado_terminos.append(Termino(termino.coeficiente, termino.exponente))

        for termino in otro_polinomio.terminos:
            encontrado = False
            for i, t in enumerate(resultado_terminos):
                if t.exponente == termino.exponente:
                    resultado_terminos[i].coeficiente -= termino.coeficiente
                    encontrado = True
                    break
            if not encontrado:
                resultado_terminos.append(Termino(-termino.coeficiente, termino.exponente))

        resultado_polinomio = Polinomio(resultado_terminos)
        return resultado_polinomio

    def dividir(self, divisor):
        cociente_terminos = []
        residuo = self

        while residuo.terminos[0].exponente >= divisor.terminos[0].exponente:
            cociente_coeficiente = residuo.terminos[0].coeficiente / divisor.terminos[0].coeficiente
            cociente_exponente = residuo.terminos[0].exponente - divisor.terminos[0].exponente

            cociente_termino = Termino(cociente_coeficiente, cociente_exponente)
            cociente_terminos.append(cociente_termino)

            cociente_parcial = Polinomio([cociente_termino])
            residuo = residuo.restar(divisor.multiplicar(cociente_parcial))

        cociente = Polinomio(cociente_terminos)
        return cociente, residuo

    def eliminar_termino(self, exponente):
        nuevos_terminos = [termino for termino in self.terminos if termino.exponente != exponente]
        return Polinomio(nuevos_terminos)

    def buscar_termino(self, exponente):
        for termino in self.terminos:
            if termino.exponente == exponente:
                return True
        return False

    def multiplicar(self, otro_polinomio):
        nuevos_terminos = []
        for t1 in self.terminos:
            for t2 in otro_polinomio.terminos:
                nuevo_coeficiente = t1.coeficiente * t2.coeficiente
                nuevo_exponente = t1.exponente + t2.exponente
                nuevo_termino = Termino(nuevo_coeficiente, nuevo_exponente)
                nuevos_terminos.append(nuevo_termino)
        return Polinomio(nuevos_terminos)

# Ejemplo de uso
terminos_polinomio_1 = [Termino(3, 2), Termino(5, 1), Termino(7, 0)]
polinomio_1 = Polinomio(terminos_polinomio_1)
print("Polinomio 1:", polinomio_1)

terminos_polinomio_2 = [Termino(2, 2), Termino(4, 1), Termino(6, 0)]
polinomio_2 = Polinomio(terminos_polinomio_2)
print("Polinomio 2:", polinomio_2)

# Restar dos polinomios
resultado_resta = polinomio_1.restar(polinomio_2)
print("Resta de polinomios:", resultado_resta)

# Dividir dos polinomios
cociente, residuo = polinomio_1.dividir(polinomio_2)
print("División de polinomios:")
print("Cociente:", cociente)
print("Residuo:", residuo)

# Eliminar un término de un polinomio
exponente_a_eliminar = 1
polinomio_sin_termino = polinomio_1.eliminar_termino(exponente_a_eliminar)
print(f"Polinomio 1 sin término con exponente {exponente_a_eliminar}:", polinomio_sin_termino)

# Determinar si un término específico existe en un polinomio
exponente_a_buscar = 2
print(f"¿El término con exponente {exponente_a_buscar} existe en el polinomio 1?:", polinomio_1.buscar_termino(exponente_a_buscar))
print(f"¿El término con exponente {exponente_a_buscar} existe en el polinomio 2?:", polinomio_2.buscar_termino(exponente_a_buscar))
