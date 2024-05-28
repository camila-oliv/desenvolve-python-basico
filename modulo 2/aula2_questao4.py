#Uma conta poupança foi aberta com um depósito de R$500,00. 
#Esta conta é remunerada em 1% de juros ao mês. O código a seguir 
#apresenta uma forma de implementação para calcular três meses de acúmulo
#de juros. Reescreva esse código usando apenas duas variáveis. 

#Dados de Entrada
juros = 1.01
saldo = 500.0

#Processamento
print(saldo)
saldo = saldo * juros
print(saldo)
saldo = saldo * juros
print(saldo)
saldo = saldo * juros

#Dados de Saída
print("Após 3 meses meu novo saldo é", saldo)
