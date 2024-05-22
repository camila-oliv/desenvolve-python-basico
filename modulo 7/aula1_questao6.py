#Dada uma string e uma palavra objetivo, encontre todos os 
#anagramas da palavra objetivo. Anagramas são palavras com 
#os mesmos caracteres rearranjados.
#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
#Digite a palavra objetivo: amor
#Anagramas: ["amor", "mora", "ramo", "Roma"] 

#Dados de Entrada
frase = "Meu amor mora em Roma e me deu um ramo de flores"
palavra_objetivo = sorted("amor")

#Processamento
lst_palavras = frase.lower().split("")
for palavra in lst_palavras:
    if sorted(palavra) == palavra_objetivo:
        print(palavra)