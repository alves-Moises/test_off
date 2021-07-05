# ==== definição das funções ====

def valida_inteiro():   
    #função para pegar valor inteiro 
    #valida os valores

    valid = False      #variavel de validação inicia como false         

    while not valid:   #enquanto a variavel de validação não for verdadeira, faça:
        try: #tente:
            x = int(input())  #x recebe o valor de entrada, formatado para o tipo inteiro
        except ValueError:    # exeção de erro de valor na validação
            print('valid inválido')   # imprimir erro 
        else:  # se não tiver erro:
            valid = True    #variavel de validação pega valor verdadeiro
    return x #retorna x

def entrada_de_valores():
    # Pega os valores de a, b, c

    print('Digite o primeiro valor: ', end = '') #mensagem requisitando para que o usuario digite um valor
    a = valida_inteiro()    #variável recebe valor inteiro que é retornado da função valida_inteiro()
    print('Digite o segundo valor: ', end = '') #mensagem requisitando para que o usuario digite um valor
    b = valida_inteiro()    #variável recebe valor inteiro que é retornado da função valida_inteiro()
    print('Digite o terceiro valor: ', end = '') #mensagem requisitando para que o usuario digite um valor
    c = valida_inteiro()    #variável recebe valor inteiro que é retornado da função valida_inteiro()

    return [a, b, c] # retorna uma lista com os valores das variaveis a, b, c
   

def main():
    
    # função principal
    print('''
        [1] Área do trapészio
        [2] Exponencial de valores
        [3] Média aritmética
        [4] Inteiros de 'a' até 'b'
        Digite a opção desejada:
        ''')
    #imprime as opções para o usuário
    i = valida_inteiro()  #usuario seleciona opção. Recebe valor de uma função para garantir uma resposta válida de acordo com as opções apresentadas
    
    lista_valores = entrada_de_valores()     #lista_valores recebe lista que é retornada da função entrada_de_valores()
    a = lista_valores[0]                     #variavel recebe valor da lista na posição 0
    b = lista_valores[1]                     #variavel recebe valor da lista na posição 1
    c = lista_valores[2]                     #variavel recebe valor da lista na posição 2

    #verificação das respostas
    if i == 1:                                          # se a resposta for igual a 1
        h = c                                           # avariavel 'h' recee o valor da variável 'c'
        Areadotrapezio = ((a + b) * h)/2                # calcula a área do trapézio com os valores de a, b, h
        print('Area do trapezio: ', Areadotrapezio)     # imprime  o resultado

    elif i == 2:                                      # se a resposta for igual a 2
        print('Exponencial dos valores: ')            # imprime um texto
        print(f'{a} * , {a}: ', a * a)                # imprime a resposta do exponencial de cada variavel
        print(f'{b} * , {b}: ', b * b)                # imprime a resposta do exponencial de cada variavel
        print(f'{c} * , {c}: ', c * c)                # imprime a resposta do exponencial de cada variavel

    elif i == 3:           # se a resposta for igual a 3
        print(f'Média aritmética de {a}, {b}, {c}: ', ((a + b + c)/3))    # calcula e imprime a media

    elif i == 4:            #   #se a resposta for igual a 4
        x = a               # variavel x recebe o valor da variavel 'a'
        soma = 0            #variavel 'soma' inicia com valor de 0 
        lista_somar = []    #lista_somar inicia como lista vazia 

        while x < b:               #laço de repetição para x < b  onde vai criar uma nova lista tendo como intervalo entre itens o valor da variável 'c'
            lista_somar.append(x)  #lista 
            x += c                   # variavel x é somada com o valor de c dentro do laço de repetição

        for item in lista_somar:              #laço de repetição ppara percorrer a lista criada anteriormente e somar os valores
            soma += item                      #somar os valores dos itens da lista
            print(f'Valor atual: {item}')     #imprimir o item o item atual da lista
        print(f'Soma: {soma}')                #imprime a soma dos itens

        print(f'Soma final: {soma}')          #prime resultado final

    else:  # se a resposta não for uma opção válida
        print('Valor inválido')  #imprime erro de entrada

main()  #chama a função main e inicia o programa