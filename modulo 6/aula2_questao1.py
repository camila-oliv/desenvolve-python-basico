#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 
#e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
#A lista ordenada, sem modificar a lista original
#A lista original
#O índice do maior valor da lista
#O índice do menor valor da lista
import random
import math

# Definir Lista
lista_aleatoria = []

for i in range(20):
    valores = random.randint(-100,100)
    lista_aleatoria.append(valores)

print(sorted(lista_aleatoria))
print(lista_aleatoria)
print("O maior valor está no índice: ", lista_aleatoria.index(max(lista_aleatoria)))
print("o menor valor está no índice: ", lista_aleatoria.index(min(lista_aleatoria)))


