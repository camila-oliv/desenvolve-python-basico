# Dados Entrada
n1, n2 = int(input("Digite um número: ")) , int(input("Digite outro número: "))

# Processamento
if ((n1+n2) % 2) == 0:
    print('É par')
else:
    print('É impar')

#print('É par'if (n1+n2) % 2 == 0 else 'É impar' )