print('Calculo IMC')

def calculo_imc():
    while True:
        try:
            altura = float(input('Informe sua altura: '))
            break
        except ValueError:
            print('Valor inválido. Digite um valor válido.')
            
    while True:
        try:
            peso = float(input('Informe sua peso: '))
            break
        except ValueError:
            print('Valor inválido. Digite um valor válido.')

    imc = peso / altura**2

    if imc < 18.5:
        print('Seu IMC é: {:.2f}, está na faixa de MAGREZA'.format(imc))
    elif imc >= 18.5 and imc <= 24.9:
        print('Seu IMC é: {:.2f}, está dentro da faixa NORMAL'.format(imc))
    elif imc >= 25 and imc <= 29.9:
        print('Seu IMC é: {:.2f}, está na faixa do SOBREPESO'.format(imc))
    elif imc >= 30 and imc <= 39.9:
        print('Seu IMC é: {:.2f}, está na faixa do OBESIDADE'.format(imc))
    else:
        print('Seu IMC é: {:.2f}, está na faixa do OBESIDADE GRAVE'.format(imc))

calculo_imc()
