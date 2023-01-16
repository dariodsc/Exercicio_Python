from random import randint      # importa de random o randint que gera números aleatorios
numero_secreto = randint(0,2)        # variavel receberá valor aleatório

escolhido = int(input("Digite seu número: "))   # input que receberá o valor do user
maior_numero = escolhido > numero_secreto       # variavel para guardar o maior numero escolhido
menor_numero = escolhido < numero_secreto       # variavel para guardar o menor numero escolhido

if escolhido == numero_secreto:
    print("Vc acertou!")
else:
    if(maior_numero):
        print("Seu número foi maior que o aleatório")
    elif(menor_numero):
        print("Seu número foi menor que o aleatório")

print("Número escolhido = {} | Número aleatório = {}".format(escolhido, numero_secreto))