class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f"A área do Triangulo é {(self.base * self.altura) / 2}"
