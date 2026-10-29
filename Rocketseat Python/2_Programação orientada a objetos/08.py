#Exemplo de uso do classmethod
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_instancia(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))



configuracao = "FIAT,UNO,2002"

carro1 = Carro.criar_instancia(configuracao)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno:{carro1.ano}")