# Dados Entrada
numero_respondentes = int(input('Digite quantidade de respondentes: '))

# Inicializar Variaveis
soma = 0
cont = 0

# Processamento
while cont < numero_respondentes:
    idade = int(input("Digite idade: "))
    soma += idade

# Atualizando Variavel de Controle do Laço
    cont += 1

# Dados de Saída

print(f"A média das idades é {soma/numero_respondentes:.0f} anos")


