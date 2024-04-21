# Dados Entrada
valor = int(input("Digite o valor: "))

# Processamento
## Começar com a MAIOR nota (100)
notas_100 = valor // 100

## Atualizar o valor
valor = valor % 100

## Notas de 50
notas_50 = valor // 50

## Atualizar o valor
valor = valor % 50

## Notas de 20
notas_20 = valor // 20

## Atualizar o valor
valor = valor % 20

## Notas de 10
notas_10 = valor // 10

## Atualizar o valor
valor = valor % 10

## Notas de 5
notas_5 = valor // 5

## Atualizar o valor
valor = valor % 5

## Notas de 2
notas_2 = valor // 2

## Atualizar o valor
valor = valor % 2

## Notas de 1
notas_1 = valor // 1

## Atualizar o valor
valor = valor % 1

# Dados de Saída
print(f"{notas_100} notas de 100")
print(f"{notas_50} notas de 50")
print(f"{notas_20} notas de 20")
print(f"{notas_10} notas de 10")
print(f"{notas_5} notas de 5")
print(f"{notas_2} notas de 2")
print(f"{notas_1} notas de 1")