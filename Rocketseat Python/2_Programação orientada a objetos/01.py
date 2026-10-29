class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

pessoa1 = Pessoa("Jorge", 30)
print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")
mensagem = pessoa1.saudacao()



pessoa2 = Pessoa("Kaylanne", 32)
print(f"Nome: {pessoa2.nome}")
print(f"Idade: {pessoa2.idade}")
mensagem = pessoa2.saudacao()

