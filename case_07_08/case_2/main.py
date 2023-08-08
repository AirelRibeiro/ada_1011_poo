from figuras_e_fracao import *

# from figuras_e_fracao.Quadrado import Quadrados

quadrado = Quadrado(4)
retangulo = Retangulo(4, 6)
triangulo = Triangulo(4, 6)
paralelogramo = Paralelogramo(4, 6)
losango = Losango(4, 6)
trapezio = Trapezio(8, 4, 6)

# print(Quadrados.area(4))

fracao_1 = Fracao(2, 5)
fracao_2 = Fracao(3, 6)

print("\n\n---------Áreas das figuras planas---------\n")
print(quadrado.area())
print(retangulo.area())
print(triangulo.area())
print(paralelogramo.area())
print(losango.area())
print(trapezio.area())

print("\n\n---------Operações com frações---------\n")
print(fracao_1.soma(fracao_2))
print(fracao_1.subtracao(fracao_2))
print(fracao_1.multiplicacao(fracao_2))
print(fracao_1.divisao(fracao_2))
