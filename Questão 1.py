# ======= funções ========
def valida_inteiro():
    #validar os valores
    
    valid = False  # variavel de validação
    while not valid: #laço de repetição enquanto não for valiado
        try:  #tente: 
            x = int(input()) # x recebe o valor do input formatado para o tipo inteiro
        except ValueError:   # se hoouver erro de tipo de valor
            print('valid inválido') #imprime erro
        else: #se não tiver erro:
            valid = True #a variavel de validação se torna True
    return x #retorna o valor  de x

def main(lista):
    #função principal

    i = 0   # variavel de controle, começando em zeero
    lista_iguais = 0  # lista de sequencia de repetições (contagem)
    #pega valores da lista e verifica series de repetição
    while i < len(lista):  # percorre a lista
        if lista[i] == lista[i-1] and lista[i] != lista[i-2] or lista[i] == lista:   #verifica se é uma sequencia de valores iguais
            lista_iguais += 1   #lista iguais aumenta em 1 caso seja sequencia
        i +=  1  #auto-incremento da variavel de controle

    print('Total de sequencias iguais: ', lista_iguais) #  imprime o total de sequencia de numeros iguais
       
# ====inicio do programa ====
lista = [] #lista incial vazia
resposta = ''   #resposta recebe vazio
while not resposta == 'n':    #enquanto o usuário não digigar 'n', continua adicionando valor
    print('Digite um valor: ')  #solicita o usuario para digitar um valor inteiro
    lista.append(valida_inteiro()) #lista adiciona o valor digitado pelo usuario depois de ter sido validado pela função valida_inteiro
    resposta = str(input('Você deseja continuar? s/n ')).lower()   #pergunta se o usuario quer continuar a adicionar valores

main(lista) #chama a função principal passando como parâmetro a lista com os valores digitados
