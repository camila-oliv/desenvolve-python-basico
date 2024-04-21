# Dados Entrada
produto_1 = (input("Digite o nome do produto 1: "))
valor_unitario1 = float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))

produto_2 = (input("Digite o nome do produto 2: "))
valor_unitario2 = float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))

produto_3 = (input("Digite o nome do produto 3: "))
valor_unitario3 = float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))

# Processamento
valor1 = valor_unitario1 * quantidade1
valor2 = valor1 + (valor_unitario2*quantidade2)
valor3 = valor2 + (valor_unitario3 * quantidade3)

# Dados Saída
print(f"Total: R$ {valor3:,.2f}")