valorEntradaMoeda = 0.00

def menu_moeda():
    global escolha_menu
    escolha_menu = int(input('Selecione uma moeda digitando seu número:' 
                '\n1 - Real'
                '\n2 - Dólar'
                '\n3 - Euro\n'))
    while escolha_menu > 3 or escolha_menu < 1:
        print('Moeda inválida!')
        menu_moeda()
    else:
        valor_inicial()

def valor_inicial():
    if escolha_menu == 1:
        valor_entrada = float(input('Informe o aporte inicial: R$ '))
        data_dia_entrada = int(input('Informe o dia do aporte: '))
        while data_dia_entrada < 1 or data_dia_entrada > 31:
            data_dia_entrada = int(input('Informe o dia do aporte novamente: '))
        data_mes_entrada = int(input('Informe o mês do aporte: '))
        while data_mes_entrada < 1 or data_mes_entrada > 12:
            data_mes_entrada = int(input('Informe o mês do aporte novamente: '))
        
    if escolha_menu == 2:
        valor_entrada = float(input('Informe o aporte inicial: $ '))
        data_dia_entrada = int(input('Informe o dia do aporte: '))
        while data_dia_entrada < 1 or data_dia_entrada > 31:
            data_dia_entrada = int(input('Informe o dia do aporte novamente: '))
        data_mes_entrada = int(input('Informe o mês do aporte: '))
        while data_mes_entrada < 1 or data_mes_entrada > 12:
            data_mes_entrada = int(input('Informe o mês do aporte novamente: '))
        
    if escolha_menu == 3:
        valor_entrada = float(input('Informe o aporte inicial: € '))
        data_dia_entrada = int(input('Informe o dia do aporte: '))
        while data_dia_entrada < 1 or data_dia_entrada > 31:
            data_dia_entrada = int(input('Informe o dia do aporte novamente: '))
        data_mes_entrada = int(input('Informe o mês do aporte: '))
        while data_mes_entrada < 1 or data_mes_entrada > 12:
            data_mes_entrada = int(input('Informe o mês do aporte novamente: '))

    global data_aporte = str(data_dia_entrada) + '/' + str(data_mes_entrada)

def menu_carteira():
    print('a')


def menu_aplicativo():
    opcao = int(input('1 - Apostas'
            '\n2 - Carteira'
            '\n3 - Sair\n'))

    if opcao == 1:
        opcao_apostas = int(input('MENU APOSTAS'
                            '\n1 - Nova Aposta'
                            '\n2 - Apostas do Dia'
                            '\n3 - Histórico'
                            '\n4 - Voltar\n'))
        #if opcao_apostas == 1:
            

    if opcao == 2:
        opcao_carteira = int(input('MENU CARTEIRA'
                            '\n1 - Aporte Inicial'
                            '\n2 - Valor Atual'
                            '\n3 - Voltar\n'))
        if opcao_carteira == 1:
            menu_moeda()

    if opcao == 3:
        print('Saindo...')
        exit()
    if opcao > 3 or opcao < 1:
        print('Opção inválida!\nSelecione a opção novamente:')
        menu_aplicativo()

# total = int(input('Informe a quantidade de dias que irá apostar: '))
#     dias = int(input(''))

#     print('DIA {}'.format(x))    
#     input('SITE: ')
#     input('JOGO: ')
#     input('APOSTA: ')
#     input('VALOR APOSTADO: R$ ')
#     input('ODDS: ')
#     input('Resultado (w/L): ')
#     print('RESUMO DA APOSTA')
#     print('PREVISÃO DE RETORNO: ')
#     print('RESULTADO: ')

#     aposta = 1
#     for x in range(1, aposta):
#         aposta += 1

# menuMoeda() 

# valorInicial()

print('Seja bem-vindo!\nSelecione a opção desejada:')

menu_aplicativo()



