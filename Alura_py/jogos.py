import forca
import adivinhacao

# importou arquivos py na mesma pasta
# Sendo esse o arquivo principal que rodará os outros

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? \n"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
        # chama a função do outro arquivo py
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
        # chama a função do outro arquivo py

if(__name__ == "__main__"):
    escolhe_jogo()
    # Definido a função principal do programa
