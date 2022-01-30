num = int(input("Digite a quantidade de números a ser avaliados: "))
quantidade = 0
x = 2

while quantidade <= num:
    if x == 2:
        print("{} é primo!".format(x))
        quantidade += 1
    elif x == 3:
        print("{} é primo!".format(x))
        quantidade += 1
    else:
        if x % 2 != 0:
            primo = True
            y = 3

            while y < x:
                if x % y == 0:
                    primo = False
                y += 1

            if primo:
                print("{} é primo!".format(x))
    quantidade += 1
    x += 1


