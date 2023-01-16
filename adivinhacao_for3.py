# Jogo de adivinhação com for, escolhendo o nivel do jogo e dando ponto ao jogador

from random import randint          # importa de random o randint que gera números aleatorios

print("#" *20)
print("Jogo da adivinhação")
print("#" *20)

numero_secreto = randint(1, 101)       # variavel receberá valor aleatório
tentativas = 0                         # variavel de tentativas guardando valor 0
pontos = 1000

print("Escolha o nível de dificuldade: \n(1) Fácil (2) Médio (3) Díficil")
nivel = int(input("Dificuldade: "))

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
    print(numero_secreto)
    numero_escolhido = int(input("Digite um número entre 1 e 100:\n "))
    print("*" *30)
    # input que receberá o valor do user
    print("Vc digitou:", numero_escolhido)

    numero_certo = numero_escolhido == numero_secreto

    if (numero_escolhido < 1 or numero_escolhido > 100):
        print("Por favor, digite um valor válido")
        print(numero_secreto)
        continue
        # continua o programa e encerra o laço if

    if numero_certo:
        print("Acertou!")
        print("Vc fez {} pontos".format(pontos))
        break
    else:
        print("Errou!")
    pontos_perdidos = abs(numero_secreto - numero_escolhido)
    pontos = pontos - pontos_perdidos