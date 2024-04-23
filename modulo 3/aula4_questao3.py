# Dados de Entrada
ano = int(input("Digite o ano: "))

# Processamento
#se o ano for (1) divisível por 4 e não for divisível por 100,
# ou (2) se for divisível por 400. Caso contrário, imprima "Não Bissexto".
a = int(ano//4) 
b = int(ano//400)



# Dado de Saída
if a and b:
    print('Bissexto')
else:
    print('Não Bissexto')