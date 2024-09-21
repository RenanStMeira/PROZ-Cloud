rodas = int(input("Informe a quantidade de rodas do veículo:"))
peso_bruto = int(input("Informe o peso bruto do veículo em quilogramas:"))
pessoas = int(input("Informe a quantidade de pessoas no veículo:"))

# Condições para determinar a categoria de habilitação
if rodas == 2 or rodas == 3:
    print("Categoria de habilitação: A")
elif rodas == 4 and pessoas <= 8 and peso_bruto <= 3500:
    print("Categoria de habilitação: B")
elif rodas >= 4 and peso_bruto > 3500 and peso_bruto <= 6000:
    print("Categoria de habilitação: C")
elif rodas >= 4 and pessoas > 8:
    print("Categoria de habilitação: D")
elif rodas >= 4 and peso_bruto > 6000:
    print("Categoria de habilitação: E")