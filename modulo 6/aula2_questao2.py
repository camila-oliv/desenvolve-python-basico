#Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma 
#variável chamada num_elementos. 
#Em seguida gere aleatoriamente valores entre 1 e 10
# em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. 
#Em seguida imprima:
#A lista elementos
#A soma dos valores da lista
#A média dos valores da lista

# Gerando Números de Elementos
import random
import math

n1 = 1

for i in range(n1):
    num_elementos = random.randint(5,20)
    print(num_elementos)



# Gerando Valores dos Elementos
elementos = []
for i in range(num_elementos):
    valores = random.randint(1,10)
    elementos.append(valores)


#Dados de Saída
print(elementos)
print(sum(elementos))
print(sum(elementos)/ len(elementos))