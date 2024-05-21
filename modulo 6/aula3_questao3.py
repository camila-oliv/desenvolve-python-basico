#Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. 
#Em seguida encontre o intervalo que possui a maior quantidade de números
#negativos e delete ele da lista com o operador del. 
#Você deve imprimir a lista antes e depois da deleção.

import random
# Dados de entrada
inicio_fatia_maior, tam_fatia_maior = 0, 0
inicio_fatia_atual, tam_fatia_atual =0, 0
lista_aleatoria = []

for i in range(20):
    valores = random.randint(-10,10)
    lista_aleatoria.append(valores)


#Processamento
for i in range (len(lista_aleatoria)):
    if lista_aleatoria [i] <0:
        tam_fatia_atual += 1
        print(lista_aleatoria)
        if tam_fatia_atual ==1:
            inicio_fatia_atual = i
    else:
        if tam_fatia_atual > tam_fatia_maior:
            tam_fatia_maior = tam_fatia_atual
            inicio_fatia_maior = inicio_fatia_atual
            tam_fatia_atual = 0


#Dados de Saída
print(inicio_fatia_maior, tam_fatia_maior)
del lista_aleatoria[inicio_fatia_maior:inicio_fatia_maior + tam_fatia_maior]
print(lista_aleatoria)


        