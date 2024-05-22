#Implemente um código que leia uma string do usuário e imprima quantas 
#vogais existem na frase e quais os seus índices da string. 
#Dica: letra in "aeiou". 
#Exemplo:
#Frase: Meu amor mora em Roma e me deu um ramo de flores

#Dados de Entrada
frase = ("Meu amor mora em Roma e me deu um ramo de flores")
vogais = 0
indice = []

#Processamento
for i in range(len(frase)):
    if frase [i] in "aeiouAEIOU":
        vogais +=1
        indice.append(i)

# Dados de Saída
print(vogais)
print(indice)