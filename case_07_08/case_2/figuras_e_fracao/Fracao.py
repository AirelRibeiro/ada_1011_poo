class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    @staticmethod
    def calcula_mmc(num1, num2):
        maior = max(num1, num2)
        while True:
            if maior % num1 == 0 and maior % num2 == 0:
                return maior
            else:
                maior += 1

    @staticmethod
    def calcula_numerador(mmc, denominador, numerador):
        return (mmc / denominador) * numerador

    def soma(self, fracao):
        if self.denominador == fracao.denominador:
            soma = self.numerador + fracao.numerador
            return f"{soma}/{fracao.denominador}"
        else:
            mmc = self.calcula_mmc(self.denominador, fracao.denominador)
            numerador_1 = self.calcula_numerador(
                mmc, self.denominador, self.numerador
            )
            numerador_2 = self.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador_1 + numerador_2}/{mmc}"

    def subtracao(self, fracao):
        if self.denominador == fracao.denominador:
            subtracao = self.numerador - fracao.numerador
            return f"{subtracao}/{fracao.denominador}"
        else:
            mmc = self.calcula_mmc(self.denominador, fracao.denominador)
            numerador_1 = self.calcula_numerador(
                mmc, self.denominador, self.numerador
            )
            numerador_2 = self.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador_1 - numerador_2}/{mmc}"

    def multiplicacao(self, fracao):
        numerador = self.numerador * fracao.numerador
        denominador = self.denominador * fracao.denominador
        return f"{numerador}/{denominador}"

    def divisao(self, fracao):
        numerador = self.numerador * fracao.denominador
        denominador = self.denominador * fracao.numerador
        return f"{numerador}/{denominador}"
