#1 # função de repetição do programa ou encerramento

def again():
    executar_novo = input("Quer executar novamente: [S] Sim ou [N] Não: \n")
    if executar_novo.upper() == "S":
        calculadora()   
        # nome da função principal
    elif executar_novo.upper() == "N":
        print("Até mais tarde!!!")
    else:
        again()
        
#2 # Importando biblioteca date para trabalhos com datas

from datetime import date

ano_atual = date.today().year
print(ano_atual)

#3 # Saudação de acordo com o horário do dia (bom dia, boa tarde, boa noite)

def saudacao():

    from datetime import datetime

    nome = str(input("Qual seu nome: "))
    hora_primaria = int(datetime.now().strftime("%H"))
    hora_atual = datetime.now().strftime("%H:%M")

    if hora_primaria < 12:
        print("Bom dia, {}. Hora certa: {} hs.".format(nome, hora_atual))
    elif hora_primaria >= 12 or hora_primaria < 18:
        print("Boa tarde, {}. Hora certa: {} hs.".format(nome, hora_atual))
    elif hora_primaria >= 18 or hora_primaria < 24:
        print("Boa noite, {}. Hora certa: {} hs".format(nome, hora_atual))

saudacao()

#4 # Medindo caracteres (strings)

texto = "Python é show!"

novo_texto = texto.replace(" ", "")

#print("O texto = {}, possui {} caracteres".format(texto, len(novo_texto)))

print(f'O Texto = {texto}, possui {len(novo_texto)} caracteres')

# 5 # Checando se variavel é um numeral

# Verificação do primeiro número
    while True:
        valor_1 = input("Primeiro Valor: ")
        if valor_1.isdigit():
            valor_1 = int(valor_1)
            break
        else:
            print("Valor inválido. Digite um número inteiro válido.")


