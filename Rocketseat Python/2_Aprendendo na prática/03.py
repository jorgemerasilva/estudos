"""
Exercício 03 - Variáveis do tipo string

"""

# Solicitando ao usuário que digite seu nome completo
nome_completo = "Jorge Mera da Silva"
print("Olá, " + nome_completo + "! Seja bem-vindo(a)!")

# Solicitando ao usuário que digite seu primeiro nome e sobrenome separadamente
nome = "Jorge"
sobrenome = "Mera"
print(f"Olá, {nome} {sobrenome}! Seja bem-vindo(a)!")

# Demonstrando diferentes formas de declarar strings em Python
nome_simples = "Jorge Mera"
nome_aspas = """Jorge Mera"""
nome_quebra_linha = "Jorge \
    Mera"


#formatação de strings
print(f"Nome simples: {nome_simples}")
print("Meu nome completo é " + "Jorge" + " " + "Mera")
print("Meu nome completo é " + "Jorge", "Mera")
print("Nome com aspas triplas: {}".format(nome_aspas))
print("Meu nome completo é %s %s" % (nome, sobrenome))
print("Meu nome completo é {} {}".format(nome, sobrenome))


#Metodos de strings

#Maiúsculas
nome_completo_upper = nome_completo.upper()
print(f"Meu nome completo em maiúsculas: {nome_completo_upper}")

#Minúsculas
nome_completo_lower = nome_completo.lower()
print(f"Meu nome completo em minúsculas: {nome_completo_lower}")

#Capitalizar a primeira letra de cada palavra
nome_completo_capitalizado = nome_completo.title()
print(f"Meu nome completo capitalizado: {nome_completo_capitalizado}")

#Capitalizar a primeira letra da string
nome_completo_capitalize = nome_completo.capitalize()
print(f"Meu nome completo com a primeira letra em maiúscula: {nome_completo_capitalize}")

#Inverter maiúsculas e minúsculas
nome_completo_swapcase = nome_completo.swapcase()
print(f"Meu nome completo com as letras em posições opostas: {nome_completo_swapcase}")

#Tirar espaços em branco no início e no final da string
nome_completo_strip = nome_completo.strip()
print(f"Meu nome completo sem espaços em branco no início e no final: {nome_completo_strip}")

#Tirar espaços em branco no início da string
nome_completo_lstrip = nome_completo.lstrip()
print(f"Meu nome completo sem espaços em branco no início: {nome_completo_lstrip}")

#Tirar espaços em branco no final da string
nome_completo_rstrip = nome_completo.rstrip()
print(f"Meu nome completo sem espaços em branco no final: {nome_completo_rstrip}")

# remove caracteres específicos
nome_completo_remover = nome_completo.strip(' ')
print(f"Meu nome completo sem caracteres específicos: {nome_completo_remover}")

# por espaços
nome_completo_split = nome_completo.split(' ')
print(f"Meu nome completo dividido por espaços: {nome_completo_split}")

#Dividir o nome completo no primeiro espaço
nome_completo_split_1 = nome_completo.split(' ', 1)
print(f"Meu nome completo dividido no primeiro espaço: {nome_completo_split_1}")

#Contar o número de caracteres
numero_caracteres = len(nome_completo)
print(f"O número de caracteres no meu nome completo é: {numero_caracteres}")

#Primeira letra do nome completo
primeira_letra = nome_completo[0]
print(f"A primeira letra do meu nome completo é: {primeira_letra}")

#Ultima letra do nome completo
ultima_letra = nome_completo[-1]
print(f"A última letra do meu nome completo é: {ultima_letra}")

#inverter o nome completo
nome_completo_invertido = nome_completo[::-1]
print(f"Meu nome completo invertido é: {nome_completo_invertido}")

#De 2 em 2 caracteres
nome_completo_2em2 = nome_completo[::2]
print(f"Meu nome completo de 2 em 2 caracteres é: {nome_completo_2em2}")

#Fatiando o nome completo para obter o primeiro nome
primeiro_nome = nome_completo[0:5]
print(f"Meu primeiro nome é: {primeiro_nome}")

#Fatiando o nome completo para obter o sobrenome
sobrenome_fatiado = nome_completo[6:10]
print(f"Meu sobrenome é: {sobrenome_fatiado}")

#Divide uma string pelas quebras de linha
frase = "Olá, meu nome é Jorge Mera da Silva.\nEu sou um estudante de Python."
frase_splitlines = frase.splitlines()
print(f"A frase dividida em linhas é: {frase_splitlines}")

#usando o join para unir uma lista de strings em uma única string
lista_nomes = ["Jorge", "Mera", "da", "Silva"]
nome_completo_join = " ".join(lista_nomes)
print(f"Meu nome completo unido é: {nome_completo_join}")

#Verificando se a frase contém o nome completo
tem_nome_completo = frase.find("Jorge Mera da Silva")
if tem_nome_completo != -1:
    print("A frase contém o nome completo.")
else:
    print("A frase não contém o nome completo.")

#Verificando se a frase contém o nome completo usando o método index
index_nome_completo = frase.index("Jorge Mera da Silva")
print(f"O índice do nome completo na frase é: {index_nome_completo}")

#Quantos o tem na frase
quantidade_o = frase.count("o")
print(f"A quantidade de 'o' na frase é: {quantidade_o}")

#Verificando se a frase começa com "Olá"
comeca_com_ola = frase.startswith("Olá")
if comeca_com_ola:
    print("A frase começa com 'Olá'.")
