while True:

    print('\nSelecione a opção desejada: ')
    opção = int(input('1 - Juros simples \n2 - Juros compostos \n3 - Sair \n\nOpção desejada: '))
    if opção == 3:
        break

    if opção != 1 and opção != 2:
        print('Opção inválida, selecione uma opção disponível')
        continue

    deposito = float(input('\nQual o valor do depósito? '))
    juros = float(input('Qual a taxa de juros? '))
    taxa = juros / 100                   #TAXA DE JUROS EM PORCENTAGEM 
    tempo = int(input('Qual o período em meses? '))

    if opção == 1:
        J = deposito * taxa * tempo      # "J" Juros. 
        M = deposito * tempo + J         # "M" Montante == Total.

        if tempo == 1:
            print(f'\nNo final de {tempo} mês, você terá um total de R${M :.2f}.')

        if tempo > 1:
            print(f'\nNo final de {tempo} meses, você terá um total de R${M :.2f}.')

    if opção == 2:
        A = (1 + taxa)**tempo            # "A" apenas o nome da variável.
        T = deposito * tempo * A         # "T" Montante == Total.

        if tempo == 1:
            print(f'\nNo final de {tempo} mês, você terá um total de R${T :.2f}.')

        if tempo > 1:
            print(f'\nNo final de {tempo} meses, você terá um total de R${T :.2f}.')

print('\nPrograma encerrado!')

