print(11*"\033[96m-")
print("Triângulos!")
print(11*"-")
l1 = int(input("\033[mInforme o primeiro lado do triângulo: "))
l2 = int(input("Informe o segundo lado do triângulo: "))
l3 = int(input("Informe do terceiro lado do triângulo: "))
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print("Com esses lados é possível ter um triângulo.")
    if l1 == l2 == l3:
        print("O triângulo formado é um equilátero.")
    elif (l1 != l2) and (l1 != l3) and (l2 != l3):
        print("O triângulo formado é um escaleno.")
else:
    print("Não é possível ter um triângulo com esses lados informados.")
