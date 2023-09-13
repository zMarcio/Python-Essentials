import sys
import os
from datetime import datetime

while True:
    arguments = sys.argv[1:]

    if not arguments:
        operation = input('Operação: ')
        n1 = input("n1: ")
        n2 = input("n2: ")
        arguments = [operation,n1,n2]
    elif len(arguments) != 3:
        print('Número de arguementos inválidos')
        print("ex: 'sum 5 5'")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ('sum','sub','mul','div')
    if operation not in valid_operations:
        print('Operação inválida')
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        if not num.replace(".","").isdigit():
            print(f"Numero inválido {num}")
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    n1, n2 = validated_nums

    if operation == "sum":
        resulta = n1 + n2

    if operation == "sub":
        resulta = n1 - n2
        
    if operation == "mul":
        resulta = n1 * n2
        
    if operation == "div":
        resulta = n1 / n2


    path = os.curdir
    filepath = os.path.join(path,"infixcalc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv("USER","anonymous")

    with open(filepath,"a") as arquivo:
        arquivo.write(f"{user}, {timestamp}, {operation}, {n1}, {n2} = {resulta} \n")
        arquivo.close()
    print(resulta)

    if input(f"Pressione enter para continuar ou qualquer tecla para sair"):
        break