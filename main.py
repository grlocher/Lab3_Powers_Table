print('Learn your squares and cubes!')
print()

while True:
    x = input('Enter a number >> ')
    x = int(x)
    print()

    print('Number', 'Squared', 'Cubed')
    print('======', '======', '======')

    for a in range(0, x, 1) :
        a += 1
        b = a ** 2
        c = a ** 3
        print(a,'\t\t', b, '\t\t', c)

    decision = input('Continue? y/n >> ')
    decision = str(decision)

    if decision != 'y':
        break