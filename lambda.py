def inpt():
    valid = False
    while not valid:
        try:
            x = int(input("Digite um valor: "))
        except ValueError:
            print("valor inválido")
        else:
            valid = True
    return x

def main():
    a = lambda l, c: l * c
    x = inpt()
    y = inpt()
    print(a(x, y))
main()