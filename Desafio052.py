# Desafio 052 - Se um número primo ou não

total = 0                           # Contabiliza os números primos dentro do intervalo definido

num = int(input('Informe um número: '))
for c in range(1, num + 1):         # num + 1 porque o programa ignora o ultimo caractere
    if num % c == 0:
        print('\033[33m', end=' ')  # Se o if for atendido, é impresso em amarelo na tela
        total = total + 1
    else:
        print('\033[31m', end=' ')  # Se o else for atendido, é impresso em vermelho na tela
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('Ele é PRIMO!')
else:
    print('Não É PRIMO!')
