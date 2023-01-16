# Desafio 047 - Números pares no intervalo de 1 até o valor definido pelo usuário na variavel C

c = int(input('Informe até que número deve ser analisado os pares: '))

for n in range(2, c + 1, 2):
    # comecando no primeiro par / Até o intervalo definido pelo usuário + 2 para contar o valor definido
    # intervalado de 2 em 2

    if n % 2 == 0:
        # Se variavel n dividido por 2 com resto 0
        print(n, end=' ')
        # Print os pares #

print('\n\nTodos os números pares no intervalo de 0 a {}'.format(c))


