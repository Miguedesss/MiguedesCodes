numero = int(input('Quantas linhas: '))
primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero: '))

for i in range(numero):
    i = i * -1
    i += numero
    if (i <= segundo and i > primeiro):
        if(i >= 10):
            print(i, ' |')
        else:
            print(i, '  |')
    elif(i <= primeiro ):
        if(i >= 10):
            if(i <= primeiro and i <= segundo):
                print(str(i) + '|', '|')
            else:
                print(str(i) + '|')
        else:
            if(i <= primeiro and i <= segundo):
                print(i,'|', '|')
            else:
                print(i,'|')
    else:
        print(i)

print('  1 2')
