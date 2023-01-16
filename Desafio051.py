# Desafio 051 - Progressão aritmetica (Informe o primeiro termo, a razao e mostre os 10 termos da PA)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='=> ')
print('Fim!')