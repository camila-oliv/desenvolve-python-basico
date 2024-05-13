#Escreva um programa em Python que utiliza a biblioteca datetime para exibir a 
#data e hora atuais com a formatação apresentada a seg

from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

print(data_e_hora_em_texto)