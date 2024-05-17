#Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50.
#Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem 
#nas duas listas. Ao final imprima:
#Ambas as listas
#A lista intersecção ordenada
#A quantidade de vezes que cada elemento aparece em cada lista
import math
import random

#Gerando Listas
lista1=[]

for i in range(20):
    valores = random.randint(0,50)
    lista1.append(valores)


lista2=[]

for i in range(20):
    valores = random.randint(0,50)
    lista2.append(valores)

# Gerando lista com valores que repetem

lista_interseccao = []


#Dados de Saída
print(lista1)
print(lista1.count())

print(lista2)
print(lista2.count(valores))
