#Herança multipla
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."

    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."


class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcego emitindo som"


morcego = Morcego("Morcego")
print(morcego.amamentar())
print(morcego.voar())