else:
    print("A frase não começa com 'Olá'.")

#Verificando se a frase termina com "Python."
termina_com_python = frase.endswith("Python.")
if termina_com_python:
    print("A frase termina com 'Python.'.")
else:
    print("A frase não termina com 'Python.'.")

#Verificando se a frase contém apenas letras
apenas_letras = frase.isalpha()
if apenas_letras:
    print("A frase contém apenas letras.")
else:
    print("A frase não contém apenas letras.")

#Verificando se a frase contém apenas números
apenas_numeros = frase.isdigit()
if apenas_numeros:
    print("A frase contém apenas números.")
else:
    print("A frase não contém apenas números.")

#Verificando se a frase contém apenas letras e números
apenas_letras_numeros = frase.isalnum()
if apenas_letras_numeros:
    print("A frase contém apenas letras e números.")
else:
    print("A frase não contém apenas letras e números.")

#Verificando se a frase contém apenas espaços em branco
apenas_espacos = frase.isspace()
if apenas_espacos:
    print("A frase contém apenas espaços em branco.")
else:
    print("A frase não contém apenas espaços em branco.")

#Verificando se a frase contém apenas letras maiúsculas
apenas_maiusculas = frase.isupper()
if apenas_maiusculas:
    print("A frase contém apenas letras maiúsculas.")
else:
    print("A frase não contém apenas letras maiúsculas.")


#Verificando se a frase contém apenas letras minúsculas
apenas_minusculas = frase.islower()
if apenas_minusculas:
    print("A frase contém apenas letras minúsculas.")
else:
    print("A frase não contém apenas letras minúsculas.")

#Removendo o prefixo "Olá, " da frase
frase_sem_prefixo = frase.removeprefix("Olá, ")
print(f"A frase sem o prefixo 'Olá, ' é: {frase_sem_prefixo}")

#Removendo o sufixo "Python." da frase
frase_sem_sufixo = frase.removesuffix("Python.")
print(f"A frase sem o sufixo 'Python.' é: {frase_sem_sufixo}")

#Contem a palavra "estudante" na frase
contém_estudante = "estudante" in frase
if contém_estudante:
    print("A frase contém a palavra 'estudante'.")
else:
    print("A frase não contém a palavra 'estudante'.")

#Centralizando o texto "Menu" em uma largura de 20 caracteres, preenchendo com "-"
texto = "Menu"
texto_formatado = texto.center(20, "#")
print(f"Texto centralizado com preenchimento: {texto_formatado}")

#Alinhando o texto "Menu" à esquerda em uma largura de 20 caracteres, preenchendo com "-"
texto_alinhado_esquerda = texto.ljust(20, "-")
print(f"Texto alinhado à esquerda com preenchimento: {texto_alinhado_esquerda}")

#Alinhando o texto "Menu" à direita em uma largura de 20 caracteres, preenchendo com "-"
texto_alinhado_direita = texto.rjust(20, "-")
print(f"Texto alinhado à direita com preenchimento: {texto_alinhado_direita}")

#zfill para preencher com zeros à esquerda
texto_zfill = texto.zfill(20)
print(f"Texto preenchido com zeros à esquerda: {texto_zfill}")


#f-strings (formatação)
funcinario, salario = "Jorge", 1234.5678

# 1234.57
print(f"Funcionário: {funcinario}, Salário: R$ {salario:.2f}")

# 1,234.57
print(f"Funcionário: {funcinario}, Salário: R$ {salario:,.2f}")

#Alinhando o salário à direita, à esquerda e centralizado em uma largura de 12 caracteres
print(f"Funcionário: {funcinario}, Salário: R$ {salario:>12.2f}")

#Alinhando o salário à esquerda, à direita e centralizado em uma largura de 12 caracteres
print(f"Funcionário: {funcinario}, Salário: R$ {salario:<12.2f}")

#Centralizando o salário em uma largura de 12 caracteres
print(f"Funcionário: {funcinario}, Salário: R$ {salario:^12.2f}")

#Formatando numero para ter 5 dígitos, preenchendo com zeros à esquerda
print(f"{42:05d}")  # Saída: 00042

#Transformando o número 0.263 em porcentagem com uma casa decimal
print(f"{0.263:.1%}") # Saída: 26.3%

#Formatando o número 1234567890 com vírgulas como separadores de milhar, sublinhados como separadores de milhar, binário, octal, hexadecimal (minúsculo e maiúsculo), notação científica (minúscula e maiúscula)
print(f"{1234567890:,}")  # Saída: 1,234,567,890

#Formatando o numero com _ como separadores de milhar
print(f"{1234567890:_}")  # Saída: 1_234_567_890

#Formatando o numero em binário
print(f"{1234567890:b}")  # Saída: 1001001100101100000001011010010

#Formatando o numero em octal
print(f"{1234567890:o}")  # Saída: 11145401322

#Formatando o numero em hexadecimal (minúsculo e maiúsculo)
print(f"{1234567890:x}")  # Saída: 499602d2

#Formatando o numero em hexadecimal (maiúsculo)
print(f"{1234567890:X}")  # Saída: 499602D2

#Formatando o numero em notação científica (minúscula e maiúscula)
print(f"{1234567890:e}")  # Saída: 1.234568e+09

#Formatando o numero em notação científica (maiúscula)
print(f"{1234567890:E}")  # Saída: 1.234568E+09

