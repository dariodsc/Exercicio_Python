# Jogo de adivinhação com for e escolhendo o nivel do jogo

from random import randint          # importa de random o randint que gera números aleatorios

print("#" *20)
print("Jogo da adivinhação")
print("#" *20)

numero_secreto = randint(1, 101)       # variavel receberá valor aleatório
tentativas = 0                         # variavel de tentativas guardando valor 0

print("Escolha o nível de dificuldade: ")
print("(1) Fácil (2) Médio (3) Díficil")
nivel = int(input("Nível: "))

if nivel == 1:
    tentativas = 20
elif nivel == 2:
    tentativas = 10
else:
    tentativas = 5

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
