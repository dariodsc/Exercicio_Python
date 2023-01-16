# Desafio 048 - Soma dos números impares divisiveis por 3 no intervalo de 1 até 500

cont = 0
soma = 0
# variavel soma com função de acumulador

for n in range(1, 501, 2):
# Começando de 1 / terminando em 500 ignorando a ultima posição / Intervalo de 2 em 2 #
# Botar 1 a mais no valor pois o Python ignora a ultima casa numeral #
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1
        # Contabiliza os valores resultantes do IF
        print(n, end=' ')
        # end=' ' para colocar um espaço entre os valores apresentados - Ex: 0 1 2...
print('\n')
print('A soma entre {} valores solicitados é de {}'.format(cont, soma))