# Dados Entrada
genero =input("Informe seu genero: Masculino m ou Feminino f: ")
idade = int(input('informe sua idade: '))
tempo_serviço = int(input("Informe o tempo de serviço (em anos): "))

# Processamento
a = (genero == 'f' and idade>=60) or (genero == 'm'and idade>=65)
b = tempo_serviço > 30
c = idade >=60 and tempo_serviço >=25

pode_aposentar = a or b or c

# Dados de Saída
print("Você pode aposentar? ")
print(pode_aposentar)