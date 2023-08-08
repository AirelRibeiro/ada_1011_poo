class Losango:
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def area(self):
        return f"A área do losango é {(self.horizontal * self.vertical) / 2}"
