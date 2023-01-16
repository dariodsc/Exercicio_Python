# Desafio 054 - Grupo de Maioridade

contmenor = 0       # contador de pessoas de menor idade
contmaior = 0       # contador de pessoas de maior idade

from datetime import date       # importando datetime de date para definir o ano atual
ano_atual = date.today().year

for c in range(1, 8):           # contador de 1 a 7, ignorando o ultimo
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = ano_atual - nasc
    if idade >= 21:              # Definida a maior idade igual ou superior a 21 anos
         contmaior = contmaior + 1
    else:
         contmenor = contmenor + 1
print('O total de adultos é {} e menores de idade é {}'.format(contmaior, contmenor))
