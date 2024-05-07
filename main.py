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

print('\t','1','\t', '2', '\t', '3', '\t', '4')
print('\t','=','\t', '=', '\t', '=', '\t', '=')

for column in range(1, x + 1):
    print(column, "|", end="\t")
    for row in range(1, x + 1):
        print(column * row, end="\t")
    print()