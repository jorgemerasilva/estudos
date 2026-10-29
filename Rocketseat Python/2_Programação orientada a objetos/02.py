#Herança e polimofismo
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        

    def emitir_som(self):
        pass


class Cachorro(Animal):
    def emitir_som(self):
        return "Au, Au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miauu!"


gato = Gato("Gato")
print(gato.emitir_som())


cachorro = Cachorro("Cachorro")
print(cachorro.emitir_som())

animais = [gato, cachorro]
for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")




