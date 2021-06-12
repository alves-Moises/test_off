def valida_escolha():
    '''valida escolha do menu'''
    valid = False

    while not valid == True:
        lista_resposta = [1, 2, 3]
        try: 
            x = int(input())
        except ValueError:
            print('Resposta inválida')
        else: valid = True
        if  ( not (x == 1 or x == 2 or x == 3) ):
            print('Resposta inválida.')
            valid = False
    return x

def valida_int():
    '''valida input do tipo inteiro'''
    valid = False

    while not valid == True:
        try: 
            x = int(input())
        except ValueError:
            print('Resposta inválida')
        else: valid = True

    return x

def pesquisa_pessoa(matriz):
    '''pesquisar pessoa na matriz'''
    pesquisa = input('Digite a função a se pesquisar: ')
    resposta_pesquisa = []
    valid = False
    for linha in matriz:
        if pesquisa in linha:
            print(linha)
            valid = True
            # print('aa', linha)
    if valid == False:
        print('Não encontrou')

def pega_pessoa(matriz):
    '''cria uma nova pessoa na matriz'''
    lista =[]
    nome = input('Digite um nome: ')
    lista.append(nome)
    codigo = input('Digite o código :')
    lista.append(codigo)
    cargo = input('Digite o cargo: ')
    lista.append(cargo)
    telefone = lista.append(input('Digite o telefone: '))
    lista.append(telefone)
    print(lista)
    return lista

def imprimir_matriz(matriz):
    '''imprime a matriz'''
    print('Lista de pessoas:')
    for linha in matriz:
        print(linha)

def main(matriz):
   
    '''função principal'''
    print('''
        Selecione a opçõa dejesada:
            [1] Pesquisar por cargo
            [2] Adicionar pessoa
            [3] Imprimir todas 
            [4] Encerrar
    ''')
    resposta = valida_escolha()
    if resposta == 4:
        print('Obrigado por utilizar o programa')
    else:
        if resposta == 1:
            pesquisa_pessoa(matriz)

        elif resposta == 2: 
            matriz.append(pega_pessoa(matriz))

        elif resposta == 3:
            imprimir_matriz(matriz)
            
        main(matriz)
 
'''Lista inicial'''
pessoa_1 = ['AdalbertoFerreira',    '01091982',    'Gestão',   '(21)99281 − 29830']
pessoa_2 = ['JulianaVasconcelos',   '011117220',   'RecursosHumanos',  '(21)99848 − 19020']
pessoa_3 = ['FlaviaAmorim',         '11289380',    'Contabilidade',    '(22)99273 − 94040']
lista_pessoas = [pessoa_1, pessoa_2, pessoa_3]

main(lista_pessoas)
