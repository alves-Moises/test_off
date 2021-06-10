import random
import copy
def jogo():
    maior = tabuleiro[0][0]
    for linha in tabuleiro:
        for elemento in linha:
            if elemento > maior:
                maior = elemento
                
    numEspacos = len(str(maior))
    
                
    for linha in tabuleiro:
        linhaAtual = '|'
        for elemento in linha:
            if elemento == 0:
                linhaAtual += ' ' * numEspacos + '|'
            else:
                linhaAtual +=(' ' * (numEspacos - len(str(elemento))))+ str(elemento) + '|'
        print(linhaAtual)
    print()

def empurraLinhas(linha):
    for i in range(3):
        for j in range(3,0,-1):
            if linha[j - 1] == 0:
                linha[j - 1] = linha[j]
                linha[j] = 0
    for j in range(3):
        if linha[j] == linha[j + 1]:
            linha[j] *= 2
            linha[j+1] = 0
    for j in range(3,0,-1):
        if linha[j-1] == 0:
            linha[j-1] = linha[j]
            linha[j] = 0
    return linha

def empurraEsquerda(tabuleiroAtual):
    for j in range(4):
        tabuleiroAtual[j] = empurraLinhas(tabuleiroAtual[j])
    return tabuleiroAtual

def inversa(linha):
    novo = []
    for j in range(3, -1, -1):
        novo.append(linha[j])
    return novo

def empurraDireita(tabuleiroAtual):
    for j in range(4):
        tabuleiroAtual[j] = inversa(tabuleiroAtual[j])
        tabuleiroAtual[j] = empurraLinhas(tabuleiroAtual[j])
        tabuleiroAtual[j] = inversa(tabuleiroAtual[j])
    return tabuleiroAtual

def transposta(tabuleiroAtual):
    for i in range(4):
        for j in range(i,4):
            if not j == i:
                trans = tabuleiroAtual[i][j]
                tabuleiroAtual[i][j] = tabuleiroAtual[j][i]
                tabuleiroAtual[j][i] = trans
    return tabuleiroAtual

def empurraCima(tabuleiroAtual):
    tabuleiroAtual = transposta(tabuleiroAtual)
    tabuleiroAtual = empurraEsquerda(tabuleiroAtual)
    tabuleiroAtual = transposta(tabuleiroAtual)
    return tabuleiroAtual

def empurraBaixo(tabuleiroAtual):
    tabuleiroAtual = transposta(tabuleiroAtual)
    tabuleiroAtual = empurraDireita(tabuleiroAtual)
    tabuleiroAtual = transposta(tabuleiroAtual)
    return tabuleiroAtual

def novoValor():
    if random.randint(1,10) == 1:
        return 4
    else:
        return 2

def addNovoValor():
    linNum = random.randint(0, 3)
    colNum = random.randint(0, 3)
    while not tabuleiro[linNum][colNum] == 0:
        linNum = random.randint(0, 3)
        colNum = random.randint(0, 3)
    tabuleiro[linNum][colNum] = novoValor()

def semMovimentos():
    transTab1 = copy.deepcopy(tabuleiro)
    transTab2 = copy.deepcopy(tabuleiro)
    transTab1 = empurraBaixo(transTab1)
    if transTab1 == transTab2:
        transTab1 = empurraCima(transTab1)
        if transTab1 == transTab2:
            transTab1 = empurraEsquerda(transTab1)
            if transTab1 == transTab2:
                transTab1 = empurraDireita(transTab1)
                if transTab1 == transTab2:
                    return True
    return False

def vitoria():
    for linha in tabuleiro:
        if 2**int(x) in linha:
            return True      
    return False
def novo_jogo():
    tabuleiro = []
    for j in range(4):
        linha = []
        for i in range(4):
            linha.append(0)
        tabuleiro.append(linha)
    numPrec = 2
    while numPrec > 0:
        linNum = random.randint(0, 3)
        colNum = random.randint(0, 3)
        if tabuleiro[linNum][colNum] == 0:
            tabuleiro[linNum][colNum] = novoValor()
            numPrec -= 1
    
tabuleiro = []
for j in range(4):
    linha = []
    for i in range(4):
        linha.append(0)
    tabuleiro.append(linha)
numPrec = 2
while numPrec > 0:
    linNum = random.randint(0, 3)
    colNum = random.randint(0, 3)
    if tabuleiro[linNum][colNum] == 0:
        tabuleiro[linNum][colNum] = novoValor()
        numPrec -= 1
print('Bem vindo ao jogo 2048! Seu objetivo é juntar as peças de mesmo valor até se chegar a 2048 (ou o valor selecionado).Para isso, para mover o tabuleiro à esquerda, use a tecla "a";para cima, use a tecla "w";para direita, usa a tecla "d"; para baixo, use a tecla "s". Divirta-se!!:')
x  = input('Escolha a potência de 2 em que se deseja atingir a pontuação, (ex:.3 será 2**3 = 8): ')
while x == '':
     x = 2048
jogo()
fimDeJogo = False
while not fimDeJogo:
    movimento = input('Para qual lado deseja mover o tabuleiro? ')
    valida = True
    transTab = copy.deepcopy(tabuleiro)
    if movimento == 'd':
        tabuleiro = empurraDireita(tabuleiro)
    elif movimento == 'w':
        tabuleiro = empurraCima(tabuleiro)
    elif movimento == 'a':
        tabuleiro = empurraEsquerda(tabuleiro)
    elif movimento == 's':
        tabuleiro = empurraBaixo(tabuleiro)
    else:
         valida = False
    if not valida:
        print('Oops,tecla errada! Tente outra tecla válida!! ')
    else:
        if tabuleiro == transTab:
            print('Oops,tente uma direção diferente!! ')
        else:
            if vitoria():
                jogo()
                print('Parabéns! Você venceu!! ')
                y = input('Deseja continuar a jogar? ')
                if y == 'sair':
                    fimDeJogo = True
                elif y == 'recomeçar':
                    fimDeJogo = True
                    novo_jogo()
            else:
                addNovoValor()
        jogo()
        if semMovimentos():
            print('Vish, não há movimentos possíveis,você perdeu :( !')
            fimDeJogo = True





            
    
