class Ingrediente:
    def __init__(self, nome, caloria, proteina, gordura, carboidrato):
        self.__nome = nome
        self.proteina = proteina
        self.gordura = gordura
        self.carboidrato = carboidrato
        self.calorias = caloria

    def getnome(self):
        return self.__nome

    def __eq__(self, other):
        if isinstance(other, Ingrediente):
            if other.getnome() == self.__nome:
                return True
        return False

    def __ne__(self, other):
        if isinstance(other, Ingrediente):
            if other.getnome() == self.__nome:
                return False
        return True

    def __str__(self):
        return f"{self.__nome} {self.calorias}Kcal"


class Refeicao:
    def __init__(self, nome, ingredientes: list):
        self.__nome = nome
        self.ingredientes = ingredientes

    def getnome(self):
        return self.__nome

    def __eq__(self, other):
        if isinstance(other, Refeicao):
            if other.getnome() == self.__nome:
                return True
        return False

    def __ne__(self, other):
        if isinstance(other, Refeicao):
            if other.getnome() == self.__nome:
                return False
        return True

    def __str__(self):
        return f"{self.__nome}"
