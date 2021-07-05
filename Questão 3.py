def valida_escolha():
    #valida escolha do menu
    valid = False # variavel de validação inicia como False

    while not valid == True:           # laço de repetição para validar a entada de valores
        try:                           # tentar fazer a validação
            x = int(input())           # x recebe o valor de entrada formatado para o tipo inteiro
        except ValueError:             # erro de valor
            print('Resposta inválida') # imprime erro 
        else: valid = True             # se não tiver erro, variavel de validação passa a ser True
        if  ( not (x == 1 or x == 2 or x == 3 or x == 4) ): # se o valor de entrada não for uma resposta valida
            print('Resposta inválida.')   # imrpime erro
            valid = False              # invalida o processo
    return x  #retorna o valor de escolha

def valida_int():
    # valida input do tipo inteiro
    valid = False  #variavel de validação começa como False
    while not valid == True:      #laço de repetição que executa enquanto não obtiver um valor válido   
        try:   #tente:
            x = int(input())   # recebe um valor inteiro do input
        except ValueError:     # se der erro de valor
            print('Resposta inválida')   #imprime erro
        else: valid = True     # se não tivber erro, torna a variável válida

    return x   #retorna o valor recebido

def pesquisa_pessoa(matriz):
    #pesquisar pessoa na matriz
    pesquisa = input('Digite a função a se pesquisar: ')  #rebe a função a qual se deseja pesquisar
    valid = False  # variavel de validação
    for linha in matriz:                     # laço de repetição para percorrer a matriz
        if pesquisa in linha:                # verifica se a função pesquisada está na linha atual onde se está percorrendo
            print(linha)                     # imprime a linha atual se for o cargo requisitado
            valid = True                     # variavel de validação
    if valid == False:                       # se não tiver validaddo:
        print('Não encontrou')               # imprime  'não encontrou'

def pega_pessoa(matriz):
    #cria uma nova pessoa na matriz

    lista =[] #lista inicia vazia
    nome = input('Digite um nome: ')      #pega o nome da pessoa
    lista.append(nome)                    #adiciona o nome na lista 
    codigo = input('Digite o código :')   #pega o código
    lista.append(codigo)                  #adiciona o código na lista
    cargo = input('Digite o cargo: ')     #pega o cargo da pessoa
    lista.append(cargo)                   #adiciona o cargo na lista
    telefone = input('Digite o telefone: ')#pega o telefone da pessoa
    lista.append(telefone)                #adiciona o telefone na lista
    print(lista) #imprime a lista
    return lista #retorna a lista 

def imprimir_matriz(matriz):
    #imprime a matriz
    print('Lista de pessoas:') #imprime texto
    for linha in matriz:   #laço de repetição para percorrer a matriz e imprimir
        print(linha)       #imprime a linha atual da matriz

def main(matriz):
   
    #função principal
    print('''
        Selecione a opçõa dejesada:
            [1] Pesquisar por cargo
            [2] Adicionar pessoa
            [3] Imprimir todas   
            [4] Encerrar
        ''') #imprime as opções

    resposta = valida_escolha()   #pega a resposta depois de uma validação

    #verifica qual a opção foi escolhida
    if resposta == 4:                            #se resposta 4
        print('Obrigado por utilizar o programa')  #mensagem de encerramento
    else:   #se não desejou encerrar
        if resposta == 1:    #se resposta for 1
            pesquisa_pessoa(matriz)  #chama a função pesquisa_pessoa() e passa matriz como parâmetro

        elif resposta == 2:  #se resposta for 2
            matriz.append(pega_pessoa(matriz)) #adiciona à matriz o retorno da função pega_pessoa(), a qual retorna uma nova pessoa

        elif resposta == 3:  #se resposta for 3
            imprimir_matriz(matriz)   #chama função para imprimir matriz, onde passa como parâmetro a matriz
            
        main(matriz) # volta para o inicio do programa
 
#Lista inicial
pessoa_1 = ['AdalbertoFerreira',    '01091982',    'Gestão',   '(21)99281 − 29830']           #instancia nova lista pessoa com todas as informações
pessoa_2 = ['JulianaVasconcelos',   '011117220',   'RecursosHumanos',  '(21)99848 − 19020']   #instancia nova lista pessoa com todas as informações
pessoa_3 = ['FlaviaAmorim',         '11289380',    'Contabilidade',    '(22)99273 − 94040']   #instancia nova lista pessoa com todas as informações
lista_pessoas = [pessoa_1, pessoa_2, pessoa_3]  #instancia a matriz com 3 pessoas já adicionadas e com todas as informações

main(lista_pessoas) #inicio do programa com a lista_pessoas
