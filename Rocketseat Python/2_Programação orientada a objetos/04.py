#Classe Abstrata
from abc import abstractmethod, ABC

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def deslidar(self):
        pass


class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        return "Carro ligando..."

    def deslidar(self):
        return "Carro desligando..."

carro1 = Carro()
print(carro1.deslidar())
print(carro1.ligar())