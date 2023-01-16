# Desafio 045 - Jogo de Jokenpo #

# importando randit de random #
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)              #
print('*' * 30)
print('Vamos jogar Jokenpo?! Vamos!')
print('''Escolha uma opção:
[ 0 ] - Pedra
[ 1 ] - Papel 
[ 2 ] - Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('*' * 30)
print('O Computador escolheu {}'.format(itens[computador]))
print('O Player 1 escolheu {}'.format(itens[jogador]))
if computador == 0:                     # COMPUTADOR JOGOU PEDRA
    if jogador == 0:                    # PEDRA
        print('Empatou!')
    elif jogador == 1:                  # PAPEL
        print('Jogador venceu!')
    elif jogador == 2:                  # TESOURA
        print('Vc Perdeu!')

elif computador == 1:                   # COMPUTADOR JOGOU PAPEL
    if jogador == 0:                    # PEDRA
        print('Computador venceu!')
    elif jogador == 1:                  # PAPEL
        print('Empatou!')
    elif jogador == 2:                  # TESOURA
        print('Jogador Venceu!')
elif computador == 2:                   # COMPUTADOR JOGOU TESOURA
    if jogador == 0:                    # PEDRA
        print('Jogador Venceu!')
    elif jogador == 1:                  # PAPEL
        print('Computador Venceu!')
    elif jogador == 2:                  # TESOURA
        print('Empatou!')
else:
    print('Jogada Invalida!')
