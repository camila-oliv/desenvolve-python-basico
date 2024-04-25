# Dados Entrada
experimento = int(input('Digite quantidade de experimentos: '))

# Inicializar Variaveis
soma_sapo, soma_rato, soma_coelho = 0, 0 , 0
cont = 0

# Processamento
while cont < experimento:
    quantidade = int(input("Digite quantidade de animais: "))
    tipo = input("Sapo (S), Rato (R), Coelho (C): ")

    if tipo =='S':
        soma_sapo += quantidade
    elif tipo == 'R':
        soma_rato += quantidade
    elif tipo == 'C':
        soma_coelho += quantidade

# Atualizando Variavel de Controle do Laço
    cont += 1

# Dados de Saída

print('Total de Cobais:', soma_coelho+soma_rato+soma_sapo)
print('Total de Sapo:', soma_sapo)
print('Total de Coelho:', soma_coelho)
print('Total de Rato:', soma_rato)
