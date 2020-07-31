valorEntradaMoeda = 0.00

def menuMoeda():
    global escolha_menu
    escolha_menu = int(input('Selecione uma moeda digitando seu número:' 
                '\n1 - Real'
                '\n2 -  Dólar'
                '\n3 -  Euro\n'))

menuMoeda()

def valorInicial():
    while escolha_menu > 3 or escolha_menu < 1:
        print('Moeda inválida!')
        menuMoeda()
    else:
        if escolha_menu == 1:
            valorEntrada = float(input('Informe o valor inicial: R$ '))
            valorEntradaMoeda = round(valorEntrada, 2)
            print(valorEntradaMoeda)

        if escolha_menu == 2:
            valorEntrada = float(input('Informe o valor inicial: $ '))
            valorEntradaMoeda = round(valorEntrada, 2)
            print(valorEntradaMoeda)

        if escolha_menu == 3:
            valorEntrada = float(input('Informe o valor inicial: € '))
            valorEntradaMoeda = round(valorEntrada, 2)
            print(valorEntradaMoeda)

valorInicial()



