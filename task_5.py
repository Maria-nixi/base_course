n1, n2 = int(input()), int(input())

if n2 == 0:
    print('На 0 делить нельзя!')
else:
    if n1 % n2 == 0:
        print(f'число - {n1} делиться на {n2}. Будет: {n1 // n2}')
    else:
        print(f'число - {n1} делиться на {n2}. Будет: {n1 // n2}')
        print(f'остаток: {n1 % n2}')

