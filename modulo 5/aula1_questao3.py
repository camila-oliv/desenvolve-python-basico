#Escreva um programa em Python que utiliza a biblioteca random para gerar um número
#aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. 
#Forneça feedback se o palpite é muito alto, muito baixo ou correto. 
#Interrompa a execução somente quando o usuário acertar o palpite.

import random

#Dados de Entradas:
n = int(input("Adivinhe o número escolhido (0 a 10): "))

# Processamento
for i in range(n):
    valor = random.randint(0, 10)
    if n > valor:
        print("Muito alto! Tente Novamente...")
    elif n < valor:
        print("Muito Baixo! Tente Novamente...")
    elif n == valor:
        print(f"Parabéns!! O número é {valor}!! ")
    
    if n == valor:
        break
    



