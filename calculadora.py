print("\n***** Python calculator *****\n")

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

print("\nSelecione o numero da operação desejada: \n")


print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")


opcao = input("\nDigite sua opcao(1/2/3/4): ")

n1 = int(input("\nInforme o primeiro número: "))
n2 = int(input("\nInforme o segundo número: "))

if opcao == '1':
    print("{} + {} = {}".format(n1, n2, add(n1, n2)))

elif opcao == '2':
    print("{} - {} = {}".format(n1, n2, sub(n1, n2)))

elif opcao == '3':
    print("{} - {} = {}".format(n1, n2, mult(n1, n2)))

elif opcao == '4':
    print("{} / {} = {}".format(n1, n2, div(n1, n2)))

else:
    print("\nOperação Inválida!\n")

