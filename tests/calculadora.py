def calcular(a, b, op):
    match op:
        case "1":
            return a + b
        case "2":
            return a - b
        case "3":
            return a * b
        case "4":
            if b == 0:
                return "Divisão por zero não é permitida."
            else:
                return a / b
        case _:
            return "Operação inválida."

def entrada_usuario():
    while True:
        try:
            a = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    while True:
        try:
            b = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    while True:
        op = input("""Digite o código da operação desejada:
               Soma:          Digite 1
               Subtração:     Digite 2
               Multiplicação: Digite 3
               Divisão:       Digite 4
""")
        if op in ["1", "2", "3", "4"]:
            break
        else:
            print("Código da operação incorreto. Digite novamente.")
    
    return a, b, op

def main():
    print("Calculadora Simples em Python")
    
    num1, num2, operacao = entrada_usuario()
    
    resultado = calcular(num1, num2, operacao)
    
    print("\n")
    print(f"O resultado é: " + str(resultado))
    print("")

main()