# Perguntar: "Quantas pessoas estão no grupo?"
numero_de_pessoas = int(input("Quantas pessoas estão no grupo? "))

# Perguntar: "Alguma pessoa fuma? (Sim/Não)"
fuma = input("Alguma pessoa fuma? (Sim/Não) ")

# Perguntar: "Alguma pessoa tem animais de estimação? (Sim/Não)"
animais = input("Alguma pessoa tem animais de estimação? (Sim/Não) ")

# Definir as áreas do restaurante
area_externa = "Alocar para área externa"
primeiro_andar = "Alocar para 1º andar"
terreo = "Alocar para térreo"

# Se fuma = "Sim" OU animais = "Sim" então
if fuma.lower() == "sim" or animais.lower() == "sim":
    print(area_externa)
# Senão Se número_de_pessoas >= 5 então
elif numero_de_pessoas >= 5:
    print(primeiro_andar)
# Senão
else:
    print(terreo)
    