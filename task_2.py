n_1 = int(input())
zn = float(input())
c = int(input())
while c != 0:
    a = n_1 * zn
    print(a, end=' ')
    if n_1 != a:
        n_1 = a
    c -= 1
        

