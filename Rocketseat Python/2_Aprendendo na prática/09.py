import re

texto = input("Digite as notas separador por ',': ")
partes = re.split(r"[\s,-]+", texto)

total = 0
for part in partes:
    total += float(part)
media = total / len(partes)

print(f"Notas: {", ".join(partes[:-1]) + " e " + partes[-1]}\nmedia: {media}")

