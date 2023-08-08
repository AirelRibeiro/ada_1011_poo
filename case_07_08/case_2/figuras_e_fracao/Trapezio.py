class Trapezio:
    def __init__(self, base_maior, base_menor, altura):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return f"A área do trapézio é {((self.base_menor + self.base_maior) * self.altura) / 2}"
