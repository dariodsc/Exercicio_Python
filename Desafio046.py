# Desafio 046 - Fogos de artificio (Contagem regressiva)

from time import sleep                 # importa sleep de time para dar pausas de 1 segundo

print('Vamos estourar os fogos!!!')
sleep(1)                               # sleep aplicado de 1 segundo
for cont in range(10, -1, -1):         # cont (contador) = contagem regresiva de 10 a 0
    print(cont)
    sleep(1)
print('Kabum! Pow! Pow!')
sleep(3)
