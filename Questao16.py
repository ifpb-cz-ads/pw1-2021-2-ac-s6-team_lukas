num = int(input("Digite um número: "))
primo = True

if num % 2 != 0:
    x = 3

    while x <= num:
        if x % 2 != 0:
            if num != x and num % x == 0:
                primo = False
        x += 1
else:
    primo = False

if primo:
    print('É primo')
else:print("Não é primo")