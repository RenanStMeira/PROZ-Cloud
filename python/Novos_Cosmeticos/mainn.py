# Declarar o array com os produtos
lista_produtos = [
    'máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções',
    'xampus', 'sabonetes', 'delineadores'
]

# Atualizar o array de produtos
lista_produtos[1] = 'rímel'
lista_produtos[4] = 'cremes hidratantes'
lista_produtos.remove('delineadores')

# Adicionar dois novos produtos
lista_produtos.append('protetor solar')
lista_produtos.append('tônico facial')

# Imprimir a nova lista no terminal
print("Nova lista de produtos:")
for produto in lista_produtos:
    print(f"Temos {produto} à venda!")