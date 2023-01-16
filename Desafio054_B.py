# Desafio 054 - Grupo de Maioridade (Informando um valor a variavel contador for)

contmenor = 0
contmaior = 0

from datetime import date
ano_atual = date.today().year

c = int(input('Informe o número de amostra de pessoas: '))

for c in range(1, c + 1):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = ano_atual - nasc
    if idade > 21:
        contmaior = contmaior + 1
    else:
        contmenor = contmenor + 1
print('No total de {} de pessoas da amostra'.format(c))
print('{} são adultos e {} são menores de idade'.format(contmaior, contmenor))
