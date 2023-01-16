# Desafio 050 B - Contabiliza todos os números / Soma dos Pares / Soma dos Impares

contpar, contimpar, somapar, somaimpar = 0, 0, 0, 0         # contador de par
#contimpar = 0       # contador de impar
#somapar = 0         # soma de par
#somaimpar = 0       # soma de impar

for c in range(1, 7):
    num = int(input('Digite {} valor : '.format(c)))
    if num % 2 == 0:
        contpar = contpar + 1
        somapar = somapar + num
    else:
        contimpar = contimpar + 1
        somaimpar = somaimpar + num
print('''
\nForam digitados {} números
Temos de pares {} que somados ficam = {}.
Temos de impares {} que somados ficam = {}'''.format(c, contpar, somapar, contimpar, somaimpar))
