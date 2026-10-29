#exemplo de uso de staticmethod

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b




print(Matematica.somar(a=20, b=30))