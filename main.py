print('Learn your squares and cubes!')
print()

while True:
    x = input('Enter a number >> ')
    x = int(x)
    print()

    print('Number', 'Squared', 'Cubed')
    print('======', '======', '======')

    a = 0
    b = 0
    c = 0

    for a in range(0, x, 1) :
        a += 1
        b = a ** 2
        c = a ** 3
        print(a, b, c)

    decision = input('Continue? y/n >> ')
    decision = str(decision)

    if decision != 'y':
        break