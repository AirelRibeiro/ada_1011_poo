class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return f"A área do quadrado é {self.lado * self.lado}"


class Quadrados:
    @staticmethod
    def area(lado):
        return f"A área do quadrado é {lado * lado}"
