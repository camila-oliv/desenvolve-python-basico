#Dadas duas variáveis v1 = 10 e v2 = 20, utilize uma terceira variável 
#para trocar os valores entre as duas variáveis. Ou seja, ao final v1 
#terá o valor de v2, e v2 o valor de v1. Você deve usar uma variável 
#auxiliar de troca, não podendo atribuir os novos valores diretamente.

#Dados de Entrada
v1=10
v2=20

#Processamento
x = v1
v1 = v2
v2 = x

#Dados de Saída
print(f"Valor V1: {v1}")
print(f"Valor V2: {v2}")
