def obter_nome():
    return input("Digite seu nome completo: ")

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

def calcular_idade(ano_nascimento, ano_atual=2022):
    return ano_atual - ano_nascimento

def main():
    nome = obter_nome()
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    print(f"{nome}, você completou ou completará {idade} anos em 2022.")

if __name__ == "__main__":
    main()