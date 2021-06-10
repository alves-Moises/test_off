def valida_inteiro():
    '''valida os valores'''
    valid = False
    while not valid:
        try:
            x = int(input())
        except ValueError:
            print('valid inválido')
        else:
            valid = True
    return x


def entrada_de_valores():
    '''pega os valores'''

    print('Digite o primeiro valor: ', end = '')
    a = valida_inteiro()
    print('Digite o segundo valor: ', end = '')
    b = valida_inteiro
    print('Digite o terceiro valor: ', end = '')
    c = valida_inteiro
    return [a, b, c]

def main():
    
    '''função principal'''
    print('''
        [1] Área do trapészio
        [2] Exponencial de valores
        [3] Média aritmética
        [4] Inteiros de 'a' até 'b'
        Digite a opção desejada:
        ''')
    i = valida_inteiro()
    '''seleciona opção'''
    

    lista_valores = entrada_de_valores()
    a = lista_valores[0]
    b = lista_valores[1]
    c = lista_valores[2]

    '''Verificação de valores'''
    if i == 1:
        h = c
        Areadotrapezio = ((a + b) * h)/2
        print('Area do trapezio: ', Areadotrapezio)

    elif i == 2:
        print(f'{a} * , {a}: ', a * a)
        print(f'{b} * , {b}: ', b * b)
        print(f'{c} * , {c}: ', c * c)

    elif i == 3:
        print(f'Média aritmética de {a}, {b}, {c}: ', ((a + b + c)/3))

    elif i == 4:
        x = a 
        soma = 0
        lista_somar = []
        while x < b:
            lista_somar.append(x)
            x += c

        for item in lista_somar:
            soma += item
            print(f'Valor atual: {item}')
        print(f'Soma: {soma}')

        print(f'Soma final: {soma}')

    else:
        print('Valor inválido')

main()