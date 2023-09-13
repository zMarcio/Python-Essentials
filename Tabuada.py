variavelIn = int(input('digite qual tabuada você quer '))
x = int(input('digite o limite (se você quer de até 10 ou até o numero que você digitou acima):'))

for variavelIn in range(variavelIn,x+1):
    if x != variavelIn:
        variavelIn+1
    i = 1
    print("----------------------------------------")
    for i in range(i,11):
        print(f"{variavelIn} X {i} = {variavelIn*i}")
        i += 1


numeros = list(range(1,11))

for numero in numeros:
    print("tabuado do: ", numero)
    i = 0
    for outro_numero in numeros:
        print(numero * outro_numero)


