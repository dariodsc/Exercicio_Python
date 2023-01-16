# Desafio 055 - Maior e menor peso da sequencia

maiorpeso = 0       # variavel que irá guardar o maior peso
menorpeso = 0       # variavel que irá guardar o menor peso

for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:              # ler o pessoa da 1 pessoa e guardar as variaves de maior e menor peso
        maiorpeso = peso
        menorpeso = peso
    else:                   # else - o peso das outras pessoas vai ser guardado nas variaveis caso ocorra variação
        if peso > maiorpeso:
            maiorpeso = peso    # Vai guardar o maior peso
        if peso < menorpeso:
            menorpeso = peso    # Vai guardar o menor peso
print('O maior peso lido foi de {} kg'.format(maiorpeso))
print('O menor peso lido foi de {} kg'.format(menorpeso))
