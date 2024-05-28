#Desenvolva um programa em Python que peça ao usuário para inserir dois 
#números decimais e calcule a diferença absoluta entre esses dois números. 
#Utilize a função nativa abs para garantir que o resultado seja sempre 
#positivo e round para arredondar o resultado para duas casas decimais.

# Dados de Entrada:
n1 = float(input("Insira um numero decimal.N1: "))
n2 = float(input("Insira outro numero decimal.N2: "))
soma = 0.0

# Processamento
for i in range (n1,n2):
    valor = abs (n1 + n2)
    soma += valor

# Dados de Saída
print(valor,round)
