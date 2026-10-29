
#Decoradores usando função
def meu_decorador(func):
    def wrapper():
        print("Antes")
        func()
        print("depois")
    return wrapper


@meu_decorador
def minha_funcao():
    print("Agora")


minha_funcao()


#Decoradores usando classes

class MeuDecoradorDeClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Antes")
        self.func()
        print("Depois")


@MeuDecoradorDeClasse
def agora():
    print("Agora")

agora()