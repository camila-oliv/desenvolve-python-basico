#Escreva um script em Python que solicita do usuário uma 
#quantidade indefinida de números inteiros (pelo menos 4 valores), 
#os armazena em uma lista e, usando fatiamento de listas, imprima:
#A lista original
#Os 3 primeiros elementos
#Os 2 últimos elementos
#A lista invertida (do fim para o começo)
#Os elementos de índice par (0, 2, 4 … )
#Os elementos de índice ímpar (1, 3, 5, … )

#Dados de Entrada
lista = []

for i in range(6):
    valores =int(input("Digite 6 valores inteiros %d: "%i))
    lista.append(valores)


#Dados de Saída
print(lista)
print(lista[4:6])
print(lista[: : -1])
