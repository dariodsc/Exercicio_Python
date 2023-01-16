# Desafio 049 - Tabuada V.2 (for)

num = int(input('Informe um número para a Tabuada: '))
for c in range(1, 11):                                  # range de 1 até 10 / O ultimo é sempre ignorado pelo sistema
    print('{} X {} = {}'.format(num, c, num*c))         # O print vai ser repetido até o comando FOR se atendido
