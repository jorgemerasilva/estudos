#Decoradores comuns
class MinhaClasse:
    valor = 10 #Atributoo da classe

    def __init__(self, nome):
        self.nome = nome #Atributo da instancia

    #Precisa criar uma instancia da classe pra chamar metodo
    def metodo_instancia(self):
        return "Método de instancia"

    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamando para valor={cls.valor}"

    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"

#instancia
obj = MinhaClasse("Jorge")
print(obj.metodo_instancia())


#Para cessar atributo da classe não precisa de instancia
print(f"{MinhaClasse.valor}")

#Chamando Método dsa classe
print(MinhaClasse.metodo_classe())