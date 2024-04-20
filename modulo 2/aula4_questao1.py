# Dados Entrada
comprimento = int(input("Digite o comprimento:"))
largura = int(input("Digite a largura:"))
preco_m2 = float(input("Valor do m2:"))

area_terreno = comprimento * largura #m2
preco_total = area_terreno * preco_m2

# Dados Saída
print(f"O terreno possui {area_terreno}m2 e custa R${preco_total:,.2f}")
