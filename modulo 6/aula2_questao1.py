#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 
#e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
#A lista ordenada, sem modificar a lista original
#A lista original
#O índice do maior valor da lista
#O índice do menor valor da lista

# Definir Lista
notas = []

for i in range(20):
    nota = int(input("Digite o valor %d:"%i))
    notas.append(nota)

print(notas)
print(max(notas))
print(min(notas))


