from random import randint

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

def main(lista):
    '''função principal'''
    i = 0
    lista_iguais = 0
    '''pega valores da lista e verifica series de repetição'''
    while i < len(lista):
        if lista[i] == lista[i-1] and lista[i] != lista[i-2] or lista[i] == lista:
            lista_iguais += 1
        i +=  1

    print('Total de sequencias iguais: ', lista_iguais)
       
'''inicio'''
lista = []
resposta = ''
while not resposta == 'n':
    print('Digite um valor: ')
    lista.append(valida_inteiro())
    resposta = str(input('Você deseja continuar? s/n ')).lower()

main(lista)
