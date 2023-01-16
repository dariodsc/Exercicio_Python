# Desafio 047 - Números pares no intervalo de 0 até 50

for n in range(2, 51, 2):
    # Começando de 2 / terminando em 50 ignorando a ultima posição / Intervalo de 2 em 2 #
    # Botar 1 a mais no valor pois o Python ignora a ultima casa numeral #

    if n % 2 == 0:
        # Se n dividido por 2 com resto 0 #

        print(n, end=' ')
        # Print os pares #

print('\n\nTodos os números pares no intervalo de 0 a 50')