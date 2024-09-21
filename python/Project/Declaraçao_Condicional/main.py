# Declarando variaveis
nome, idade = "Renan", 32
print("O " + nome + " tem " + str(idade) + " anos")

# Condicional
nome = input("Digite seu nome: ")

if nome == "Renan":
    print("Você é o Renan")
    idade = input("Digite sua idade: ")
    if idade == str(32):
        print("o nome e a idade bateram")
    else:
        print("O nome foi verdadeiro, mas a idade não bateu")        
                