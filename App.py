def menuMoeda():
    escolhaMenu = input('Selecione uma moeda digitando seu número:' 
                '\n1 - Real'
                '\n2-  Dólar'
                '\n3-  Euro\n')

menuMoeda()

print(1 , escolhaMenu)

valorEntradaMoeda = 0.00

def valorInicial(escolhaMenu):
    while escolhaMenu == '1' or '2' or '3':
        if escolhaMenu == '1':
            valorEntrada = float(input('Informe o valor inicial: R$ '))
            valorEntradaMoeda = round(valorEntrada, 2)
            print(valorEntradaMoeda)
            print(type(valorEntradaMoeda))

        if escolhaMenu == '2':
            valorEntrada = float(input('Informe o valor inicial: $ '))
            valorEntradaMoeda = round(valorEntrada, 2)
            print(valorEntradaMoeda)
            print(type(valorEntradaMoeda))

        if escolhaMenu == '3':
            valorEntrada = float(input('Informe o valor inicial: € '))
            valorEntradaMoeda = round(valorEntrada, 2)
            print(valorEntradaMoeda)
            print(type(valorEntradaMoeda))
    else:
        print('Moeda inválida')
        menuMoeda()

valorInicial()

print(type(valorEntradaMoeda))

soma = 20 + valorEntradaMoeda

print(soma)



