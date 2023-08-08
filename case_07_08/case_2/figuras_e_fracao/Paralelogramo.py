class Paralelogramo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f"A área do paralelogramo é {self.base * self.altura}"
