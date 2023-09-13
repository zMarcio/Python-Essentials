import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path,"notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print(f"Invalid usage")
    print(f"Invalid usage\n you must specify subcommands {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

while True:
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag?").strip().lower()

        for line in open(filepath):
            title,tag,text = line.split("\t")
            if tag.lower() == arguments[1].lower():
                print(f"title: {title}")
                print(f"text: {text}")
                print("-"*30) 
                print()

    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            title = input("Qual é o titulo? ").strip().title()
            
        text = [
            f"{title}",
            input("Tag:").strip(),
            input("text:").strip()
        ]
        with open(filepath,"a") as file_:
            file_.write("\t".join(text)+ "\n")


    continuar = input(f"Quer continuar {arguments[0]} adicionando notas? [N/Y]").strip().lower()

    if continuar != "y":
        break