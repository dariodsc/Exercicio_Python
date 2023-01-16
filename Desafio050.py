# Desafio 050 - Números pares dentro de uma sequencia

cont = 0                    # contabiliza os valores digitados que atendem ao if #
soma = 0                    # soma os valores digitados que atendem ao if        #

for c in range(1, 7):       # range de 1 a 7 para que na execução não mostre o primeiro valor com 0 #
    num = int(input('Digite {} valor: '.format(c)))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print('Foi informado {} números pares'.format(cont))
print('Sendo que a soma dos pares é {}'.format(soma))
