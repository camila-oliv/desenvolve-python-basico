#Dados Entrada
distancia = int(input('Digite a distância em km: '))
peso_pacote = int(input('Digite o peso em kg: '))

# Processamento
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

a = (distancia <= 100) and (peso_pacote * 1)
b = (distancia >= 101) and (distancia<=300) and (peso_pacote * 1.50)
c = (distancia <= 300)and (peso_pacote * 2)

frete = a or b or c 

if peso_pacote >10:
    frete += 10


#Dados de Saída
print(f'Seu frete é {frete}')
