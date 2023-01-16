from random import randint          # importa de random o randint que gera números aleatorios
from random import randrange

numero_secreto = randint(1, 3)       # variavel receberá valor aleatório
tentativas = 5                      # variavel de tentativas

for rodada in range(1, tentativas + 1):
    print("*" *30)
    print("Tentativa {} de {}".format(rodada, tentativas))
    print("*" *30)
    numero_escolhido = int(input("Digite um número entre 1 e 100:\n "))
    print("*" *30)
    # input que receberá o valor do user
    print("Vc digitou:",numero_escolhido)

    numero_certo = numero_escolhido == numero_secreto

    if (numero_escolhido < 1 or numero_escolhido > 100):
        print("Por favor, digite um valor válido")
        print(numero_escolhido)
        continue
        # continua o programa e encerra o laço if

    if numero_certo:
        print("Acertou!")
        break
    else:
        print("Errou!")
