#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule
#a raíz quadrada da soma dos valores. Peça ao usuário o valor de n.
#Biblioteca random: Função randint()
#Biblioteca math: Função sqrt()

import random
import math
# Dados de Entrada:
n = int(input("Digite a quantidade de valores: "))
soma = 0

# Processamento:
for i in range(n):
    valor = random.randint(0, 100)
    soma += valor

# Dados de Saída:
print(soma)
print(f"A raiz quadrada da soma é {math.sqrt(soma):.2f}")