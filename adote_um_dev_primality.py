def int_input():
    valid = False
    while not valid:
        try:
            x = int(input())
        except ValueError:
            print('Wrong value. Try again')
        else:
            valid = True
    return x



def get_prim(x = 0):
    i = 1
    m = 0

    while i < x + 1:
        if x % i == 0:
            # print(f'{x} // {i}: ', x % i)
            m += 1
        i += 1
    print(m)
    
    if m == 2:
        valid = True
    else:
        valid = False

    return(valid)

def main():
    valid = False
    list_number = []
    while not valid:
        print('A number, please: ', end = '')
        x = int_input()
        if not(get_prim(x)):
            list_number.append(x)
        else:
            valid = True

    print('Número primo.')
    print(list_number)
main()