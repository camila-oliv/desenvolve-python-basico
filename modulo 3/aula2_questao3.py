#Dados Entrada
idade_participante = int(input("Qual sua idade?: "))
jogou_3tab = (input('Você jogou pelo menos 3 jogos de tabuleiro? True ou False?' ))
vitorias = int(input("Quantas vezes você venceu um jogo?: "))

#Processamento
#tiver entre 16 e 18 anos
#já tiver jogado pelo menos 3 jogos
#já ter vencido pelo menos 1 jogo, 
a = (idade_participante >16) and (idade_participante <= 18)
b = (jogou_3tab == 'true')
c = vitorias >= 1

foi_aceito = a or b or c

# Dados de Saída
print('O participante foi permitido ingressar ao clube? ')
print(foi_aceito)
