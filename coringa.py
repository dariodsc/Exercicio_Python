#1 # função de repetição do programa ou encerramento

# Primeira Versão

def again():
    import os   # import para a usar o cls / Limpar a tela
    calcular_denovo = input("Quer calcular novamente: [S] Sim ou [N] Não: \n")
    if calcular_denovo.upper().strip()[0] == "S":
        os.system('cls')    # Usado no import
        calculadora()   # mudar para sua função principal
    elif calcular_denovo.upper().strip()[0] == "N":
        print("Encerrando...")
    else:
        print('Valor invalido!')
        again()
    # fim da função again
        
# Segunda Versão - simplificada do chatgpt 

 def again(): 
    executar_novo = input("Quer jogar novamente? [S] Sim ou [N] Não: \n")
    if executar_novo.upper().strip() in ['S', 'SIM']:
        jokenpo()   # mudar para sua função principal
    elif executar_novo.upper().strip() in ['N', 'NÃO']:
        print("Até mais tarde!!!")
    else:
        again()
        
#2 # Importando biblioteca date para trabalhos com datas

from datetime import date

ano_atual = date.today().year
print(ano_atual)

#3 # Saudação de acordo com o horário do dia (bom dia, boa tarde, boa noite)

# Primeira Versão - Saudação com nome

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

# Segunda Versão - Somente Saudação

def saudacao():

    from datetime import datetime
   
    hora_primaria = int(datetime.now().strftime("%H"))

    if hora_primaria < 12:
        print('Bom dia')
    elif hora_primaria >= 12 or hora_primaria < 18:
        print('Boa tarde')
    elif hora_primaria >= 18 or hora_primaria < 24:
        print('Boa noite')

saudacao()

#4 # Medindo caracteres (strings)

texto = "Python é show!"

novo_texto = texto.replace(" ", "")

#print("O texto = {}, possui {} caracteres".format(texto, len(novo_texto)))

print(f'O Texto = {texto}, possui {len(novo_texto)} caracteres')

# 5 # Checando se variavel é um numeral

# Verificação a variavel é um INT
    while True:
        valor_1 = input("Primeiro Valor: ")
        if valor_1.isdigit():
            valor_1 = int(valor_1)
            break
        else:
            print("Valor inválido. Digite um número inteiro válido.")


