def adivinhacao():

    numero_secreto = 42
    total_de_tentativas = 4

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número(Entre 1 e 100): ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)
        
        if(chute < 1 or chute > 100):
            print("Por favor, Digite um número entre 1 e 100")
            continue
            # Dá continuidade, não encerra o program
                
        # validação
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
            # Quando o numero for acertado, encerra o programa
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            # Caso o chute seja maior que o numero secreto
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            # Caso o chute seja menor que o numero secreto

    print("Fim do jogo")

adivinhacao()
