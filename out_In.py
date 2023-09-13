import os
import sys
arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]
if not (filename.endswith(".txt") and templatename.endswith(".txt")):
    print("Informe arquivos de texto válidos (.txt)")
    sys.exit(1)


path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path,templatename)

for line in open(filepath):
    nome, email = line.split(",")
    print(f"Enviando email para: {email}")
    print(
        open(templatepath).read() % {
            "nome":nome,
            "produto":"caneta",
            "texto": "escreve muito bem",
            "link": "http//canetaslegais.com",
            "quantidade": 45,
            "preco": 50,
        }
    )
    print("-"*75)