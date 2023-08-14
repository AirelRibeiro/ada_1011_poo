class Fracao:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

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

    # Getters e Setters para numerador
    def get_numerador(self):
        return self.__numerador

    def set_numerador(self, numerador):
        self.__numerador = numerador

    # Getters e Setters para denominador
    def get_denominador(self):
        return self.__denominador

    def set_denominador(self, denominador):
        self.__denominador = denominador

    def __add__(self, fracao):
        if self.__denominador == fracao.denominador:
            soma = self.__numerador + fracao.numerador
            return f"{soma}/{fracao.denominador}"
        else:
            mmc = Fracao.calcula_mmc(self.__denominador, fracao.denominador)
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador1 + numerador2}/{mmc}"

    def __sub__(self, fracao):
        if self.__denominador == fracao.denominador:
            subtracao = self.__numerador - fracao.numerador
            return f"{subtracao}/{fracao.denominador}"
        else:
            mmc = Fracao.calcula_mmc(self.__denominador, fracao.denominador)
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador1 - numerador2}/{mmc}"

    def __mul__(self, fracao):
        numerador = self.__numerador * fracao.numerador
        denominador = self.__denominador * fracao.denominador
        return f"{numerador}/{denominador}"

    def __truediv__(self, fracao):
        numerador = self.__numerador * fracao.denominador
        denominador = self.__denominador * fracao.numerador
        return f"{numerador}/{denominador}"

    numerador = property(get_numerador, set_numerador)
    denominador = property(get_denominador, set_denominador)


class Fracao_O_Retorno:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

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

    # Getters e Setters para numerador
    def get_numerador(self):
        return self.__numerador

    def set_numerador(self, numerador):
        self.__numerador = numerador

    # Getters e Setters para denominador
    def get_denominador(self):
        return self.__denominador

    def set_denominador(self, denominador):
        self.__denominador = denominador

    def __add__(self, fracao):
        if self.__denominador == fracao.denominador:
            soma = self.__numerador + fracao.numerador
            return f"{soma}/{fracao.denominador}"
        else:
            mmc = Fracao.calcula_mmc(self.__denominador, fracao.denominador)
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador1 + numerador2}/{mmc}"

    def __sub__(self, fracao):
        if self.__denominador == fracao.denominador:
            subtracao = self.__numerador - fracao.numerador
            return f"{subtracao}/{fracao.denominador}"
        else:
            mmc = Fracao.calcula_mmc(self.__denominador, fracao.denominador)
            numerador1 = Fracao.calcula_numerador(
                mmc, self.__denominador, self.__numerador
            )
            numerador2 = Fracao.calcula_numerador(
                mmc, fracao.denominador, fracao.numerador
            )
            return f"{numerador1 - numerador2}/{mmc}"

    def __mul__(self, fracao):
        numerador = self.__numerador * fracao.numerador
        denominador = self.__denominador * fracao.denominador
        return Fracao(numerador, denominador)

    def __truediv__(self, fracao):
        numerador = self.__numerador * fracao.denominador
        denominador = self.__denominador * fracao.numerador
        return f"{numerador}/{denominador}"

    numerador = property(get_numerador, set_numerador)
    denominador = property(get_denominador, set_denominador)


fracao1 = Fracao(5, 8)
fracao2 = Fracao_O_Retorno(2, 5)

fracao3 = fracao1 * fracao2

print(fracao1 + fracao2)
print(fracao1 - fracao2)
print(fracao3)  # objeto(fracao2).metodo(__mul__)(fracao1)
print(fracao1 / fracao2)
