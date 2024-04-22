# Dados de Entrada
classe = input("Escolha a classe (guerreiro, mago ou arqueiro):")
força =int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20)"))

# Processamento
#Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
#Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
#Arqueiro: Força e Magia devem ser ambos superiores a 5, 
#mas nenhum deles pode ser superior a 15

guerreiro = (força>=15) and (magia<=10)
mago = (força<=10) and (magia>=15)
arqueiro = (força >5) and (magia>5) and (força<15) and (magia<15)

atributos_consistentes = guerreiro or mago or arqueiro

#Dados de Saída
print("Pontos de atributo consistentes com a classe escolhida:")
print(atributos_consistentes)