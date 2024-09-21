def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Essa opção não existe"

while True:
    print("Escolha a operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    
    operacao = int(input("Digite o número da operação: "))
    
    if operacao == 0:
        print("Saindo...")
        break
    elif operacao in [1, 2, 3, 4]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado: {resultado}")
    else:
        print("Essa opção não existe")