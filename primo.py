num = int(input('Digite um numero: '))
soma_divisiveis = 0
for n in range(1, num+1):
    if num % n == 0:
        soma_divisiveis += 1 

if soma_divisiveis == 2:       
    print(f'O {num} é primo')
else:
    print(f'O {num} nao é primo')