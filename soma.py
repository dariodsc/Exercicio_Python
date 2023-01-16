n1 = int(input("Informe o primeiro número:\n"))
n2 = int(input("Informe o primeiro número:\n"))
soma = n1 + n2
resto = soma / 2

if resto == 0:
    print("O valor:\n{} é par".format(soma))
else:
    print("O valor:\n{} é impar".format(soma))